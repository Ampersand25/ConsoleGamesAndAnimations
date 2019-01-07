#100 is a game for two players in which each player picks a number from 1 to 10 in turns
#the number picked by each player is added to a sum (the same for each player)
#the winner is the one who equals the sum with 100
#if the sum exceeds 100, the player who chosed the last number lost
import random, os
def game_over(sum):
    return sum >= 100
def nr_cif(num, cif):
    if not num:
        return cif
    return nr_cif(num // 10, cif + 1)
def func(cont, sc1, sc2):
    print('\x1b[1;37;40m', end = "")
    print('+' * 17, end = "")
    for i in range(nr_cif(cont, 0)):
        print('+', end = "")
    print('\n+ Round number %d +\n' % cont, end = "")
    print('+' * 17, end = "")
    for i in range(nr_cif(cont, 0)):
        print('+', end = "\n")
    print('\nGeneral score:\n\x1b[1;35;40m%s %d\x1b[1;37;40m - \x1b[1;36;40m%d %s\x1b[1;37;40m' % (p1, sc1, sc2, p2))
    sum = 0
    print('\nChoose who to start the game:\n1)\x1b[1;35;40m%s\x1b[1;37;40m\n2)\x1b[1;36;40m%s\x1b[1;37;40m\n3)\x1b[1;35;40mRan\x1b[1;36;40mdom\x1b[1;37;40m' % (p1, p2))
    ans = int(input('Answer: '))
    while ans != 1 and ans != 2 and ans != 3:
        ans = int(input('Invalid answer typed. Retype: '))
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
            print('\x1b[1;35;40m', end = "")
            print(p1 + "\x1b[1;37;40m's turn")
        else:
            print('\x1b[1;36;40m', end = "")
            print(p2 + "\x1b[1;37;40m's turn")
        num = int(input('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m: \x1b[1;34;40m'))
        print('\x1b[1;37;40m', end = "")
        while num < 1 or num > 10:
            num = int(input('Invalid number. Try again: \x1b[1;34;40m'))
            print('\x1b[1;37;40m', end = "")
        sum += num
        turn += 1
    print('\nSum = \x1b[1;31;40m%d' % sum)
    if sum is 100:
        if turn % 2:
            sc2 += 1
            print('\x1b[1;36;40m', end = "")
            print(p2 + ' \x1b[1;33;40mwinner!\x1b[1;37;40m')
        else:
            sc1 += 1
            print('\x1b[1;35;40m', end = "")
            print(p1 + ' \x1b[1;33;40mwinner!\x1b[1;37;40m')
    else:
        if turn % 2:
            sc1 += 1
            print('\x1b[1;35;40m', end = "")
            print(p1 + ' \x1b[1;33;40mwinner!\x1b[1;37;40m')
        else:
            sc2 += 1
            print('\x1b[1;36;40m', end = "")
            print(p2 + ' \x1b[1;33;40mwinner!\x1b[1;37;40m')
    print('\nGeneral score:\n\x1b[1;35;40m%s %d\x1b[1;37;40m - \x1b[1;36;40m%d %s\x1b[1;37;40m' % (p1, sc1, sc2, p2))
    print('\x1b[1;37;40m\nPress:\n1)For a new round\n2)For the end of the game (or simply close the console)')
    ans = int(input('Enter your answer here: '))
    while ans is not 1 and ans is not 2:
        ans = int(input('Inexistent optin. Try again: '))
    if ans is 1:
        os.system('CLS')
        func(cont + 1, sc1, sc2)
sum, cont, sc1, sc2 = 0, 1, 0, 0
p1 = input('\x1b[1;37;40mPlayer 1: \x1b[1;35;40m')
print('\x1b[1;37;40m', end = "")
p2 = input('Player 2: \x1b[1;36;40m')
print('\x1b[1;37;40m', end = "")
os.system('CLS')
func(cont, sc1, sc2)
