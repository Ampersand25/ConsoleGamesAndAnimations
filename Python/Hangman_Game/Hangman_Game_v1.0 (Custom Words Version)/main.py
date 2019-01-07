import sys, os
def type():
    for i in range(len(str)):
        if car[i]:
            print(str[i], end = " ")
        else:
            print('_', end = " ")
def full():
    for i in range(len(str)):
        if car[i] == 0:
            return False
    return True
def draw():
    if cont == 0:
        file = open("drawing#1.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 1:
        file = open("drawing#2.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 2:
        file = open("drawing#3.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 3:
        file = open("drawing#4.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 4:
        file = open("drawing#5.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 5:
        file = open("drawing#6.txt","r")
        for line in file:
            print(line, end = "")
    else:
        file = open("drawing#7.txt","r")
        for line in file:
            print(line, end = "")
    file.close()
white, red = '\x1b[1;37;40m', '\x1b[1;31;40m'
print('%s' % white, end = "")
f = open('date.in','r')
str = f.read()
f.close()
#deleting the last character of the string str (the last character is a space)
str = str[:-1]
if str.isalpha() == False:
    print('%sInvalid word format!%s' % (red, white))
    sys.exit()
size = len(str)
if size <= 2:
    print('%sThe string entered is too short!%s' % (red, white))
    sys.exit()
car = []
for i in range(size):
    car.append(0)
car[0] = car[size - 1] = 1
for i in range(1, size - 1):
    if str[i].lower() == str[0].lower() or str[i].lower() == str[size - 1].lower():
        car[i] = 1
cont, hs = 0, ''
while full() == False:
    print('\033[4mLifes left\033[0m%s: %d\n' % (white, 6 - cont))
    draw()
    if cont == 6:
        print('%s' % red)
        for i in range(size):
            print(str[i], end = " ")
        print('%s' % white)
        print('\nYou lost. Better luck next time!')
        sys.exit()
    print()
    type()
    print('\n\n\033[4mEnter a letter\033[0m%s: ' % white, end = "")
    chr = input()
    while len(chr) != 1 or chr.isalpha() == False:
        print('\n%sThe character typed is not a letter!%s\n\033[4mTry again\033[0m%s: ' % (red, white, white), end = "")
        chr = input()
    if str.count(chr.lower()) or str.count(chr.upper()):
        for i in range(size):
            if str[i].lower() == chr.lower():
                car[i] = 1
    elif hs.count(chr.lower()) == 0:
        cont += 1
    hs += chr.lower()
    os.system('CLS')
print('\033[4mLifes left\033[0m%s: %d\n' % (white, 6 - cont))
draw()
print()
type()
print('\n\nCongratulations! You guessed the hidden word!')
