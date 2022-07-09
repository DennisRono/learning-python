import os

def filterFileBySize(dirname, filesize):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    files = list(filter(lambda x:os.path.getsize(x)>filesize, listOfFiles))
    for r in files:
        f = open("results.txt", "a")
        f.write(r)
    f.close()


filterFileBySize("venv", 250000)