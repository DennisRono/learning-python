import os

def files(dirname, filesize):
    filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)])

files("venv", 2000)
