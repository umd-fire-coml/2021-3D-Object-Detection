from os import system
from pathlib import Path
import requests
from threading import Thread
from queue import Queue

class DownloadAccelerator:
    def __init__(self, url, output, chunk_size=int(5e6), num_workers=30):
        print(f"Initializing download accelerator for {output}")
        print("\tRequesting file size")
        headers = {key.lower(): val.lower() for key, val in requests.head(url).headers.items()}
        content_length = int(headers['content-length'])

        added_chunk = 0 if (content_length % chunk_size == 0) else 1
        num_chunks = content_length // chunk_size
        num_chunks += added_chunk

        print("\tChunking file")
        chunks = Queue()

        for chunk in range(num_chunks):
            chunk_start = chunk * chunk_size
            chunk_end = chunk_start + chunk_size - 1
            if chunk_end >= content_length:
                chunk_end = content_length - 1
            chunks.put((chunk, chunk_start, chunk_end))

        self.chunks = chunks
        self.num_chunks = num_chunks
        self.output = output
        self.url = url
        self.completed_chunks = 0
        self.num_workers = num_workers

    def set_chunk_complete(self):
        self.completed_chunks += 1
        print(f"Completed {self.completed_chunks} out of {self.num_chunks} chunks.", end='\r', flush=True)
    
    def worker_task(self):
        while not self.chunks.empty():
            chunk_index, chunk_start, chunk_end = self.chunks.get()
            with open(f"{self.output}.part.{chunk_index}", 'wb') as output_file:
                r = requests.get(self.url, headers={'Range': f"bytes={chunk_start}-{chunk_end}"})
                output_file.write(r.content)
                self.set_chunk_complete()
                self.chunks.task_done()

    def spawn_workers(self):
        print(f"Spawning {self.num_workers} workers...")
        for i in range(0, self.num_workers):
            new_thread = Thread(target=self.worker_task)
            new_thread.start()

        self.chunks.join()

    def reconstruct_file(self):
        print("Reconstructing the output file from the partial files")
        system(f"cat {self.output}.part.* > {self.output}")
        print("Deleting partial files")
        system(f"rm {self.output}.part.*")

    def start(self):
        self.spawn_workers()
        self.reconstruct_file()