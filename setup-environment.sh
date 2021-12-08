#!/bin/bash
echo "Setting up environment"
echo "Getting rid of any existing venv folder"
rm -rf venv
echo "Creating a new virtual environment"
python3 -m venv venv
echo "Activating that virtual environment"
. venv/bin/activate
echo "Installing all dependencies"
pip3 install -r requirements.txt
echo "Done!"