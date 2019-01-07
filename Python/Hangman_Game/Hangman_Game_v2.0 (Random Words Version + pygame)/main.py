import sys, os, pygame, random, time, pickle
from pygame.locals import *
def full(str, car):
    for i in range(len(str)):
        if car[i] == 0:
            return False
    return True
def draw(cont):
    if cont == 0:
        file = open("drawing#1.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 1:
        file = open("drawing#2.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 2:
        file = open("drawing#3.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 3:
        file = open("drawing#4.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 4:
        file = open("drawing#5.txt","r")
        for line in file:
            print(line, end = "")
    elif cont == 5:
        file = open("drawing#6.txt","r")
        for line in file:
            print(line, end = "")
    else:
        file = open("drawing#7.txt","r")
        for line in file:
            print(line, end = "")
    file.close()
def function():
    try:
        with open('used_words.txt', 'rb') as file:
            wrd = pickle.load(file)
    except:
        wrd = []
    pygame.init()
    Window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame Console")
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Red = (255, 0, 0)
    Yellow = (255, 255, 0)
    basicFont = pygame.font.SysFont(None, 48)
    os.system('CLS')
    white, red = '\x1b[1;37;40m', '\x1b[1;31;40m'
    print('%s' % white, end = "")
    strings = []
    f, g = open("results.txt","r"), open("key.log","w")
    for line in f:
        strings.append(line)
    f.close()
    ls = len(strings)
    cont = random.randint(0, ls - 1)
    str = strings[cont]
    str = str[:-1]
    if len(wrd) == ls:
        wrd = []
        with open('used_words.txt', 'wb') as file:
            pickle.dump(wrd, file)
    while wrd.count(str) != 0:
        cont = random.randint(0, ls - 1)
        for i in range(cont, ls):
            str = strings[i]
            str = str[:-1]
            if wrd.count(str) == 0:
                break
        if wrd.count(str):
            for i in range(0, cont):
                str = strings[i]
                str = str[:-1]
                if wrd.count(str) == 0:
                    break
    size = len(str)
    car = []
    for i in range(size):
        car.append(0)
    car[0] = car[size - 1] = 1
    for i in range(1, size - 1):
        if str[i].lower() == str[0].lower() or str[i].lower() == str[size - 1].lower():
            car[i] = 1
    cont, hs = 0, ''
    while full(str, car) == False:
        print('\033[4mLifes left\033[0m%s: %d\n' % (white, 6 - cont))
        draw(cont)
        if cont == 6:
            txt = ""
            for i in range(len(str)):
                txt += str[i]
                txt += '  '
            txt = txt[:-1]
            Window.fill(Black)
            text = basicFont.render('%s' % txt, True, Red, Black)
            textRect = text.get_rect()
            textRect.centerx = Window.get_rect().centerx
            textRect.centery = Window.get_rect().centery
            Window.blit(text, textRect)
            pygame.display.update()
            print('\nYou lost. Better luck next time!')
            wrd.append(str)
            with open('used_words.txt', 'wb') as file:
                pickle.dump(wrd, file)
            g.close()
            print('\nPress:\n1)For a new round\n2)For quitting the game\nAnswer: ', end = "")
            ans = int(input())
            while ans != 1 and ans != 2:
                ans = int(input('Incorrect answer! Try again: '))
            if ans == 1:
                function()
            else:
                pygame.quit()
                sys.exit()
            ans = int(input())
        okok = False
        while okok == False:
            txt = ""
            for i in range(len(str)):
                if car[i]:
                    txt += str[i]
                else:
                    txt += '_'
                txt += '  '
            txt = txt[:-1]
            Window.fill(Black)
            text = basicFont.render('%s' % txt, True, White, Black)
            textRect = text.get_rect()
            textRect.centerx = Window.get_rect().centerx
            textRect.centery = Window.get_rect().centery
            Window.blit(text, textRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    okok = True
                    if event.key == pygame.K_a:
                        chr = 'A'
                    elif event.key == pygame.K_b:
                        chr = 'B'
                    elif event.key == pygame.K_c:
                        chr = 'C'
                    elif event.key == pygame.K_d:
                        chr = 'D'
                    elif event.key == pygame.K_e:
                        chr = 'E'
                    elif event.key == pygame.K_f:
                        chr = 'F'
                    elif event.key == pygame.K_g:
                        chr = 'G'
                    elif event.key == pygame.K_h:
                        chr = 'H'
                    elif event.key == pygame.K_i:
                        chr = 'I'
                    elif event.key == pygame.K_j:
                        chr = 'J'
                    elif event.key == pygame.K_k:
                        chr = 'K'
                    elif event.key == pygame.K_l:
                        chr = 'L'
                    elif event.key == pygame.K_m:
                        chr = 'M'
                    elif event.key == pygame.K_n:
                        chr = 'N'
                    elif event.key == pygame.K_o:
                        chr = 'O'
                    elif event.key == pygame.K_p:
                        chr = 'P'
                    elif event.key == pygame.K_q:
                        chr = 'Q'
                    elif event.key == pygame.K_r:
                        chr = 'R'
                    elif event.key == pygame.K_s:
                        chr = 'S'
                    elif event.key == pygame.K_t:
                        chr = 'T'
                    elif event.key == pygame.K_u:
                        chr = 'U'
                    elif event.key == pygame.K_v:
                        chr = 'V'
                    elif event.key == pygame.K_w:
                        chr = 'W'
                    elif event.key == pygame.K_x:
                        chr = 'X'
                    elif event.key == pygame.K_y:
                        chr = 'Y'
                    elif event.key == pygame.K_z:
                        chr = 'Z'
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        okok = False
        g.write('%s\n' % chr)
        while len(chr) != 1 or chr.isalpha() == False:
            print('\n%sThe character typed is not a letter!%s\n\033[4mTry again\033[0m%s: ' % (red, white, white), end = "")
            chr = input()
        if str.count(chr.lower()) or str.count(chr.upper()):
            for i in range(size):
                if str[i].lower() == chr.lower():
                    car[i] = 1
        elif hs.count(chr.lower()) == 0:
            cont += 1
        hs += chr.lower()
        os.system('CLS')
    txt = ""
    for i in range(len(str)):
        if car[i]:
            txt += str[i]
        else:
            txt += '_'
        txt += '  '
    txt = txt[:-1]
    Window.fill(Black)
    text = basicFont.render('%s' % txt, True, Yellow, Black)
    textRect = text.get_rect()
    textRect.centerx = Window.get_rect().centerx
    textRect.centery = Window.get_rect().centery
    Window.blit(text, textRect)
    pygame.display.update()
    g.close()
    print('\033[4mLifes left\033[0m%s: %d\n' % (white, 6 - cont))
    draw(cont)
    print('\nCongratulations! You guessed the hidden word!')
    wrd.append(str)
    with open('used_words.txt', 'wb') as file:
        pickle.dump(wrd, file)
    g.close()
    print('\nPress:\n1)For a new round\n2)For quitting the game\nAnswer: ', end = "")
    ans = int(input())
    while ans != 1 and ans != 2:
        ans = int(input('Incorrect answer! Try again: '))
    if ans == 1:
        function()
    else:
        pygame.quit()
        sys.exit()
    ans = int(input())
function()
