#Player VS AI
#Impossible Difficulty
#print('\x1b[1;31;40m') for red txt
#print('\x1b[1;34;40m') for blue txt
#print('\033[1;37;40m') for white text
import random, os, pickle
red, blue, white, und, eund = '\x1b[1;31;40m', '\x1b[1;34;40m', '\033[1;37;40m', '\033[4m', '\033[0m'
def stats_display():
    g = open('statistics.txt','w')
    g.write(' Statistics:\n-Total games played: %d\n-Nr. of wins: %d (oviously)\n-Nr. of draws: %d\n-Nr. of loses: %d' % (sts[0], sts[1], sts[2], sts[3]))
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
                print('%sX%s' % (red, white), end = "")
            elif matrix[x][y] is 100:
                print('%s0%s' % (blue, white), end = "")
            else:
                print('_', end = "")
            if y <= 1:
                print('/', end = "")
        print('\n')
def end_game(matrix):
    for x in range(3):
        for y in range(3):
            if not matrix[x][y]:
                return False
    return True
def computer():
    print('%s%s WINNER!' % (blue, 'Computer'))
def win(matrix):
    if (matrix[0][0] + matrix[1][1] + matrix[2][2] is 200) or (matrix[0][2] + matrix[1][1] + matrix[2][0] is 200):
        return True
    for x in range(3):
        if (matrix[x][0] + matrix[x][1] + matrix[x][2] is 200) or (matrix[0][x] + matrix[1][x] + matrix[2][x] is 200):
            return True
    return False
def get_win(matrix):
    if matrix[0][0] + matrix[1][1] + matrix[2][2] is 200:
        if not matrix[0][0]:
            matrix[0][0] = 100
        elif not matrix[1][1]:
            matrix[1][1] = 100
        else:
            matrix[2][2] = 100
    elif matrix[0][2] + matrix[1][1] + matrix[2][0] is 200:
        if not matrix[0][2]:
            matrix[0][2] = 100
        elif not matrix[1][1]:
            matrix[1][1] = 100
        else:
            matrix[2][0] = 100
    else:
        for x in range(3):
            if matrix[x][0] + matrix[x][1] + matrix[x][2] is 200:
                if not matrix[x][0]:
                    matrix[x][0] = 100
                elif not matrix[x][1]:
                    matrix[x][1] = 100
                else:
                    matrix[x][2] = 100
                break
            elif matrix[0][x] + matrix[1][x] + matrix[2][x] is 200:
                if not matrix[0][x]:
                    matrix[0][x] = 100
                elif not matrix[1][x]:
                    matrix[1][x] = 100
                else:
                    matrix[2][x] = 100
                break
def defend(matrix):
    if (matrix[0][0] + matrix[1][1] + matrix[2][2] is 2) or (matrix[0][2] + matrix[1][1] + matrix[2][0] is 2):
        return True
    for x in range(3):
        if (matrix[x][0] + matrix[x][1] + matrix[x][2] is 2) or (matrix[0][x] + matrix[1][x] + matrix[2][x] is 2):
            return True
    return False
def get_defense(matrix):
    if matrix[0][0] + matrix[1][1] + matrix[2][2] is 2:
        if not matrix[0][0]:
            matrix[0][0] = 100
        elif not matrix[1][1]:
            matrix[1][1] = 100
        else:
            matrix[2][2] = 100
    elif matrix[0][2] + matrix[1][1] + matrix[2][0] is 2:
        if not matrix[0][2]:
            matrix[0][2] = 100
        elif not matrix[1][1]:
            matrix[1][1] = 100
        else:
            matrix[2][0] = 100
    else:
        for x in range(3):
            if matrix[x][0] + matrix[x][1] + matrix[x][2] is 2:
                if not matrix[x][0]:
                    matrix[x][0] = 100
                elif not matrix[x][1]:
                    matrix[x][1] = 100
                else:
                    matrix[x][2] = 100
                break
            elif matrix[0][x] + matrix[1][x] + matrix[2][x] is 2:
                if not matrix[0][x]:
                    matrix[0][x] = 100
                elif not matrix[1][x]:
                    matrix[1][x] = 100
                else:
                    matrix[2][x] = 100
                break
def move(matrix):
    for x in range(3):
        if (matrix[x][0] + matrix[x][1] + matrix[x][2] is 100) or (matrix[0][x] + matrix[1][x] + matrix[2][x] is 100):
            return True
    return False
def get_move(matrix):
    if matrix[2][2] is 1 and matrix[1][1] is 100 and matrix[1][0] is 1 and not matrix[0][0]:
        matrix[0][0] = 100
    elif matrix[2][0] is 1 and matrix[1][1] is 100 and matrix[1][2] is 1 and not matrix[0][2]:
        matrix[0][2] = 100
    elif matrix[0][0] is 1 and matrix[1][1] is 100 and matrix[1][2] is 1 and not matrix[2][2]:
        matrix[2][2] = 100
    elif matrix[0][2] is 1 and matrix[1][1] is 100 and matrix[1][0] is 1 and not matrix[2][0]:
        matrix[2][0] = 100
    elif (matrix[1][1] + matrix[2][2] is 2) and (not matrix[2][0]):
        matrix[2][0] = 100
    elif (matrix[1][1] + matrix[0][0] is 2) and (not matrix[0][2]):
        matrix[0][2] = 100
    elif (matrix[1][1] + matrix[0][2] is 2) and (not matrix[0][0]):
        matrix[0][0] = 100
    elif (matrix[1][1] + matrix[2][0] is 2) and (not matrix[2][2]):
        matrix[2][2] = 100
    elif (matrix[0][0] + matrix[1][1] + matrix[2][2] is 102) and (not matrix[1][0]):
        matrix[1][0] = 100
    elif (matrix[0][2] + matrix[1][1] + matrix[2][0] is 102) and (not matrix[1][2]):
        matrix[1][2] = 100
    elif matrix[0][0] + matrix[1][1] + matrix[2][2] is 100:
        if not matrix[0][0]:
            matrix[0][0] = 100
        else:
            matrix[2][2] = 100
    elif matrix[0][2] + matrix[1][1] + matrix[2][0] is 100:
        if not matrix[0][2]:
            matrix[0][2] = 100
        else:
            matrix[2][0] = 100
    elif move(matrix):
        for x in range(3):
            if matrix[x][0] + matrix[x][1] + matrix[x][2] is 100:
                if not matrix[x][0]:
                    matrix[x][0] = 100
                else:
                    matrix[x][2] = 100
                break
            elif matrix[0][x] + matrix[1][x] + matrix[2][x] is 100:
                if not matrix[0][x]:
                    matrix[0][x] = 100
                else:
                    matrix[2][x] = 100
                break
    else:
        ok = 0
        for x in range(3):
            for y in range(3):
                if not matrix[x][y]:
                    matrix[x][y] = 100
                    ok = 1
                    break
            if ok:
                break
def function():
    stats_display()
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    print('Select who to start the game:\n1)%s%s%s\n2)%sComputer%s\n3)%sRan%sdom%s' % (red, name, white, blue, white, red, blue, white))
    turn = int(input('Your answer: '))
    while turn is not 1 and turn is not 2 and turn is not 3:
        turn = int(input('\n%sInexistent option%s%s!\nTry again: ' % (und, eund, white)))
    if turn is 3:
        turn = random.randint(1, 2)
    exit = 0
    os.system('CLS')
    if turn is 1:
        type(matrix)
        print("*%s%s's turn%s*" % (red, name, white))
        l = int(input('-line: \x1b[1;31;40m'))
        print('%s' % white, end = "")
        while l < 1 or l > 3:
            print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
            l = int(input('\x1b[1;31;40m'))
            print('%s' % white, end = "")
        l -= 1
        c = int(input('-column: \x1b[1;31;40m'))
        print('%s' % white, end = "")
        while c < 1 or c > 3:
            print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
            c = int(input('\x1b[1;31;40m'))
            print('%s' % white, end = "")
        c -= 1
        matrix[l][c] = 1
        if l is 1 and c is 1:
            num = random.randint(1,4)
            if num is 1:
                matrix[0][0] = 100
            elif num is 2:
                matrix[0][2] = 100
            elif num is 3:
                matrix[2][0] = 100
            else:
                matrix[2][2] = 100
        else:
            matrix[1][1] = 100
        print()
        while not end_game(matrix):
            if turn % 2:
                os.system('CLS')
                type(matrix)
                print("*%s%s's turn%s*" % (red, name, white))
                l = int(input('-line: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
                while matrix[l][c] != 0:
                    print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                    while l < 1 or l > 3:
                        print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                        l = int(input('\x1b[1;31;40m'))
                        print('%s' % white, end = "")
                    l -= 1
                    c = int(input('-column: \x1b[1;31;40m'))
                    print('%s' % white, end = "")
                    while c < 1 or c > 3:
                        print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                        c = int(input('\x1b[1;31;40m'))
                        print('%s' % white, end = "")
                    c -= 1
                matrix[l][c] = 1
            else:
                if win(matrix):
                    sts[0] += 1
                    sts[3] += 1
                    with open('stats.txt', 'wb') as file:
                        pickle.dump(sts, file)
                    get_win(matrix)
                    os.system('CLS')
                    type(matrix)
                    computer()
                    exit = 1
                    stats_display()
                    print('\n%s%sPress%s%s:\n1)For a new round\n2)For the end of the game' % (white, und, eund, white))
                    ans = int(input('Enter your answer here: '))
                    while ans != 1 and ans != 2:
                        print('\n%sInvalid answer%s%s!' % (und, eund, white))
                        ans = int(input('Try again: '))
                    if ans is 1:
                        os.system('CLS')
                        function()
                elif defend(matrix):
                    get_defense(matrix)
                else:
                    get_move(matrix)
                print('%s' % white, end = "")
            turn += 1
            if exit:
                break
        if not exit:
            sts[0] += 1
            sts[2] += 1
            with open('stats.txt', 'wb') as file:
                pickle.dump(sts, file)
            os.system('CLS')
            type(matrix)
            print('TIE!')
            stats_display()
            print('\n%s%sPress%s%s:\n1)For a new round\n2)For the end of the game' % (white, und, eund, white))
            ans = int(input('Enter your answer here: '))
            while ans != 1 and ans != 2:
                print('\n%sInvalid answer%s%s!' % (und, eund, white))
                ans = int(input('Try again: '))
            if ans is 1:
                os.system('CLS')
                function()
    else:
        matrix[2][0] = 100
        type(matrix)
        print("*%s%s's turn%s*" % (red, name, white))
        l = int(input('-line: \x1b[1;31;40m'))
        print('%s' % white, end = "")
        while l < 1 or l > 3:
            print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
            l = int(input('\x1b[1;31;40m'))
            print('%s' % white, end = "")
        l -= 1
        c = int(input('-column: \x1b[1;31;40m'))
        print('%s' % white, end = "")
        while c < 1 or c > 3:
            print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
            c = int(input('\x1b[1;31;40m'))
            print('%s' % white, end = "")
        c -= 1
        while matrix[l][c] != 0:
            print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
            l = int(input('\x1b[1;31;40m'))
            print('%s' % white, end = "")
            while l < 1 or l > 3:
                print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            l -= 1
            c = int(input('-column: '))
            print('%s' % white, end = "")
            while c < 1 or c > 3:
                print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                c = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            c -= 1
        matrix[l][c] = 1
        os.system('CLS')
        if l is 2 and c is 1:
            matrix[1][0] = 100
            type(matrix)
            print("*%s%s's turn%s*" % (red, name, white))
            l = int(input('-line: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while l < 1 or l > 3:
                print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            l -= 1
            c = int(input('-column: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while c < 1 or c > 3:
                print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                c = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            c -= 1
            while matrix[l][c] != 0:
                print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
            matrix[l][c] = 1
            if l is 0 and c is 0:
                matrix[1][1] = 100
                turn = 1
        elif l is 1 and c is 0:
            matrix[2][1] = 100
            os.system('CLS')
            type(matrix)
            print("*%s%s's turn%s*" % (red, name, white))
            l = int(input('-line: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while l < 1 or l > 3:
                print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            l -= 1
            c = int(input('-column: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while c < 1 or c > 3:
                print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                c = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            c -= 1
            while matrix[l][c] != 0:
                print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
            matrix[l][c] = 1
            if l is 2 and c is 2:
                matrix[1][1] = 100
                turn = 1
        elif l is 0 and c is 1:
            matrix[0][0] = 100
            os.system('CLS')
            type(matrix)
            print("*%s%s's turn%s*" % (red, name, white))
            l = int(input('-line: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while l < 1 or l > 3:
                print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            l -= 1
            c = int(input('-column: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while c < 1 or c > 3:
                print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                c = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            c -= 1
            while matrix[l][c] != 0:
                print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
            matrix[l][c] = 1
            if l is 2 and c is 1:
                matrix[1][1] = 100
                turn = 1
        elif l is 1 and c is 2:
            matrix[2][2] = 100
            os.system('CLS')
            type(matrix)
            print("*%s%s's turn%s*" % (red, name, white))
            l = int(input('-line: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while l < 1 or l > 3:
                print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            l -= 1
            c = int(input('-column: \x1b[1;31;40m'))
            print('%s' % white, end = "")
            while c < 1 or c > 3:
                print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                c = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
            c -= 1
            while matrix[l][c] != 0:
                print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                l = int(input('\x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
            matrix[l][c] = 1
            if l is 1 and c is 0:
                matrix[1][1] = 100
                turn = 1
        while not end_game(matrix):
            if turn % 2:
                os.system('CLS')
                type(matrix)
                print("*%s%s's turn%s*" % (red, name, white))
                l = int(input('-line: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while l < 1 or l > 3:
                    print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                l -= 1
                c = int(input('-column: \x1b[1;31;40m'))
                print('%s' % white, end = "")
                while c < 1 or c > 3:
                    print('%sColumn index out of range%s%s!\n-column: ' % (und, eund, white), end = "")
                    c = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                c -= 1
                while matrix[l][c] != 0:
                    print('%sPosition already taken%s%s!\n-line: ' % (und, eund, white), end = "")
                    l = int(input('\x1b[1;31;40m'))
                    print('%s' % white, end = "")
                    while l < 1 or l > 3:
                        print('%sLine index out of range%s%s!\n-line: ' % (und, eund, white), end = "")
                        l = int(input('\x1b[1;31;40m'))
                        print('%s' % white, end = "")
                    l -= 1
                    c = int(input('-column: \x1b[1;31;40m'))
                    print('%s' % white, end = "")
                    while c < 1 or c > 3:
                        print('%sColumn index out of range%s%s!\n-column: ', end = "")
                        c = int(input('\x1b[1;31;40m'))
                        print('%s' % white, end = "")
                    c -= 1
                matrix[l][c] = 1
            else:
                if win(matrix):
                    sts[0] += 1
                    sts[3] += 1
                    with open('stats.txt', 'wb') as file:
                        pickle.dump(sts, file)
                    get_win(matrix)
                    os.system('CLS')
                    type(matrix)
                    computer()
                    exit = 1
                    stats_display()
                    print('\n%s%sPress%s%s:\n1)For a new round\n2)For the end of the game' % (white, und, eund, white))
                    ans = int(input('Enter your answer here: '))
                    while ans != 1 and ans != 2:
                        print('\n%sInvalid answer%s%s!' % (und, eund, white))
                        ans = int(input('Try again: '))
                    if ans is 1:
                        os.system('CLS')
                        function()
                elif defend(matrix):
                    get_defense(matrix)
                else:
                    get_move(matrix)
                print('%s' % white, end = "")
            turn += 1
            if exit:
                break
        if not exit:
            sts[0] += 1
            sts[2] += 1
            with open('stats.txt', 'wb') as file:
                pickle.dump(sts, file)
            os.system('CLS')
            type(matrix)
            print('TIE!')
            stats_display()
            print('\n%s%sPress%s%s:\n1)For a new round\n2)For the end of the game' % (white, und, eund, white))
            ans = int(input('Enter your answer here: '))
            while ans != 1 and ans != 2:
                print('\n%sInvalid answer%s%s!' % (und, eund, white))
                ans = int(input('Try again: '))
            if ans is 1:
                os.system('CLS')
                function()
try:
    with open('stats.txt', 'rb') as file:
        sts = pickle.load(file)
except:
    sts = [0, 0, 0, 0]
print('%s' % white, end = "")
name = input('Enter your name here: \x1b[1;31;40m')
print('\n%sRules:%s\n%s = X%s\n%s = 0%s' % (white, red, name, blue, 'Computer', white), end = "\n\n")
function()
