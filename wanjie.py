import os

def files(dirname, filesize):
    print([(os.path +file) for file in os.listdir(dirname) if os.path.getsize(file) > filesize])

files("./venv", 2000)