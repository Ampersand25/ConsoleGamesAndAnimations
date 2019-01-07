import random, os
str = 'abcdefghijklmnopqrstuvwxyz'
rond, white, blue = 1, '\033[1;37;40m', '\033[1;34;40m'
def function(rond):
    nr = random.randint(0, len(str) - 1)
    print('%sRound %d)\nThink about a letter from %sa%s to %sz%s and write it: %s' % (white, rond, blue, white, blue, white, blue), end = "")
    le = input()
    le = le.lower()
    print('%s' % white, end = "")
    tr = 0
    while str.count(le) is 0:
        if tr is 3:
            print('You entered wrong symbols too many times!')
            return 0
        tr += 1
        print("The symbol you entered is not a letter from '%sa%s' to '%sz%s'!\nRe-enter another one: %s" % (blue, white, blue, white, blue), end = "")
        le = input()
        print('%s' % white, end = "")
    count = 0
    while le != str[nr]:
        print()
        if str.index(le) > str.index(str[nr]):
            print('Too right!')
        else:
            print('Too left!')
        print('Try again: %s' % blue, end = "")
        le = input()
        print('%s' % white, end = "")
        tr = 0
        while str.count(le) is 0:
            if tr is 3:
                print('You entered wrong symbols too many times!')
                return 0
            tr += 1
            print("The symbol you entered is not a letter from '%sa%s' to '%sz%s'!\nRe-enter another one: %s" % (blue, white, blue, white, blue), end = "")
            le = input()
            print('%s' % white, end = "")
        count += 1
    print('\nCongratulations! You guessed the letter %s%s%s of %s%d%s attempts!' % (blue, str[nr], white, blue, count + 1, white))
    print('\nPress\n1)for a new round\n2)for the end of the game\nAnswer: ', end = "")
    op = int(input())
    while op != 1 and op != 2:
        print('\nOption unavailable!\nRe-enter one of the options above: ', end = "")
        op = int(input())
    if op is 1:
        os.system('CLS')
        function(rond + 1)
    else:
        return 0
function(rond)
