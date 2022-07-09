import os


def files(dirname, filesize):
    try:
        filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)])
    except:
        print("an error ocured")

files("venv", 2000)
