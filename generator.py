# Defining Functions for generation
def x2(x):
    return 1+x**2


def x3(x):
    return 1+x**2+x**3

# Opening file system
filex2 = open('data/datax2', "w+")
filex2.write('Number,Value\n')
for i in range(1000):
    filex2.write(f'{(i)},{i**2}\n')
filex2.close()

filex3 = open('data/datax3', "w+")
filex3.write('Number,Value\n')
for i in range(1000):
    filex3.write(f'{(i)},{i**3}\n')
filex3.close()