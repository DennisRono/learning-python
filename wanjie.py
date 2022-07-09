import os


def files(dirname, filesize):
    try:
        files = filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)])
        return files
    except:
        print("an error ocured")

print(files("venv", 2000))
