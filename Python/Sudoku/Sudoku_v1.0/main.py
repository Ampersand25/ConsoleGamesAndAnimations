import os, random
def type(matrix, cmat):
    print(' ' * 3, end = "")
    for x in range(9):
        print(x + 1, end = " ")
    print()
    for x in range(9):
        print('%d |' % (x + 1), end = "")
        for y in range(9):
            if matrix[x][y] is cmat[x][y] and matrix[x][y] is not 0:
                print(matrix[x][y], end = "|")
            elif matrix[x][y] is not 0 and matrix[x][y] > 0:
                print('\033[1;32;40m%d\033[1;37;40m' % matrix[x][y], end = "|")
            elif matrix[x][y] is not 0 and matrix[x][y] < 0:
                print('\033[1;31;40m%d\033[1;37;40m' % -matrix[x][y], end = "|")
            else:
                print(' ', end = "|")
        print()
'''
def type2(matrix):
    print(' ' * 3, end = "")
    for x in range(9):
        print(x + 1, end = " ")
    print()
    print(' ' * 2, end = "")
    for x in range(9):
        print('-' * 2, end = "")
    print('-', end = "")
    print()
    for x in range(9):
        print('%d |' % (x + 1), end = "")
        for y in range(9):
            if matrix[x][y] is not 0:
                print(matrix[x][y], end = "|")
            else:
                print(' ', end = "|")
        print()
        print(' ' * 2, end = "")
        for y in range(9):
            print('-' * 2, end = "")
        print('-', end = "")
        print()
'''
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
        matrix = [[0, 2, 0, 0, 0, 0, 0, 0, 9],
                  [9, 0, 6, 0, 0, 2, 0, 0, 3],
                  [0, 0, 8, 0, 1, 9, 0, 7, 5],
                  [0, 0, 5, 1, 3, 0, 0, 9, 0],
                  [3, 7, 0, 0, 0, 0, 5, 0, 0],
                  [8, 1, 9, 0, 2, 5, 6, 3, 0],
                  [0, 4, 0, 0, 0, 1, 0, 5, 0],
                  [0, 0, 0, 9, 4, 7, 0, 0, 6],
                  [0, 9, 2, 0, 0, 0, 8, 0, 1]]
        cmat = [[0, 2, 0, 0, 0, 0, 0, 0, 9],
                [9, 0, 6, 0, 0, 2, 0, 0, 3],
                [0, 0, 8, 0, 1, 9, 0, 7, 5],
                [0, 0, 5, 1, 3, 0, 0, 9, 0],
                [3, 7, 0, 0, 0, 0, 5, 0, 0],
                [8, 1, 9, 0, 2, 5, 6, 3, 0],
                [0, 4, 0, 0, 0, 1, 0, 5, 0],
                [0, 0, 0, 9, 4, 7, 0, 0, 6],
                [0, 9, 2, 0, 0, 0, 8, 0, 1]]
        sol = [[1, 2, 7, 3, 5, 8, 4, 6, 9],
               [9, 5, 6, 4, 7, 2, 1, 8, 3],
               [4, 3, 8, 6, 1, 9, 2, 7, 5],
               [2, 6, 5, 1, 3, 4, 7, 9, 8],
               [3, 7, 4, 8, 9, 6, 5, 1, 2],
               [8, 1, 9, 7, 2, 5, 6, 3, 4],
               [6, 4, 3, 2, 8, 1, 9, 5, 7],
               [5, 8, 1, 9, 4, 7, 3, 2, 6],
               [7, 9, 2, 5, 6, 3, 8, 4, 1]]
        typee(matrix, 'Casual.TXT')
        typee(sol, 'Casual_SOLUTION.TXT')
    elif a is 2:
        dif = 'Medium'
        matrix = [[0, 0, 8, 4, 7, 0, 0, 3, 0],
                  [4, 0, 0, 0, 1, 8, 9, 0, 5],
                  [0, 0, 0, 0, 3, 6, 0, 7, 0],
                  [0, 0, 5, 1, 0, 0, 0, 0, 8],
                  [0, 0, 7, 3, 0, 9, 0, 0, 0],
                  [0, 0, 0, 0, 4, 0, 2, 5, 3],
                  [0, 0, 0, 5, 0, 0, 0, 0, 0],
                  [7, 3, 0, 0, 0, 0, 0, 8, 1],
                  [0, 2, 0, 7, 0, 3, 0, 4, 9]]
        cmat = [[0, 0, 8, 4, 7, 0, 0, 3, 0],
                [4, 0, 0, 0, 1, 8, 9, 0, 5],
                [0, 0, 0, 0, 3, 6, 0, 7, 0],
                [0, 0, 5, 1, 0, 0, 0, 0, 8],
                [0, 0, 7, 3, 0, 9, 0, 0, 0],
                [0, 0, 0, 0, 4, 0, 2, 5, 3],
                [0, 0, 0, 5, 0, 0, 0, 0, 0],
                [7, 3, 0, 0, 0, 0, 0, 8, 1],
                [0, 2, 0, 7, 0, 3, 0, 4, 9]]
        sol = [[6, 9, 8, 4, 7, 5, 1, 3, 2],
               [4, 7, 3, 2, 1, 8, 9, 6, 5],
               [1, 5, 2, 9, 3, 6, 8, 7, 4],
               [3, 4, 5, 1, 6, 2, 7, 9, 8],
               [2, 8, 7, 3, 5, 9, 4, 1, 6],
               [9, 1, 6, 8, 4, 7, 2, 5, 3],
               [8, 6, 4, 5, 9, 1, 3, 2, 7],
               [7, 3, 9, 6, 2, 4, 5, 8, 1],
               [5, 2, 1, 7, 8, 3, 6, 4, 9]]
        typee(matrix, 'Medium.TXT')
        typee(sol, 'Medium_SOLUTION.TXT')
    elif a is 3:
        dif = 'Hard'
        matrix = [[0, 0, 0, 0, 4, 8, 0, 0, 0],
                  [0, 0, 0, 0, 0, 6, 0, 9, 0],
                  [0, 0, 8, 0, 5, 0, 0, 7, 4],
                  [0, 0, 0, 0, 0, 4, 0, 0, 0],
                  [0, 0, 2, 3, 0, 9, 0, 0, 1],
                  [0, 3, 7, 0, 0, 0, 5, 4, 6],
                  [0, 4, 0, 8, 0, 0, 0, 0, 7],
                  [0, 9, 0, 0, 0, 5, 0, 1, 8],
                  [1, 0, 0, 0, 3, 0, 0, 0, 5]]
        cmat = [[0, 0, 0, 0, 4, 8, 0, 0, 0],
                [0, 0, 0, 0, 0, 6, 0, 9, 0],
                [0, 0, 8, 0, 5, 0, 0, 7, 4],
                [0, 0, 0, 0, 0, 4, 0, 0, 0],
                [0, 0, 2, 3, 0, 9, 0, 0, 1],
                [0, 3, 7, 0, 0, 0, 5, 4, 6],
                [0, 4, 0, 8, 0, 0, 0, 0, 7],
                [0, 9, 0, 0, 0, 5, 0, 1, 8],
                [1, 0, 0, 0, 3, 0, 0, 0, 5]]
        sol = [[3, 1, 9, 7, 4, 8, 6, 5, 2],
               [5, 7, 4, 2, 1, 6, 8, 9, 3],
               [6, 2, 8, 9, 5, 3, 1, 7, 4],
               [8, 6, 1, 5, 7, 4, 2, 3, 9],
               [4, 5, 2, 3, 6, 9, 7, 8, 1],
               [9, 3, 7, 1, 8, 2, 5, 4, 6],
               [2, 4, 5, 8, 9, 1, 3, 6, 7],
               [7, 9, 3, 6, 2, 5, 4, 1, 8],
               [1, 8, 6, 4, 3, 7, 9, 2, 5]]
        typee(matrix, 'Hard.TXT')
        typee(sol, 'Hard_SOLUTION.TXT')
    else:
        dif = 'Expert'
        matrix = [[0, 0, 0, 1, 0, 0, 0, 5, 2],
                  [6, 0, 0, 0, 0, 0, 8, 1, 0],
                  [0, 0, 0, 0, 6, 0, 0, 0, 0],
                  [0, 0, 0, 9, 7, 0, 3, 0, 0],
                  [9, 0, 5, 0, 0, 4, 0, 8, 0],
                  [0, 2, 0, 0, 0, 0, 0, 0, 0],
                  [7, 0, 0, 4, 0, 0, 9, 0, 0],
                  [0, 4, 0, 3, 0, 5, 0, 0, 8],
                  [8, 0, 0, 2, 0, 0, 0, 0, 0]]
        cmat = [[0, 0, 0, 1, 0, 0, 0, 5, 2],
                [6, 0, 0, 0, 0, 0, 8, 1, 0],
                [0, 0, 0, 0, 6, 0, 0, 0, 0],
                [0, 0, 0, 9, 7, 0, 3, 0, 0],
                [9, 0, 5, 0, 0, 4, 0, 8, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [7, 0, 0, 4, 0, 0, 9, 0, 0],
                [0, 4, 0, 3, 0, 5, 0, 0, 8],
                [8, 0, 0, 2, 0, 0, 0, 0, 0]]
        sol = [[3, 8, 7, 1, 4, 9, 6, 5, 2],
               [6, 9, 4, 5, 2, 3, 8, 1, 7],
               [5, 1, 2, 7, 6, 8, 4, 3, 9],
               [1, 6, 8, 9, 7, 2, 3, 4, 5],
               [9, 7, 5, 6, 3, 4, 2, 8, 1],
               [4, 2, 3, 8, 5, 1, 7, 9, 6],
               [7, 5, 1, 4, 8, 6, 9, 2, 3],
               [2, 4, 6, 3, 9, 5, 1, 7, 8],
               [8, 3, 9, 2, 1, 7, 5, 6, 4]]
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
