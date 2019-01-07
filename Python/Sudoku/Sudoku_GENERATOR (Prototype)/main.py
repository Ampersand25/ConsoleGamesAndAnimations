import random, os, sys
def zone(line, col):
    if line >= 0 and line <= 2 and col >= 0 and col <= 2:
        return 1
    if line >= 0 and line <= 2 and col >= 3 and col <= 5:
        return 2
    if line >= 0 and line <=2 and col >=6 and col <= 8:
        return 3
    if line >= 3 and line <= 5 and col >= 0 and col <= 2:
        return 4
    if line >= 3 and line <= 5 and col >= 3 and col <= 5:
        return 5
    if line >= 3 and line <=5 and col >=6 and col <= 8:
        return 6
    if line >= 6 and line <= 8 and col >= 0 and col <= 2:
        return 7
    if line >= 6 and line <= 8 and col >= 3 and col <= 5:
        return 8
    return 9
def conv(line, col):
    if zone(line, col) == 1 or zone(line, col) == 9:
        print('\033[1;37;41m', end = "")
    elif zone(line, col) == 2 or zone(line, col) == 8:
        print('\033[1;37;42m', end = "")
    elif zone(line, col) == 3 or zone(line, col) == 7:
        print('\033[1;37;43m', end = "")
    elif zone(line, col) == 4:
        print('\033[1;37;44m', end = "")
    elif zone(line, col) == 5:
        print('\033[1;37;45m', end = "")
    else:
        print('\033[1;37;46m', end = "")
def type(matrix):
    print(' ' * 3, end = "")
    for x in range(9):
        print(x + 1, end = " ")
    print()
    for x in range(9):
        print('%d ' % (x + 1), end = " ")
        for y in range(9):
            if matrix[x][y]:
                conv(x, y)
                print(matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
            else:
                conv(x, y)
                print('-', end = " ")
                print('\033[1;37;40m', end = "")
        print()
def typee(matrix):
    f = open('generator.txt','w')
    for x in range(9):
        for y in range(9):
            if matrix[x][y]:
                f.write('%d' % matrix[x][y])
            else:
                f.write('0')
            if y < 8:
                f.write(' ')
        f.write('\n')
    f.close()
def func(nr_el):
    okok = True
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    k = 0
    while k < nr_el:
        line, col = random.randint(0, 8), random.randint(0, 8)
        while matrix[line][col] != 0:
            line, col = random.randint(0, 8), random.randint(0, 8)
        v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if matrix[i][col] != 0:
                v[matrix[i][col]] = 1
            if matrix[line][i] != 0:
                v[matrix[line][i]] = 1
        if zone(line, col) == 1:
            for i in range(0, 3):
                for j in range(0, 3):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 2:
            for i in range(0, 3):
                for j in range(3, 6):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 3:
            for i in range(0, 3):
                for j in range(6, 9):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 4:
            for i in range(3, 6):
                for j in range(0, 3):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 5:
            for i in range(3, 6):
                for j in range(3, 6):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 6:
            for i in range(3, 6):
                for j in range(6, 9):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 7:
            for i in range(6, 9):
                for j in range(0, 3):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        elif zone(line, col) == 8:
            for i in range(6, 9):
                for j in range(3, 6):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if matrix[i][j] != 0:
                        v[matrix[i][j]] = 1
        vs, cont = [], 0
        for i in range(1, 10):
            if v[i] == 0:
                cont += 1
                vs.append(i)
        if cont >= 1:
            val = random.randint(0, cont - 1)
            val = vs[val]
            matrix[line][col] = val
            k += 1
        elif cont == 0:
            okok = False
            func(nr_el)
    if okok == True:
        type(matrix)
        typee(matrix)
        sys.exit()
#main function
print('\x1b[1;37;40m', end = "")
nr_el = int(input('Choose the number of elements from [0, 81]: '))
while nr_el < 0 or nr_el > 81:
    nr_el = int(input('Value out of range!\nTry another number: '))
func(nr_el)
