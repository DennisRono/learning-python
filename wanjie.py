import os


# # def files(dirname, filesize):
# #     try:
# #         files = list(filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)]))
# #         return files
# #     except:
# #         print("an error ocured")

# # print(files("venv", 200))

def main():
    dirName = 'venv';
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    print(listOfFiles)
if __name__ == '__main__':
    main()