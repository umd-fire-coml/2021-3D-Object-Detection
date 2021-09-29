from download.accelerator import DownloadAccelerator
import hashlib
import pathlib

def test_download_accelerator():
    output_directory = pathlib.Path("data/temp_storage")
    if not output_directory.exists():
        output_directory.mkdir(parents=True)
    
    output_file = output_directory / "picture.jpg"
    file_url = "https://images.unsplash.com/photo-1594058573823-d8edf1ad3380?ixid=MnwxMjA3fDF8MHxzZWFyY2h8MXx8Y2l0eXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60"

    accelerator = DownloadAccelerator(file_url, output_file)
    accelerator.start()

    with open(output_file, 'rb') as file:
        assert(hashlib.md5(file.read()).hexdigest() == "07e0563800acd088fceae7161065ba6a")
