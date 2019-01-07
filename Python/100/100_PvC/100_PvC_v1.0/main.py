#100 is a game for two players in which each player picks a number from 1 to 10 in turns
#the number picked by each player is added to a sum (the same for each player)
#the winner is the one who equals the sum with 100
#if the sum exceeds 100, the player who chosed the last number lost
import random, os
game_nr = 1
def game_over(nr):
    return nr >= 100
def casual():
    sum = 0
    print('\nDifficulty: Casual\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    while not game_over(sum):
        print('\nSum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        if turn % 2:
            print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
            num = int(input('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m: \x1b[1;34;40m'))
            print('\x1b[1;37;40m', end = "")
            while num < 1 or num > 10:
                num = int(input('Invalid number. Try again: \x1b[1;34;40m'))
                print('\x1b[1;37;40m', end = "")
        else:
            if sum >= 90:
                num = 100 - sum
            else:
                num = random.randint(1, 10)
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m" % num)
        sum += num
        turn += 1
    print('\nSum = \x1b[1;31;40m%d' % sum)
    if sum is 100:
        if turn % 2:
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
        else:
            print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
    else:
        print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
def intermediate():
    sum = 0
    print('\nDifficulty: Intermediate\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    while not game_over(sum):
        print('\nSum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        if turn % 2:
            print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
            num = int(input('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m: \x1b[1;34;40m'))
            print('\x1b[1;37;40m', end = "")
            while num < 1 or num > 10:
                num = int(input('Invalid number. Try again: \x1b[1;34;40m'))
                print('\x1b[1;37;40m', end = "")
        else:
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn")
            if sum >= 79 and sum <= 88:
                num = 89 - sum
            elif sum >= 90:
                num = 100 - sum
            else:
                num = random.randint(1, 10)
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m" % num)
        sum += num
        turn += 1
    print('\nSum = \x1b[1;31;40m%d' % sum)
    if sum is 100:
        if turn % 2:
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
        else:
            print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
    else:
        print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
def on_track(arr, nr):
    for x in range(10):
        if arr[x] > nr:
            return arr[x]
def hardcore():
    sum = 0
    print('\nDifficulty: Hardcore\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    if turn is 2:
        print('\nSum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m" % 1)
        sum, turn, last = 1, 3, 0
        while not game_over(sum):
            print('\nSum = \x1b[1;31;40m%d' % sum)
            print('\x1b[1;37;40m', end = "")
            if turn % 2:
                num = int(input('\x1b[1;32;40mYour\x1b[1;37;40m turn\nChoose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m: \x1b[1;34;40m'))
                print('\x1b[1;37;40m', end = "")
                while num < 1 or num > 10:
                    num = int(input('Invalid number. Try again: \x1b[1;34;40m'))
                    print('\x1b[1;37;40m', end = "")
                last = num
            else:
                num = 11 - last
                print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m" % num)
            sum += num
            turn += 1
        print('\nSum = \x1b[1;31;40m%d' % sum)
        if sum >= 100:
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
    else:
        #Arithmetic progression with a(1) = 1, a(n) = 100 and r = 11
        arr = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
        while not game_over(sum):
            print('\nSum = \x1b[1;31;40m%d' % sum)
            print('\x1b[1;37;40m', end = "")
            if turn % 2:
                num = int(input('\x1b[1;32;40mYour\x1b[1;37;40m turn\nChoose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m: \x1b[1;34;40m'))
                print('\x1b[1;37;40m', end = "")
                while num < 1 or num > 10:
                    num = int(input('Invalid number. Try again: \x1b[1;34;40m'))
                    print('\x1b[1;37;40m', end = "")
            else:
                if on_track(arr, sum) - sum <= 10:
                    num = on_track(arr, sum) - sum
                else:
                    num = random.randint(1, 10)
                print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m" % num)
            sum += num
            turn += 1
        print('\nSum = \x1b[1;31;40m%d' % sum)
        if sum is 100:
            if turn % 2:
                print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
            else:
                print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
        else:
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
def nr_cif(num):
    cate = 0
    while num != 0:
        cate += 1
        num //= 10
    return cate
def main(game_nr):
    print('\x1b[1;37;40m', end = "")
    print('-' * 14, end = "")
    for i in range(nr_cif(game_nr)):
        print('-', end = "")
    print('\n|Game number %d|' % game_nr)
    print('-' * 14, end = "")
    for i in range(nr_cif(game_nr)):
        print('-', end = "")
    print('\n\nSelect the level of difficulty:\n1)Casual\n2)Intermediate\n3)Hardcore\n4)Random')
    dif = int(input('Your option is: '))
    while dif < 1 or dif > 4:
        dif = int(input('Invalid answer. Retype your option: '))
    if dif is 4:
        dif = random.randint(1,3)
    if dif is 1:
        casual()
    elif dif is 2:
        intermediate()
    else:
        hardcore()
    print('\x1b[1;37;40m\nPress:\n1)For a new game\n2)For the end of the game (or simply close the console)')
    ans = int(input('Enter your answer here: '))
    while ans is not 1 and ans is not 2:
        ans = int(input('Inexistent optin. Try again: '))
    if ans is 1:
        os.system('CLS')
        main(game_nr + 1)
main(game_nr)
