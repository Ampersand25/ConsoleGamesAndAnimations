'''
print('\x1b[1;31;40m') 4 red txt
print('\x1b[1;32;40m') 4 green txt
print('\x1b[1;33;40m') 4 yellow txt
print('\x1b[1;34;40m') 4 blue txt
print('\x1b[1;35;40m') 4 pink txt
print('\x1b[1;36;40m') 4 cyan txt
print('\x1b[1;37;40m') 4 white txt
2 4 8 16 32 64 128 256 512 1024 2048 - the positive powers of 2 until 2048 (except 1)
'''
import random, os
def win_game(matrix):
    for i in range(4):
        if matrix[i][i] == 2048:
            return True
        for j in range(i + 1, 4):
            if matrix[i][j] == 2048 or matrix[j][i] == 2048:
                return True
    return False
def is_full(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
    return True
def game_over(matrix):
    if is_full(matrix) == False or win_game(matrix) == True:
        return False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1]:
                return False
    for i in range(4):
        for j in range(3):
            if matrix[j][i] == matrix[j + 1][i]:
                return False
    return True
def nr_cif(cont):
    if not cont:
        return 1
    var = 0
    while cont:
        var += 1
        cont //= 10
    return var
def el_max(matrix, col):
    mx = 0
    for i in range(4):
        if matrix[i][col] > mx:
            mx = matrix[i][col]
    return mx
def red():
    print('\x1b[1;31;40m', end = "")
def green():
    print('\x1b[1;32;40m', end = "")
def yellow():
    print('\x1b[1;33;40m', end = "")
def blue():
    print('\x1b[1;34;40m', end = "")
def pink():
    print('\x1b[1;35;40m', end = "")
def cyan():
    print('\x1b[1;36;40m', end = "")
def white():
    print('\x1b[1;37;40m', end = "")
def convert(elem):
    if elem == 2 or elem == 128:
        red()
    elif elem == 4 or elem == 256:
        green()
    elif elem == 8 or elem == 512:
        yellow()
    elif elem == 16 or elem == 1024:
        blue()
    elif elem == 32:
        pink()
    elif elem == 64:
        cyan()
def special():
    red()
    print(2, end = "")
    green()
    print(0, end = "")
    pink()
    print(4, end = "")
    cyan()
    print(8, end = "")
def color(ind):
    if ind == 0:
        white()
    elif ind % 6 == 0:
        red()
    elif ind % 6 == 1:
        green()
    elif ind % 6 == 2:
        yellow()
    elif ind % 6 == 3:
        blue()
    elif ind % 6 == 4:
        pink()
    else:
        cyan()
def type(matrix, score, val, num):
    if num:
        print('Number of moves = %d' % num)
    print('\x1b[1;37;41mScore\x1b[1;37;40m ', end = "")
    color(val)
    print('%d\n\x1b[1;37;40m' % score[0])
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != 0 and matrix[i][j] != 2048:
                convert(matrix[i][j])
                print('%d' % matrix[i][j], end = "")
                print('\x1b[1;37;40m', end = "")
            elif matrix[i][j] == 2048:
                special()
                print('\x1b[1;37;40m', end = "")
            else:
                print('*', end = "")
            k = nr_cif(el_max(matrix, j)) - nr_cif(matrix[i][j]) + 1
            print(' ' * k, end = "")
        print('\n')
def up(matrix, score):
    for i in range(4):
        if matrix[0][i] != 0 and matrix[1][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[1][i] = 0
            if matrix[2][i] != 0 and matrix[2][i] == matrix[3][i]:
                matrix[2][i] *= 2
                score[0] += matrix[2][i]
                matrix[3][i] = 0
        elif matrix[0][i] != 0 and matrix[1][i] == 0 and matrix[2][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[2][i] = 0
        elif matrix[0][i] != 0 and matrix[1][i] == 0 and matrix[2][i] == 0 and matrix[3][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[3][i] = 0
        elif matrix[1][i] != 0 and matrix[2][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[2][i] = 0
        elif matrix[1][i] != 0 and matrix[2][i] == 0 and matrix[3][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[3][i] = 0
        elif matrix[2][i] != 0 and matrix[3][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[3][i] = 0
    for i in range(4):
        if matrix[2][i] == 0 and matrix[3][i] != 0:
            matrix[2][i] = matrix[3][i]
            matrix[3][i] = 0
        if matrix[1][i] == 0 and matrix[2][i] != 0:
            matrix[1][i] = matrix[2][i]
            matrix[2][i] = 0
            if matrix[3][i] != 0:
                matrix[2][i] = matrix[3][i]
                matrix[3][i] = 0
        if matrix[0][i] == 0 and matrix[1][i]:
            matrix[0][i] = matrix[1][i]
            matrix[1][i] = 0
            if matrix[2][i] != 0:
                matrix[1][i] = matrix[2][i]
                matrix[2][i] = 0
                if matrix[3][i] != 0:
                    matrix[2][i] = matrix[3][i]
                    matrix[3][i] = 0
def down(matrix, score):
    for i in range(4):
        if matrix[3][i] != 0 and matrix[2][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[2][i] = 0
            if matrix[1][i] != 0 and matrix[1][i] == matrix[0][i]:
                matrix[1][i] *= 2
                score[0] += matrix[1][i]
                matrix[0][i] = 0
        elif matrix[3][i] != 0 and matrix[2][i] == 0 and matrix[1][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[1][i] = 0
        elif matrix[3][i] != 0 and matrix[2][i] == 0 and matrix[1][i] == 0 and matrix[0][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[0][i] = 0
        elif matrix[2][i] != 0 and matrix[1][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[1][i] = 0
        elif matrix[2][i] != 0 and matrix[1][i] == 0 and matrix[0][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[0][i] = 0
        elif matrix[1][i] != 0 and matrix[0][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[0][i] = 0
    for i in range(4):
        if matrix[1][i] == 0 and matrix[0][i] != 0:
            matrix[1][i] = matrix[0][i]
            matrix[0][i] = 0
        if matrix[2][i] == 0 and matrix[1][i] != 0:
            matrix[2][i] = matrix[1][i]
            matrix[1][i] = 0
            if matrix[0][i] != 0:
                matrix[1][i] = matrix[0][i]
                matrix[0][i] = 0
        if matrix[3][i] == 0 and matrix[2][i]:
            matrix[3][i] = matrix[2][i]
            matrix[2][i] = 0
            if matrix[1][i] != 0:
                matrix[2][i] = matrix[1][i]
                matrix[1][i] = 0
                if matrix[0][i] != 0:
                    matrix[1][i] = matrix[0][i]
                    matrix[0][i] = 0
def left(matrix, score):
    for i in range(4):
        if matrix[i][0] != 0 and matrix[i][1] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][1] = 0
            if matrix[i][2] != 0 and matrix[i][2] == matrix[i][3]:
                matrix[i][2] *= 2
                score[0] += matrix[i][2]
                matrix[i][3] = 0
        elif matrix[i][0] != 0 and matrix[i][1] == 0 and matrix[i][2] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][2] = 0
        elif matrix[i][0] != 0 and matrix[i][1] == 0 and matrix[i][2] == 0 and matrix[i][3] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][3] = 0
        elif matrix[i][1] != 0 and matrix[i][2] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][2] = 0
        elif matrix[i][1] != 0 and matrix[i][2] == 0 and matrix[i][3] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][3] = 0
        elif matrix[i][2] != 0 and matrix[i][3] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][3] = 0
    for i in range(4):
        if matrix[i][2] == 0 and matrix[i][3] != 0:
            matrix[i][2] = matrix[i][3]
            matrix[i][3] = 0
        if matrix[i][1] == 0 and matrix[i][2] != 0:
            matrix[i][1] = matrix[i][2]
            matrix[i][2] = 0
            if matrix[i][3] != 0:
                matrix[i][2] = matrix[i][3]
                matrix[i][3] = 0
        if matrix[i][0] == 0 and matrix[i][1]:
            matrix[i][0] = matrix[i][1]
            matrix[i][1] = 0
            if matrix[i][2] != 0:
                matrix[i][1] = matrix[i][2]
                matrix[i][2] = 0
                if matrix[i][3] != 0:
                    matrix[i][2] = matrix[i][3]
                    matrix[i][3] = 0
def right(matrix, score):
    for i in range(4):
        if matrix[i][3] != 0 and matrix[i][2] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][2] = 0
            if matrix[i][1] != 0 and matrix[i][1] == matrix[i][0]:
                matrix[i][1] *= 2
                score[0] += matrix[i][1]
                matrix[i][0] = 0
        elif matrix[i][3] != 0 and matrix[i][2] == 0 and matrix[i][1] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][1] = 0
        elif matrix[i][3] != 0 and matrix[i][2] == 0 and matrix[i][1] == 0 and matrix[i][0] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][0] = 0
        elif matrix[i][2] != 0 and matrix[i][1] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][1] = 0
        elif matrix[i][2] != 0 and matrix[i][1] == 0 and matrix[i][0] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][0] = 0
        elif matrix[i][1] != 0 and matrix[i][0] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][0] = 0
    for i in range(4):
        if matrix[i][1] == 0 and matrix[i][0] != 0:
            matrix[i][1] = matrix[i][0]
            matrix[i][0] = 0
        if matrix[i][2] == 0 and matrix[i][1] != 0:
            matrix[i][2] = matrix[i][1]
            matrix[i][1] = 0
            if matrix[i][0] != 0:
                matrix[i][1] = matrix[i][0]
                matrix[i][0] = 0
        if matrix[i][3] == 0 and matrix[i][2]:
            matrix[i][3] = matrix[i][2]
            matrix[i][2] = 0
            if matrix[i][1] != 0:
                matrix[i][2] = matrix[i][1]
                matrix[i][1] = 0
                if matrix[i][0] != 0:
                    matrix[i][1] = matrix[i][0]
                    matrix[i][0] = 0
def copy(m1, m2):
    for i in range(4):
        for j in range(4):
            m1[i][j] = m2[i][j]
def same(m1, m2):
    for i in range(4):
        for j in range(4):
            if m1[i][j] != m2[i][j]:
                return False
    return True
def func():
    num = 0
    mat = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
    cmat = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    l, c = random.randint(0, 3), random.randint(0, 3)
    mat[l][c] = 2
    l, c = random.randint(0, 3), random.randint(0, 3)
    while mat[l][c] != 0:
        l, c = random.randint(0, 3), random.randint(0, 3)
    mat[l][c], val, score, typo = 2, 0, [0], 0
    type(mat, score, val, num)
    while game_over(mat) == False and win_game(mat) == False:
        copy(cmat, mat)
        print('\033[4mDirection\033[0m:', end = "")
        print('\x1b[1;37;40m', end = " ")
        str = input()
        if str == 'w' or str == 'W':
            up(mat, score)
        elif str == 's' or str == 'S':
            down(mat, score)
        elif str == 'a' or str == 'A':
            left(mat, score)
        elif str == 'd' or str == 'D':
            right(mat, score)
        else:
            print('\033[91mInvalid command!\033[0m\n')
            print('\x1b[1;37;40m', end = "")
        if same(cmat,mat) == False:
            l, c = random.randint(0, 3), random.randint(0, 3)
            while mat[l][c] != 0:
                l, c = random.randint(0, 3), random.randint(0, 3)
            mat[l][c] = 2
        if score[0] != typo:
            val += 1
            typo = score[0]
        if same(cmat, mat) == False:
            num += 1
            os.system('CLS')
            type(mat, score, val, num)
    if game_over(mat) == True:
        print('\x1b[1;37;41mGame over!\x1b[1;37;40m')
    else:
        print('\x1b[1;37;43mCongratulations, you won!\x1b[1;37;40m')
    print('\nPress:\n1)For a new game\n2)For the end of the current game')
    ans = int(input('Enter your answer here: '))
    while ans != 1 and ans != 2:
        print('\n\x1b[1;31;40mInvalid answer!\x1b[1;37;40m')
        ans = int(input('Try again: '))
    if ans is 1:
        os.system('CLS')
        func()
    else:
        return 0
#main function
print('\x1b[1;37;40m', end = "")
print('Welcome to ', end = "")
special()
print('\x1b[1;37;40m!')
print('\n\x1b[1;31;40m\033[4mHOW TO PLAY\033[0m\x1b[1;37;40m:\nUse the W/A/S/D or w/a/s/d keys to move the tiles in the direction you want.\nWhen two tiles with the same number touch, they merge into one!\n')
print('Created by \x1b[1;31;40mGabriele Cirulli\x1b[1;37;40m.\nBased on 1024 by Veewo Studio and conceptually similar to Threes by Asher Vollmer.\n')
os.system("PAUSE")
os.system('CLS')
func()
