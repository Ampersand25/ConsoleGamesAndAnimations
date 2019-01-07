import random
alpha = "abcdefghijklmnopqrstuvwxyz"
str = ""
print('\x1b[1;37;40m', end = "")
nr = int(input('Choose the length of the string: '))
for i in range(nr):
    str += alpha[random.randint(0, len(alpha) - 1)]
print('The generated string is: %s' % str)
g = open("string.out","w")
g.write(str)
g.close()
