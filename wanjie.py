import os


# # def files(dirname, filesize):
# #     try:
# #         files = list(filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)]))
# #         return files
# #     except:
# #         print("an error ocured")

# # print(files("venv", 200))

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def main():
    dirName = 'venv';
    # listOfFiles = getListOfFiles(dirName)
    # for elem in listOfFiles:
    #     print(elem)
    # print ("****************")
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    for elem in listOfFiles:
        print(elem)
if __name__ == '__main__':
    main()