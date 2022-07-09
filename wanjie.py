# import os

# def files(dirname, filesize):
#     print([(os.path +file) for file in os.listdir(dirname) if os.path.getsize(file) > filesize])
#     filter(lambda x:os.path.getsize>20000L, [os.path.join(dir, x) for x in os.listdir(dir)])

# files("./venv", 2000)

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# using filter function
filtered = filter(fun, sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)