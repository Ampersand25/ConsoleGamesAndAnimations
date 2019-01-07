#100 is a game for two players in which each player picks a number from 1 to 10 in turns
#the number picked by each player is added to a sum (the same for each player)
#the winner is the one who equals the sum with 100
#if the sum exceeds 100, the player who chosed the last number lost
import pygame, sys, os, random, time, pickle
from pygame.locals import *
game_nr = 1
def game_over(nr):
    return nr >= 100
def stats_display():
    f = open('stats.txt','w')
    f.write(' Casual\n-matches: %d\n-wins: %d\n-defeats: %d' % (casual_stats[0], casual_stats[1], casual_stats[2]))
    f.write('\n\n Intermediate\n-matches: %d\n-wins: %d\n-defeats: %d' % (intermediate_stats[0], intermediate_stats[1], intermediate_stats[2]))
    f.write('\n\n Hardcore\n-matches: %d\n-wins: %d\n-defeats: %d' % (hardcore_stats[0], hardcore_stats[1], hardcore_stats[2]))
    f.close()
def casual():
    casual_stats[0] += 1
    sum = 0
    print('Difficulty: Casual\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    os.system('CLS')
    pygame.init()
    Window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame Console")
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Gray = (128, 128, 128)
    Lime = (0, 255, 0)
    Blue = (0, 0, 255)
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('WELCOME TO 100!', True, Lime, Black)
    textRect = text.get_rect()
    textRect.centerx = Window.get_rect().centerx
    textRect.centery = Window.get_rect().centery
    Window.blit(text, textRect)
    pygame.display.update()
    Window.fill(Black)
    while not game_over(sum):
        print('Sum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        if turn % 2:
            print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
            print('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m\x1b[1;34;40m')
            print('\x1b[1;37;40m', end = "")
            okok = False
            while okok == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Window.fill(Black)
                        text = basicFont.render('QUITTING...', True, Gray, Black)
                        textRect = text.get_rect()
                        textRect.centerx = Window.get_rect().centerx
                        textRect.centery = Window.get_rect().centery
                        Window.blit(text, textRect)
                        pygame.display.update()
                        time.sleep(1.5)
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        okok = True
                        if event.key == pygame.K_1:
                            num = 1
                            text = basicFont.render('YOU PRESSED 1', True, Blue, Black)
                        elif event.key == pygame.K_2:
                            num = 2
                            text = basicFont.render('YOU PRESSED 2', True, Blue, Black)
                        elif event.key == pygame.K_3:
                            num = 3
                            text = basicFont.render('YOU PRESSED 3', True, Blue, Black)
                        elif event.key == pygame.K_4:
                            num = 4
                            text = basicFont.render('YOU PRESSED 4', True, Blue, Black)
                        elif event.key == pygame.K_5:
                            num = 5
                            text = basicFont.render('YOU PRESSED 5', True, Blue, Black)
                        elif event.key == pygame.K_6:
                            num = 6
                            text = basicFont.render('YOU PRESSED 6', True, Blue, Black)
                        elif event.key == pygame.K_7:
                            num = 7
                            text = basicFont.render('YOU PRESSED 7', True, Blue, Black)
                        elif event.key == pygame.K_8:
                            num = 8
                            text = basicFont.render('YOU PRESSED 8', True, Blue, Black)
                        elif event.key == pygame.K_9:
                            num = 9
                            text = basicFont.render('YOU PRESSED 9', True, Blue, Black)
                        elif event.key == pygame.K_0:
                            num = 10
                            text = basicFont.render('YOU PRESSED 10', True, Blue, Black)
                        elif event.key == pygame.K_ESCAPE:
                            Window.fill(Black)
                            text = basicFont.render('QUITTING...', True, Gray, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            time.sleep(1.5)
                            pygame.quit()
                            sys.exit()
                        else:
                            okok = False
                            text = basicFont.render('INVALID COMMAND', True, Red, Black)
                        textRect = text.get_rect()
                        textRect.centerx = Window.get_rect().centerx
                        textRect.centery = Window.get_rect().centery
                        Window.blit(text, textRect)
                        pygame.display.update()
                        Window.fill(Black)
            os.system('CLS')
        else:
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn")
            if sum >= 90:
                num = 100 - sum
            else:
                num = random.randint(1, 10)
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m\n" % num)
        sum += num
        turn += 1
    pygame.quit()
    print('Sum = \x1b[1;31;40m%d' % sum)
    if sum is 100:
        if turn % 2:
            casual_stats[2] += 1
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
        else:
            casual_stats[1] += 1
            print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
    else:
        casual_stats[2] += 1
        print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
    with open('casual.txt', 'wb') as file:
        pickle.dump(casual_stats, file)
def intermediate():
    intermediate_stats[0] += 1
    sum = 0
    print('Difficulty: Intermediate\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    os.system('CLS')
    pygame.init()
    Window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame Console")
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Gray = (128, 128, 128)
    Lime = (0, 255, 0)
    Blue = (0, 0, 255)
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('WELCOME TO 100!', True, Lime, Black)
    textRect = text.get_rect()
    textRect.centerx = Window.get_rect().centerx
    textRect.centery = Window.get_rect().centery
    Window.blit(text, textRect)
    pygame.display.update()
    Window.fill(Black)
    while not game_over(sum):
        print('Sum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        if turn % 2:
            print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
            print('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m\x1b[1;34;40m')
            print('\x1b[1;37;40m', end = "")
            okok = False
            while okok == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Window.fill(Black)
                        text = basicFont.render('QUITTING...', True, Gray, Black)
                        textRect = text.get_rect()
                        textRect.centerx = Window.get_rect().centerx
                        textRect.centery = Window.get_rect().centery
                        Window.blit(text, textRect)
                        pygame.display.update()
                        time.sleep(1.5)
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        okok = True
                        if event.key == pygame.K_1:
                            num = 1
                            text = basicFont.render('YOU PRESSED 1', True, Blue, Black)
                        elif event.key == pygame.K_2:
                            num = 2
                            text = basicFont.render('YOU PRESSED 2', True, Blue, Black)
                        elif event.key == pygame.K_3:
                            num = 3
                            text = basicFont.render('YOU PRESSED 3', True, Blue, Black)
                        elif event.key == pygame.K_4:
                            num = 4
                            text = basicFont.render('YOU PRESSED 4', True, Blue, Black)
                        elif event.key == pygame.K_5:
                            num = 5
                            text = basicFont.render('YOU PRESSED 5', True, Blue, Black)
                        elif event.key == pygame.K_6:
                            num = 6
                            text = basicFont.render('YOU PRESSED 6', True, Blue, Black)
                        elif event.key == pygame.K_7:
                            num = 7
                            text = basicFont.render('YOU PRESSED 7', True, Blue, Black)
                        elif event.key == pygame.K_8:
                            num = 8
                            text = basicFont.render('YOU PRESSED 8', True, Blue, Black)
                        elif event.key == pygame.K_9:
                            num = 9
                            text = basicFont.render('YOU PRESSED 9', True, Blue, Black)
                        elif event.key == pygame.K_0:
                            num = 10
                            text = basicFont.render('YOU PRESSED 10', True, Blue, Black)
                        elif event.key == pygame.K_ESCAPE:
                            Window.fill(Black)
                            text = basicFont.render('QUITTING...', True, Gray, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            time.sleep(1.5)
                            pygame.quit()
                            sys.exit()
                        else:
                            okok = False
                            text = basicFont.render('INVALID COMMAND', True, Red, Black)
                        textRect = text.get_rect()
                        textRect.centerx = Window.get_rect().centerx
                        textRect.centery = Window.get_rect().centery
                        Window.blit(text, textRect)
                        pygame.display.update()
                        Window.fill(Black)
            os.system('CLS')
        else:
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn")
            if sum >= 79 and sum <= 88:
                num = 89 - sum
            elif sum >= 90:
                num = 100 - sum
            else:
                num = random.randint(1, 10)
            print("\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m\n" % num)
        sum += num
        turn += 1
    pygame.quit()
    print('Sum = \x1b[1;31;40m%d' % sum)
    if sum is 100:
        if turn % 2:
            intermediate_stats[2] += 1
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
        else:
            intermediate_stats[1] += 1
            print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
    else:
        intermediate_stats[2] += 1
        print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
    with open('intermediate.txt', 'wb') as file:
        pickle.dump(intermediate_stats, file)
def on_track(arr, nr):
    for x in range(10):
        if arr[x] > nr:
            return arr[x]
def hardcore():
    hardcore_stats[0] += 1
    sum = 0
    print('Difficulty: Hardcore\nChoose who to start the game:\n1)\x1b[1;32;40mYou\x1b[1;37;40m\n2)\x1b[1;33;40mThe computer\x1b[1;37;40m\n3)\x1b[1;32;40mRan\x1b[1;33;40mdom\x1b[1;37;40m')
    ans = int(input('Answer: '))
    while ans < 1 or ans > 3:
        ans = int(input('Invalid option. Try again: '))
    if ans is 1:
        turn = 1
    elif ans is 2:
        turn = 2
    else:
        turn = random.randint(1, 2)
    os.system('CLS')
    pygame.init()
    Window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame Console")
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Gray = (128, 128, 128)
    Lime = (0, 255, 0)
    Blue = (0, 0, 255)
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('WELCOME TO 100!', True, Lime, Black)
    textRect = text.get_rect()
    textRect.centerx = Window.get_rect().centerx
    textRect.centery = Window.get_rect().centery
    Window.blit(text, textRect)
    pygame.display.update()
    Window.fill(Black)
    if turn is 2:
        print('Sum = \x1b[1;31;40m%d' % sum)
        print('\x1b[1;37;40m', end = "")
        print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m\n" % 1)
        sum, turn, last = 1, 3, 0
        while not game_over(sum):
            print('Sum = \x1b[1;31;40m%d' % sum)
            print('\x1b[1;37;40m', end = "")
            if turn % 2:
                print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
                print('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m\x1b[1;34;40m')
                print('\x1b[1;37;40m', end = "")
                okok = False
                while okok == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Window.fill(Black)
                            text = basicFont.render('QUITTING...', True, Gray, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            time.sleep(1.5)
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            okok = True
                            if event.key == pygame.K_1:
                                num = 1
                                text = basicFont.render('YOU PRESSED 1', True, Blue, Black)
                            elif event.key == pygame.K_2:
                                num = 2
                                text = basicFont.render('YOU PRESSED 2', True, Blue, Black)
                            elif event.key == pygame.K_3:
                                num = 3
                                text = basicFont.render('YOU PRESSED 3', True, Blue, Black)
                            elif event.key == pygame.K_4:
                                num = 4
                                text = basicFont.render('YOU PRESSED 4', True, Blue, Black)
                            elif event.key == pygame.K_5:
                                num = 5
                                text = basicFont.render('YOU PRESSED 5', True, Blue, Black)
                            elif event.key == pygame.K_6:
                                num = 6
                                text = basicFont.render('YOU PRESSED 6', True, Blue, Black)
                            elif event.key == pygame.K_7:
                                num = 7
                                text = basicFont.render('YOU PRESSED 7', True, Blue, Black)
                            elif event.key == pygame.K_8:
                                num = 8
                                text = basicFont.render('YOU PRESSED 8', True, Blue, Black)
                            elif event.key == pygame.K_9:
                                num = 9
                                text = basicFont.render('YOU PRESSED 9', True, Blue, Black)
                            elif event.key == pygame.K_0:
                                num = 10
                                text = basicFont.render('YOU PRESSED 10', True, Blue, Black)
                            elif event.key == pygame.K_ESCAPE:
                                Window.fill(Black)
                                text = basicFont.render('QUITTING...', True, Gray, Black)
                                textRect = text.get_rect()
                                textRect.centerx = Window.get_rect().centerx
                                textRect.centery = Window.get_rect().centery
                                Window.blit(text, textRect)
                                pygame.display.update()
                                time.sleep(1.5)
                                pygame.quit()
                                sys.exit()
                            else:
                                okok = False
                                text = basicFont.render('INVALID COMMAND', True, Red, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            Window.fill(Black)
                os.system('CLS')
            else:
                num = 11 - last
                print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m\n" % num)
            sum += num
            turn += 1
        pygame.quit()
        print('Sum = \x1b[1;31;40m%d' % sum)
        if sum >= 100:
            hardcore_stats[2] += 1
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
    else:
        #Arithmetic progression with a(1) = 1, a(n) = 100 and r = 11
        arr = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
        while not game_over(sum):
            print('Sum = \x1b[1;31;40m%d' % sum)
            print('\x1b[1;37;40m', end = "")
            if turn % 2:
                print('\x1b[1;32;40mYour\x1b[1;37;40m turn')
                print('Choose a number from \x1b[1;34;40m1\x1b[1;37;40m to \x1b[1;34;40m10\x1b[1;37;40m\x1b[1;34;40m')
                print('\x1b[1;37;40m', end = "")
                okok = False
                while okok == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Window.fill(Black)
                            text = basicFont.render('QUITTING...', True, Gray, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            time.sleep(1.5)
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            okok = True
                            if event.key == pygame.K_1:
                                num = 1
                                text = basicFont.render('YOU PRESSED 1', True, Blue, Black)
                            elif event.key == pygame.K_2:
                                num = 2
                                text = basicFont.render('YOU PRESSED 2', True, Blue, Black)
                            elif event.key == pygame.K_3:
                                num = 3
                                text = basicFont.render('YOU PRESSED 3', True, Blue, Black)
                            elif event.key == pygame.K_4:
                                num = 4
                                text = basicFont.render('YOU PRESSED 4', True, Blue, Black)
                            elif event.key == pygame.K_5:
                                num = 5
                                text = basicFont.render('YOU PRESSED 5', True, Blue, Black)
                            elif event.key == pygame.K_6:
                                num = 6
                                text = basicFont.render('YOU PRESSED 6', True, Blue, Black)
                            elif event.key == pygame.K_7:
                                num = 7
                                text = basicFont.render('YOU PRESSED 7', True, Blue, Black)
                            elif event.key == pygame.K_8:
                                num = 8
                                text = basicFont.render('YOU PRESSED 8', True, Blue, Black)
                            elif event.key == pygame.K_9:
                                num = 9
                                text = basicFont.render('YOU PRESSED 9', True, Blue, Black)
                            elif event.key == pygame.K_0:
                                num = 10
                                text = basicFont.render('YOU PRESSED 10', True, Blue, Black)
                            elif event.key == pygame.K_ESCAPE:
                                Window.fill(Black)
                                text = basicFont.render('QUITTING...', True, Gray, Black)
                                textRect = text.get_rect()
                                textRect.centerx = Window.get_rect().centerx
                                textRect.centery = Window.get_rect().centery
                                Window.blit(text, textRect)
                                pygame.display.update()
                                time.sleep(1.5)
                                pygame.quit()
                                sys.exit()
                            else:
                                okok = False
                                text = basicFont.render('INVALID COMMAND', True, Red, Black)
                            textRect = text.get_rect()
                            textRect.centerx = Window.get_rect().centerx
                            textRect.centery = Window.get_rect().centery
                            Window.blit(text, textRect)
                            pygame.display.update()
                            Window.fill(Black)
                os.system('CLS')
            else:
                if on_track(arr, sum) - sum <= 10:
                    num = on_track(arr, sum) - sum
                else:
                    num = random.randint(1, 10)
                print("\x1b[1;33;40mComputer's\x1b[1;37;40m turn\n\x1b[1;33;40mComputer's\x1b[1;37;40m choice is: \x1b[1;34;40m%d\x1b[1;37;40m\n" % num)
            sum += num
            turn += 1
        pygame.quit()
        print('Sum = \x1b[1;31;40m%d' % sum)
        if sum is 100:
            if turn % 2:
                hardcore_stats[2] += 1
                print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
            else:
                hardcore_stats[1] += 1
                print('\x1b[1;32;40m!!YOU WON!!\x1b[1;37;40m')
        else:
            hardcore_stats[2] += 1
            print('\x1b[1;33;40m!!COMPUTER WON!!\x1b[1;37;40m')
    with open('hardcore.txt', 'wb') as file:
        pickle.dump(hardcore_stats, file)
def nr_cif(num):
    cate = 0
    while num != 0:
        cate += 1
        num //= 10
    return cate
def main(game_nr):
    if game_nr == 1:
        print()
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
    os.system('CLS')
    if dif is 4:
        dif = random.randint(1,3)
    if dif is 1:
        casual()
    elif dif is 2:
        intermediate()
    else:
        hardcore()
    stats_display()
    print('\x1b[1;37;40m\nPress:\n1)For a new game\n2)For the end of the game (or simply close the console)')
    ans = int(input('Enter your answer here: '))
    while ans is not 1 and ans is not 2:
        ans = int(input('Inexistent optin. Try again: '))
    if ans is 1:
        os.system('CLS')
        main(game_nr + 1)
try:
    with open('casual.txt', 'rb') as file:
        casual_stats = pickle.load(file)
except:
    casual_stats = [0, 0, 0]
try:
    with open('intermediate.txt', 'rb') as file:
        intermediate_stats = pickle.load(file)
except:
    intermediate_stats = [0, 0, 0]
try:
    with open('hardcore.txt', 'rb') as file:
        hardcore_stats = pickle.load(file)
except:
    hardcore_stats = [0, 0, 0]
main(game_nr)
