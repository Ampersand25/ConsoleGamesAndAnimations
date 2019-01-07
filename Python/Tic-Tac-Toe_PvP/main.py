#A Player VS Player Tic-Tac-Toe Game
#print("\033[1;36;40m") for cyan text
#print("\033[1;35;40m") for purple text
#print("\033[1;37;40m") for white text
import os, sys, random
def type(matrix):
    print(' ' * 2, end = "")
    for x in range(3):
        print(x + 1, end = " ")
    print()
    for x in range(3):
        print(x + 1, end = " ")
        for y in range(3):
            if matrix[x][y] is 1:
                print('\033[1;36;40mX\033[1;37;40m', end = " ")
            elif matrix[x][y] is 2:
                print('\033[1;35;40m0\033[1;37;40m', end = " ")
            else:
                print('_', end = " ")
        print('\n')
def end_game(matrix):
    for x in range(3):
        for y in range(3):
            if matrix[x][y] == 0:
                return False
    return True
def function(sc1, sc2):
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    tie = True
    print('Choose who to start the game:\n1)\033[1;36;40m%s\033[1;37;40m\n2)\033[1;35;40m%s\033[1;37;40m\n3)\033[1;36;40mRan\033[1;35;40mdom\033[1;37;40m' % (p1, p2))
    turn = int(input('\033[4mAnswer\033[0m\x1b[1;37;40m: '))
    while turn != 1 and turn != 2 and turn != 3:
        print('\n\x1b[1;31;40m\033[4mInvalid answer\033[0m\x1b[1;31;40m!\x1b[1;37;40m')
        turn = int(input('Try again: '))
    if turn == 3:
        turn = random.randint(0, 1)
    else:
        turn -= 1
    os.system('CLS')
    while not end_game(matrix):
        type(matrix)
        if turn % 2 == 0:
            print(' \033[4m\033[1;36;40m%s\033[0m\033[1;36;40m' % p1)
        else:
            print(' \033[4m\033[1;35;40m%s\033[0m\033[1;35;40m' % p2)
        print('-line: ', end = "")
        l = int(input())
        while l < 1 or l > 3:
            print(' Line index out of range!\n-line: ', end = "")
            l = int(input())
        l -= 1
        print('-column: ', end = "")
        c = int(input())
        while c < 1 or c > 3:
            print(' Column index out of range!\n-column: ', end = "")
            c = int(input())
        c -= 1
        while matrix[l][c] != 0:
            print(' Position already taken!\n-line: ', end = "")
            l = int(input())
            while l < 1 or l > 3:
                print(' Line index out of range!\n-line: ', end = "")
                l = int(input())
            l -= 1
            print('-column: ', end = "")
            c = int(input())
            while c < 1 or c > 3:
                print(' Column index out of range!\n-column: ', end = "")
                c = int(input())
            c -= 1
        if turn % 2 == 0:
            matrix[l][c] = 1
        else:
            matrix[l][c] = 2
        print()
        print('\033[1;37;40m', end = "")
        os.system('CLS')
        if matrix[0][c] == matrix[1][c] and matrix[1][c] == matrix[2][c]:
            type(matrix)
            if matrix[0][c] == 1:
                print('\033[1;36;40m\033[4m%s WINNER\033[0m\033[1;36;40m!\033[1;37;40m' % p1)
                sc1 += 1
            else:
                print('\033[1;35;40m\033[4m%s WINNER\033[0m\033[1;35;40m!\033[1;37;40m' % p2)
                sc2 += 1
            tie = False
            break
        if matrix[l][0] == matrix[l][1] and matrix[l][1] == matrix[l][2]:
            type(matrix)
            if matrix[l][0] == 1:
                print('\033[1;36;40m\033[4m%s WINNER\033[0m\033[1;36;40m!\033[1;37;40m' % p1)
                sc1 += 1
            else:
                print('\033[1;35;40m\033[4m%s WINNER\033[0m\033[1;35;40m!\033[1;37;40m' % p2)
                sc2 += 1
            tie = False
            break
        if l == c and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            type(matrix)
            if matrix[l][c] == 1:
                print('\033[1;36;40m\033[4m%s WINNER\033[0m\033[1;36;40m!\033[1;37;40m' % p1)
                sc1 += 1
            else:
                print('\033[1;35;40m\033[4m%s WINNER\033[0m\033[1;35;40m!\033[1;37;40m' % p2)
                sc2 += 1
            tie = False
            break
        if l + c == 2 and matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
            type(matrix)
            if matrix[l][c] == 1:
                print('\033[1;36;40m\033[4m%s WINNER\033[0m\033[1;36;40m!\033[1;37;40m' % p1)
                sc1 += 1
            else:
                print('\033[1;35;40m\033[4m%s WINNER\033[0m\033[1;35;40m!\033[1;37;40m' % p2)
                sc2 += 1
            tie = False
            break
        turn += 1
    if tie:
        type(matrix)
        print('\033[4mTIE\033[0m\x1b[1;37;40m!')
    print('General score: \033[1;36;40m%s |%d|\033[1;37;40m : \033[1;35;40m|%d| %s\033[1;37;40m' % (p1, sc1, sc2, p2))
    print('\n\033[4mPress\033[0m\x1b[1;37;40m:\n1)For a new round\n2)For the end of the game')
    ans = int(input('Enter your answer here: '))
    while ans != 1 and ans != 2:
        print('\n\x1b[1;31;40m\033[4mInvalid answer\033[0m\x1b[1;31;40m!\x1b[1;37;40m')
        ans = int(input('Try again: '))
    if ans is 1:
        os.system('CLS')
        function(sc1, sc2)
    else:
        sys.exit()
sc1, sc2 = 0, 0
print(' \033[1;37;40m\033[4mRules\033[0m\x1b[1;37;40m:\n\033[1;36;40mPlayer 1 = X\n\033[1;35;40mPlayer 2 = 0\033[1;36;40m', end = "\n" * 2)
p1 = input('Player 1: ')
print('\033[1;35;40m', end = "")
p2 = input('Player 2: ')
print('\033[1;37;40m', end = "")
os.system('CLS')
function(sc1, sc2)
