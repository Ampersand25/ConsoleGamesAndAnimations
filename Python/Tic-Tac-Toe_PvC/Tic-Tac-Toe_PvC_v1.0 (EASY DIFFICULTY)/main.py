#A Player VS Generated Intelligence
#print("\033[1;32;40m") for green text
#print("\033[1;33;40m") for yellow text
#print("\033[1;37;40m") for white text
import random, os, pickle
def stats_display():
    g = open('statistics.txt','w')
    g.write(' Statistics:\n-Total games played: %d\n-Nr. of wins: %d\n-Nr. of draws: %d\n-Nr. of loses: %d' % (sts[0], sts[1], sts[2], sts[3]))
    g.close()
def type(matrix):
    print(' ' * 2, end = "")
    for x in range(3):
        print(x + 1, end = " ")
    print()
    for x in range(3):
        print(x + 1, end = " ")
        for y in range(3):
            if matrix[x][y] is 1:
                print('\033[1;32;40mX\033[1;37;40m', end = "")
            elif matrix[x][y] is 2:
                print('\033[1;33;40m0\033[1;37;40m', end = "")
            else:
                print('_', end = "")
            if y <= 1:
                print('/', end = "")
        print('\n')
def end_game(matrix):
    for x in range(3):
        for y in range(3):
            if matrix[x][y] == 0:
                return False
    return True
def player(name):
    print('\033[1;32;40m%s WINNER!' % name)
def computer():
    print('\033[1;33;40m%s WINNER!' % 'Computer')
def function(sc1, sc2):
    stats_display()
    end = False
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    print('Choose who to start the game:\n1)\033[1;32;40mYou\033[1;37;40m\n2)\033[1;33;40mThe computer\033[1;37;40m\n3)\033[1;32;40mRan\033[1;33;40mdom\033[1;37;40m')
    turn = int(input('Answer: '))
    while turn != 1 and turn != 2 and turn != 3:
        print('\n\x1b[1;31;40m\033[4mInvalid answer\033[0m\x1b[1;31;40m!\x1b[1;37;40m')
        turn = int(input('Try again: '))
    if turn == 3:
        turn = random.randint(0, 1)
    else:
        turn -= 1
    while not end_game(matrix):
        os.system('CLS')
        if turn % 2 == 0:
            type(matrix)
            print('\033[1;32;40m \033[4m%s\033[0m\033[1;32;40m' % name)
            l = int(input('-line: '))
            while l < 1 or l > 3:
                print(' Line index out of range!\n-line: ', end = "")
                l = int(input())
            l -= 1
            c = int(input('-column: '))
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
                c = int(input('-column: '))
                while c < 1 or c > 3:
                    print(' Column index out of range!\n-column: ', end = "")
                    c = int(input())
                c -= 1
        else:
            l = random.randint(0,2)
            c = random.randint(0,2)
            while matrix[l][c] != 0:
                l = random.randint(0,2)
                c = random.randint(0,2)
        if turn % 2 == 0:
            matrix[l][c] = 1
        else:
            matrix[l][c] = 2
        print()
        print('\033[1;37;40m', end = "")
        if matrix[0][c] == matrix[1][c] and matrix[1][c] == matrix[2][c]:
            os.system('CLS')
            type(matrix)
            if matrix[0][c] == 1:
                sc1 += 1
                sts[1] += 1
                player(name)
            else:
                sc2 += 1
                sts[3] += 1
                computer()
            print('\033[1;37;40m', end = "")
            end = True
            break
        if matrix[l][0] == matrix[l][1] and matrix[l][1] == matrix[l][2]:
            os.system('CLS')
            type(matrix)
            if matrix[l][0] == 1:
                sc1 += 1
                sts[1] += 1
                player(name)
            else:
                sc2 += 1
                sts[3] += 1
                computer()
            print('\033[1;37;40m', end = "")
            end = True
            break
        if l == c and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            os.system('CLS')
            type(matrix)
            if matrix[l][c] == 1:
                sc1 += 1
                sts[1] += 1
                player(name)
            else:
                sc2 += 1
                sts[3] += 1
                computer()
            print('\033[1;37;40m', end = "")
            end = True
            break
        if l + c == 2 and matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
            os.system('CLS')
            type(matrix)
            if matrix[l][c] == 1:
                sc1 += 1
                sts[1] += 1
                player(name)
            else:
                sc2 += 1
                sts[3] += 1
                computer()
            print('\033[1;37;40m', end = "")
            end = True
            break
        turn += 1
    if end == False:
        sts[2] += 1
        os.system('CLS')
        type(matrix)
        print('TIE!')
        end = True
    if end == True:
        sts[0] += 1
        with open('stats.txt', 'wb') as file:
            pickle.dump(sts, file)
        stats_display()
        print('\n\033[4mGeneral score\033[0m\x1b[1;37;40m: \033[1;32;40m%s |%d|\033[1;37;40m : \033[1;33;40m|%d| %s\033[1;37;40m' % (name, sc1, sc2, 'Computer'))
        print('\nPress:\n1)For a new game\n2)For the end of the current game')
        ans = int(input('Enter your answer here: '))
        while ans != 1 and ans != 2:
            print('\n\x1b[1;31;40m\033[4mInvalid answer\033[0m\x1b[1;31;40m!\x1b[1;37;40m')
            ans = int(input('Try again: '))
        if ans is 1:
            os.system('CLS')
            function(sc1, sc2)
        else:
            return 0
try:
    with open('stats.txt', 'rb') as file:
        sts = pickle.load(file)
except:
    sts = [0, 0, 0, 0]
print('\033[1;37;40m', end = "")
name, sc1, sc2 = input('Enter your name: '), 0, 0
print('\n \033[1;37;40m\033[4mRules\033[0m\033[1;37;40m:\033[1;32;40m\n%s = X\033[1;33;40m\n%s = 0\033[1;37;40m' % (name, 'Computer'), end = "\n\n")
function(sc1, sc2)
