#Update (version 2.0): Better graphics and brand new levels
import os, random
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
def conv_error(line, col):
    if zone(line, col) == 1 or zone(line, col) == 9:
        print('\033[1;31;41m', end = "")
    elif zone(line, col) == 2 or zone(line, col) == 8:
        print('\033[1;31;42m', end = "")
    elif zone(line, col) == 3 or zone(line, col) == 7:
        print('\033[1;31;43m', end = "")
    elif zone(line, col) == 4:
        print('\033[1;31;44m', end = "")
    elif zone(line, col) == 5:
        print('\033[1;31;45m', end = "")
    else:
        print('\033[1;31;46m', end = "")
def type(matrix, cmat):
    print(' ' * 3, end = "")
    for x in range(9):
        print(x + 1, end = " ")
    print()
    for x in range(9):
        print('%d ' % (x + 1), end = " ")
        for y in range(9):
            if matrix[x][y] is cmat[x][y] and matrix[x][y] is not 0:
                conv(x, y)
                print(matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
            elif matrix[x][y] is not 0 and matrix[x][y] > 0:
                conv(x, y)
                print(matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
                cmat[x][y] = matrix[x][y]
            elif matrix[x][y] is not 0 and matrix[x][y] < 0:
                conv_error(x, y)
                print(-matrix[x][y], end = " ")
                print('\033[1;37;40m', end = "")
            else:
                conv(x, y)
                print('-', end = " ")
                print('\033[1;37;40m', end = "")
        print()
def typee(matrix, file_name):
    f = open('%s' % file_name,'w')
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
def result(matrix):
    for x in range(9):
        for y in range(9):
            if matrix[x][y] <= 0:
                return False
    return True
def function():
    print('\033[1;37;40m\033[4mWelcome to Sudoku\033[0m\033[1;37;40m!\n\nBefore you start, please choose the level of difficulty between:\n1)Easy\n2)Medium\n3)Hard\n4)Expert\n5)Random\nAnswer: ', end = "")
    a = int(input())
    while a < 1 or a > 5:
        print('\n\x1b[1;31;40mNon-existent option!\x1b[1;37;40m\nRe-enter your choice: ', end = "")
        a = int(input())
    if a is 5:
        a = random.randint(1, 4)
    os.system('CLS')
    if a is 1:
        dif = 'Easy'
        matrix = [[0, 0, 0, 0, 0, 0, 3, 0, 0],
                  [0, 2, 0, 0, 9, 0, 8, 0, 0],
                  [0, 4, 3, 6, 0, 0, 0, 0, 0],
                  [0, 9, 0, 1, 8, 4, 5, 6, 0],
                  [4, 0, 1, 7, 3, 6, 0, 0, 0],
                  [0, 6, 8, 0, 0, 0, 0, 4, 1],
                  [2, 0, 0, 0, 0, 9, 4, 3, 0],
                  [8, 0, 0, 5, 6, 3, 9, 0, 2],
                  [5, 0, 0, 4, 0, 0, 0, 7, 0]]
        cmat = [[0, 0, 0, 0, 0, 0, 3, 0, 0],
                [0, 2, 0, 0, 9, 0, 8, 0, 0],
                [0, 4, 3, 6, 0, 0, 0, 0, 0],
                [0, 9, 0, 1, 8, 4, 5, 6, 0],
                [4, 0, 1, 7, 3, 6, 0, 0, 0],
                [0, 6, 8, 0, 0, 0, 0, 4, 1],
                [2, 0, 0, 0, 0, 9, 4, 3, 0],
                [8, 0, 0, 5, 6, 3, 9, 0, 2],
                [5, 0, 0, 4, 0, 0, 0, 7, 0]]
        sol = [[1, 8, 5, 2, 4, 7, 3, 9, 6],
               [6, 2, 7, 3, 9, 1, 8, 5, 4],
               [9, 4, 3, 6, 5, 8, 1, 2, 7],
               [7, 9, 2, 1, 8, 4, 5, 6, 3],
               [4, 5, 1, 7, 3, 6, 2, 8, 9],
               [3, 6, 8, 9, 2, 5, 7, 4, 1],
               [2, 1, 6, 8, 7, 9, 4, 3, 5],
               [8, 7, 4, 5, 6, 3, 9, 1, 2],
               [5, 3, 9, 4, 1, 2, 6, 7, 8]]
        typee(matrix, 'Casual.TXT')
        typee(sol, 'Casual_SOLUTION.TXT')
    elif a is 2:
        dif = 'Medium'
        matrix = [[0, 9, 0, 1, 2, 0, 0, 8, 0],
                  [5, 0, 6, 0, 0, 0, 0, 0, 7],
                  [0, 0, 2, 0, 0, 7, 3, 0, 0],
                  [7, 0, 4, 8, 3, 0, 2, 0, 0],
                  [9, 0, 0, 0, 0, 0, 0, 0, 5],
                  [0, 0, 1, 0, 6, 9, 0, 0, 8],
                  [0, 8, 0, 0, 0, 0, 0, 6, 4],
                  [0, 0, 3, 9, 1, 4, 0, 0, 0],
                  [0, 0, 0, 5, 0, 0, 7, 1, 0]]
        cmat = [[0, 9, 0, 1, 2, 0, 0, 8, 0],
                [5, 0, 6, 0, 0, 0, 0, 0, 7],
                [0, 0, 2, 0, 0, 7, 3, 0, 0],
                [7, 0, 4, 8, 3, 0, 2, 0, 0],
                [9, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 1, 0, 6, 9, 0, 0, 8],
                [0, 8, 0, 0, 0, 0, 0, 6, 4],
                [0, 0, 3, 9, 1, 4, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 7, 1, 0]]
        sol = [[4, 9, 7, 1, 2, 3, 5, 8, 6],
               [5, 3, 6, 4, 9, 8, 1, 2, 7],
               [8, 1, 2, 6, 5, 7, 3, 4, 9],
               [7, 6, 4, 8, 3, 5, 2, 9, 1],
               [9, 2, 8, 7, 4, 1, 6, 3, 5],
               [3, 5, 1, 2, 6, 9, 4, 7, 8],
               [1, 8, 5, 3, 7, 2, 9, 6, 4],
               [6, 7, 3, 9, 1, 4, 8, 5, 2],
               [2, 4, 9, 5, 8, 6, 7, 1, 3]]
        typee(matrix, 'Medium.TXT')
        typee(sol, 'Medium_SOLUTION.TXT')
    elif a is 3:
        dif = 'Hard'
        matrix = [[0, 4, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 3, 0, 0, 9],
                  [7, 9, 0, 0, 0, 6, 0, 2, 0],
                  [5, 0, 0, 0, 9, 0, 1, 0, 7],
                  [0, 0, 8, 0, 6, 0, 0, 9, 4],
                  [0, 2, 9, 0, 0, 8, 0, 0, 0],
                  [0, 0, 0, 0, 3, 0, 7, 0, 0],
                  [0, 5, 7, 4, 1, 0, 0, 0, 0],
                  [0, 0, 3, 0, 8, 7, 0, 5, 0]]
        cmat = [[0, 4, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 9],
                [7, 9, 0, 0, 0, 6, 0, 2, 0],
                [5, 0, 0, 0, 9, 0, 1, 0, 7],
                [0, 0, 8, 0, 6, 0, 0, 9, 4],
                [0, 2, 9, 0, 0, 8, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 7, 0, 0],
                [0, 5, 7, 4, 1, 0, 0, 0, 0],
                [0, 0, 3, 0, 8, 7, 0, 5, 0]]
        sol = [[3, 4, 2, 9, 5, 1, 8, 7, 6],
               [6, 8, 1, 7, 2, 3, 5, 4, 9],
               [7, 9, 5, 8, 4, 6, 3, 2, 1],
               [5, 3, 6, 2, 9, 4, 1, 8, 7],
               [1, 7, 8, 3, 6, 5, 2, 9, 4],
               [4, 2, 9, 1, 7, 8, 6, 3, 5],
               [2, 6, 4, 5, 3, 9, 7, 1, 8],
               [8, 5, 7, 4, 1, 2, 9, 6, 3],
               [9, 1, 3, 6, 8, 7, 4, 5, 2]]
        typee(matrix, 'Hard.TXT')
        typee(sol, 'Hard_SOLUTION.TXT')
    else:
        dif = 'Expert'
        matrix = [[0, 0, 0, 0, 0, 3, 0, 2, 6],
                  [7, 1, 2, 0, 0, 0, 0, 0, 0],
                  [0, 6, 0, 0, 0, 0, 0, 0, 0],
                  [0, 4, 0, 1, 5, 0, 0, 0, 0],
                  [0, 0, 8, 0, 0, 9, 0, 0, 4],
                  [0, 0, 0, 0, 7, 4, 0, 0, 0],
                  [0, 3, 6, 0, 0, 8, 0, 9, 0],
                  [0, 0, 0, 9, 0, 0, 5, 7, 0],
                  [1, 9, 0, 0, 0, 2, 0, 0, 0]]
        cmat = [[0, 0, 0, 0, 0, 3, 0, 2, 6],
                [7, 1, 2, 0, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 0, 0, 0],
                [0, 4, 0, 1, 5, 0, 0, 0, 0],
                [0, 0, 8, 0, 0, 9, 0, 0, 4],
                [0, 0, 0, 0, 7, 4, 0, 0, 0],
                [0, 3, 6, 0, 0, 8, 0, 9, 0],
                [0, 0, 0, 9, 0, 0, 5, 7, 0],
                [1, 9, 0, 0, 0, 2, 0, 0, 0]]
        sol = [[9, 8, 5, 4, 1, 3, 7, 2, 6],
               [7, 1, 2, 6, 8, 5, 4, 3, 9],
               [4, 6, 3, 2, 9, 7, 8, 1, 5],
               [2, 4, 9, 1, 5, 6, 3, 8, 7],
               [6, 7, 8, 3, 2, 9, 1, 5, 4],
               [3, 5, 1, 8, 7, 4, 9, 6, 2],
               [5, 3, 6, 7, 4, 8, 2, 9, 1],
               [8, 2, 4, 9, 6, 1, 5, 7, 3],
               [1, 9, 7, 5, 3, 2, 6, 4, 8]]
        typee(matrix, 'Expert.TXT')
        typee(sol, 'Expert_SOLUTION.TXT')
    while True:
        print('\033[4mGame difficulty\033[0m\x1b[1;37;40m: %s' % dif, end = "\n\n")
        type(matrix, cmat)
        print()
        print('-line: ', end = "")
        l = int(input())
        while l < 1 or l > 9:
            print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m\n-line: ', end = "")
            l = int(input())
        l -= 1
        print('-column: ', end = "")
        c = int(input())
        while c < 1 or c > 9:
            print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m\n-column: ', end = "")
            c = int(input())
        c -= 1
        while cmat[l][c] != 0:
            print("\x1b[1;31;40mYou can't change the initial configuration of the game!\x1b[1;37;40m\n-line: ", end = "")
            l = int(input())
            while l < 1 or l > 9:
                print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m\n-line: ', end = "")
                l = int(input())
            l -= 1
            print('-column: ', end = "")
            c = int(input())
            while c < 1 or c > 9:
                print('\x1b[1;31;40mAccess violation!\x1b[1;37;40m\n-column: ', end = "")
                c = int(input())
            c -= 1
        print('-value: ', end = "")
        v = int(input())
        while v < 1 or v > 9:
            print('\x1b[1;31;40mError!\x1b[1;37;40m\n-value: ', end = "")
            v = int(input())
        if sol[l][c] is not v:
            matrix[l][c] = -v
        else:
            matrix[l][c] = v
        if result(matrix) is True:
            os.system('CLS')
            print('\033[4mGame difficulty\033[0m\x1b[1;37;40m: %s' % dif, end = "\n\n")
            type(matrix, cmat)
            print('\n\033[1;33;40mCongratulations, you have successfully completed the game on %s difficulty!\033[1;37;40m' % dif)
            print('\n\033[4mPress\033[0m\x1b[1;37;40m:\n1)For a new game\n2)For the end of the current game')
            ans = int(input('Enter your answer here: '))
            while ans != 1 and ans != 2:
                print('\n\x1b[1;31;40mInvalid answer!\x1b[1;37;40m')
                ans = int(input('Try again: '))
            if ans is 1:
                os.system('CLS')
                function()
            break
        os.system('CLS')
function()
