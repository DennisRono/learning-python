import os

def files(dirname, filesize):
    [(path +file) for file in os.listdir(dirname) if os.path.getsize(file) > filesize]