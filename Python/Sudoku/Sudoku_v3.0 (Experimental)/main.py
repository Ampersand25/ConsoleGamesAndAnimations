#A generated configuration of the Sudoku table
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
        print('\033[1;37;46m', end = "")
    elif zone(line, col) == 2 or zone(line, col) == 8:
        print('\033[1;37;45m', end = "")
    elif zone(line, col) == 3 or zone(line, col) == 7:
        print('\033[1;37;44m', end = "")
    elif zone(line, col) == 4:
        print('\033[1;37;43m', end = "")
    elif zone(line, col) == 5:
        print('\033[1;37;42m', end = "")
    else:
        print('\033[1;37;41m', end = "")
def convv(line, col):
    if zone(line, col) == 1 or zone(line, col) == 9:
        print('\033[1;30;46m', end = "")
    elif zone(line, col) == 2 or zone(line, col) == 8:
        print('\033[1;30;45m', end = "")
    elif zone(line, col) == 3 or zone(line, col) == 7:
        print('\033[1;30;44m', end = "")
    elif zone(line, col) == 4:
        print('\033[1;30;43m', end = "")
    elif zone(line, col) == 5:
        print('\033[1;30;42m', end = "")
    else:
        print('\033[1;30;41m', end = "")
def type(matrix):
    print(' ' * 3, end = "")
    for x in range(9):
        print(x + 1, end = " ")
    print()
    for x in range(9):
        print('%d ' % (x + 1), end = " ")
        for y in range(9):
            if matrix[x][y] > 0:
                conv(x, y)
                print(matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
            elif matrix[x][y] < 0:
                convv(x, y)
                print(-matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
            else:
                conv(x, y)
                print('-', end = " ")
                print('\033[1;37;40m', end = "")
        print()
def typee(matrix):
    h = open('matrix.out','w')
    for x in range(9):
        for y in range(9):
            if matrix[x][y]:
                h.write('%d' % matrix[x][y])
            else:
                h.write('0')
            if y < 8:
                h.write(' ')
        h.write('\n')
    h.close()
def complete(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return False
    return True
def win(matrix):
    if complete(matrix) == False:
        return False
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        for j in range(9):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        for j in range(9):
            if car[matrix[j][i]]:
                return False
            car[matrix[j][i]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        for j in range(0, 3):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        for j in range(3, 6):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        for j in range(6, 9):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, 6):
        for j in range(0, 3):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, 6):
        for j in range(3, 6):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, 6):
        for j in range(6, 9):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(6, 9):
        for j in range(0, 3):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(6, 9):
        for j in range(3, 6):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(6, 9):
        for j in range(6, 9):
            if car[matrix[i][j]]:
                return False
            car[matrix[i][j]] = 1
    return True
def func():
    okok = True
    print('\x1b[1;37;40m', end = "")
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    nr_el = random.randint(24, 36)
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
            func()
    if okok == True:
        type(matrix)
        typee(matrix)
        while True:
            lin = int(input('\n-line: '))
            while lin < 1 or lin > 9:
                print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m')
                lin = int(input('-line: '))
            lin -= 1
            col = int(input('-column: '))
            while col < 1 or col > 9:
                print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m')
                col = int(input('-column: '))
            col -= 1
            while matrix[lin][col]:
                print("\x1b[1;31;40mYou can't change the initial configuration of the game!\x1b[1;37;40m")
                lin = int(input('-line: '))
                while lin < 1 or lin > 9:
                    print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m')
                    lin = int(input('-line: '))
                lin -= 1
                col = int(input('-column: '))
                while col < 1 or col > 9:
                    print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m')
                    col = int(input('-column: '))
                col -= 1
            val = int(input('-value: '))
            while val < 1 or val > 9:
                print('\x1b[1;31;40mError!\x1b[1;37;40m')
                val = int(input('-value: '))
            matrix[lin][col] = -val
            os.system('CLS')
            type(matrix)
            if win(matrix):
                print('\n\033[1;33;40mCongratulations, you have successfully completed the game!\033[1;37;40m')
                g = open('solution.out','w')
                for x in range(9):
                    for y in range(9):
                        if matrix[x][y]:
                            g.write('%d' % matrix[x][y])
                        if y < 8:
                            g.write(' ')
                    g.write('\n')
                g.close()
                print('\n\033[4mPress\033[0m\x1b[1;37;40m:\n1)For a new game\n2)For the end of the current game')
                ans = int(input('Enter your answer here: '))
                while ans != 1 and ans != 2:
                    print('\n\x1b[1;31;40mInvalid answer!\x1b[1;37;40m')
                    ans = int(input('Try again: '))
                if ans is 1:
                    os.system('CLS')
                    func()
                else:
                    sys.exit()
func()
