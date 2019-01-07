import random, os
rond, white, red = 1, '\033[1;37;40m', '\033[1;31;40m'
def function(rond):
    n = random.randint(1, 100)
    print('%sRound %d)\nThink about a number from %s1%s to %s100%s and write it: \033[1;31;40m' % (white, rond, red, white, red, white), end = "")
    k = int(input())
    print('%s' % white, end = "")
    nr = 0
    while k < 1 or k > 100:
        if nr is 3:
            print('You entered wrong numbers too many times!')
            return 0
        nr += 1
        print('The number entered is not in the range of %s[1,100]%s!\nRe-enter another number: %s' % (red, white, red), end = "")
        k = int(input())
        print('%s' % white, end = "")
    count = 0
    while k is not n:
        print()
        if k > n:
            print('Too much!')
        else:
            print('Too little!')
        print('Try again: %s' % red, end = "")
        k = int(input())
        print('%s' % white, end = "")
        nr = 0
        while k < 1 or k > 100:
            if nr is 3:
                print('You entered wrong numbers too many times!')
                return 0
            nr += 1
            print('The number entered is not in the range of %s[1,100]%s!\nRe-enter another number: %s' % (red, white, red), end = "")
            k = int(input())
            print('%s' % white, end = "")
        count += 1
    print('\nCongratulations! You guessed the number %s%d%s of %s%d%s attempts!' % (red, n, white, red, count + 1, white))
    print('\nPress:\n1)for a new round\n2)for the end of the game\nAnswer: ', end = "")
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
