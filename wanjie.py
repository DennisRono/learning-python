# import os

# def files(dirname, filesize):
#     print([(os.path +file) for file in os.listdir(dirname) if os.path.getsize(file) > filesize])
#     filter(lambda x:os.path.getsize>20000L, [os.path.join(dir, x) for x in os.listdir(dir)])

# files("./venv", 2000)


# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
  
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))