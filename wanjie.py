# import os


# # def files(dirname, filesize):
# #     try:
# #         files = list(filter(lambda x:os.path.getsize(x)>filesize, [os.path.join(dirname, x) for x in os.listdir(dirname)]))
# #         return files
# #     except:
# #         print("an error ocured")

# # print(files("venv", 200))

# for x in os.listdir("venv"):
#     print(x)

import os

for fyle in os.listdir("venv"):
    if os.stat(fyle).st_size > 20000:
        print(fyle, os.stat(fyle).st_size)