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

print([(os.path + file) for file in os.listdir("venv") if os.path.getsize(file) > 200])