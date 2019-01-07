import pygame, sys, os, random, time
from pygame.locals import *
str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rond, white, blue, red, green = 1, '\033[1;37;40m', '\033[1;34;40m', '\x1b[1;31;40m', '\033[1;32;40m'
def function(rond):
    pygame.init()
    Window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame Console")
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Gray = (128, 128, 128)
    Lime = (0, 255, 0)
    Blue = (0, 0, 255)
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('WELCOME TO GUESS THE LETTER!', True, Lime, Black)
    textRect = text.get_rect()
    textRect.centerx = Window.get_rect().centerx
    textRect.centery = Window.get_rect().centery
    Window.blit(text, textRect)
    pygame.display.update()
    Window.fill(Black)
    nr, count = random.randint(0, len(str) - 1), 0
    if rond is 1:
        print()
    print('%sRound %d)\n%sThink about a letter from %sA%s to %sZ%s and write it in the Pygame Console until you guess the letter generated\n' % (green, rond, white, blue, white, blue, white), end = "")
    okok = False
    while okok == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                if event.key == pygame.K_a:
                    le = 'A'
                elif event.key == pygame.K_b:
                    le = 'B'
                elif event.key == pygame.K_c:
                    le = 'C'
                elif event.key == pygame.K_d:
                    le = 'D'
                elif event.key == pygame.K_e:
                    le = 'E'
                elif event.key == pygame.K_f:
                    le = 'F'
                elif event.key == pygame.K_g:
                    le = 'G'
                elif event.key == pygame.K_h:
                    le = 'H'
                elif event.key == pygame.K_i:
                    le = 'I'
                elif event.key == pygame.K_j:
                    le = 'J'
                elif event.key == pygame.K_k:
                    le = 'K'
                elif event.key == pygame.K_l:
                    le = 'L'
                elif event.key == pygame.K_m:
                    le = 'M'
                elif event.key == pygame.K_n:
                    le = 'N'
                elif event.key == pygame.K_o:
                    le = 'O'
                elif event.key == pygame.K_p:
                    le = 'P'
                elif event.key == pygame.K_q:
                    le = 'Q'
                elif event.key == pygame.K_r:
                    le = 'R'
                elif event.key == pygame.K_s:
                    le = 'S'
                elif event.key == pygame.K_t:
                    le = 'T'
                elif event.key == pygame.K_u:
                    le = 'U'
                elif event.key == pygame.K_v:
                    le = 'V'
                elif event.key == pygame.K_w:
                    le = 'W'
                elif event.key == pygame.K_x:
                    le = 'X'
                elif event.key == pygame.K_y:
                    le = 'Y'
                elif event.key == pygame.K_z:
                    le = 'Z'
                elif event.key == pygame.K_ESCAPE:
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
    while le != str[nr]:
        os.system('CLS')
        count += 1
        if str.index(le) > str.index(str[nr]):
            text = basicFont.render('TOO RIGHT', True, Blue, Black)
        else:
            text = basicFont.render('TOO LEFT', True, Blue, Black)
        textRect = text.get_rect()
        textRect.centerx = Window.get_rect().centerx
        textRect.centery = Window.get_rect().centery
        Window.blit(text, textRect)
        pygame.display.update()
        Window.fill(Black)
        print('\033[4mAttempt number %d\033[0m' % count, end = "")
        print('\x1b[1;37;40m')
        print('You choose the letter %s%s%s\nTry again' % (blue, le, white))
        okok = False
        while okok == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                    if event.key == pygame.K_a:
                        le = 'A'
                    elif event.key == pygame.K_b:
                        le = 'B'
                    elif event.key == pygame.K_c:
                        le = 'C'
                    elif event.key == pygame.K_d:
                        le = 'D'
                    elif event.key == pygame.K_e:
                        le = 'E'
                    elif event.key == pygame.K_f:
                        le = 'F'
                    elif event.key == pygame.K_g:
                        le = 'G'
                    elif event.key == pygame.K_h:
                        le = 'H'
                    elif event.key == pygame.K_i:
                        le = 'I'
                    elif event.key == pygame.K_j:
                        le = 'J'
                    elif event.key == pygame.K_k:
                        le = 'K'
                    elif event.key == pygame.K_l:
                        le = 'L'
                    elif event.key == pygame.K_m:
                        le = 'M'
                    elif event.key == pygame.K_n:
                        le = 'N'
                    elif event.key == pygame.K_o:
                        le = 'O'
                    elif event.key == pygame.K_p:
                        le = 'P'
                    elif event.key == pygame.K_q:
                        le = 'Q'
                    elif event.key == pygame.K_r:
                        le = 'R'
                    elif event.key == pygame.K_s:
                        le = 'S'
                    elif event.key == pygame.K_t:
                        le = 'T'
                    elif event.key == pygame.K_u:
                        le = 'U'
                    elif event.key == pygame.K_v:
                        le = 'V'
                    elif event.key == pygame.K_w:
                        le = 'W'
                    elif event.key == pygame.K_x:
                        le = 'X'
                    elif event.key == pygame.K_y:
                        le = 'Y'
                    elif event.key == pygame.K_z:
                        le = 'Z'
                    elif event.key == pygame.K_ESCAPE:
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
        print('%s' % white, end = "")
    pygame.quit()
    os.system('CLS')
    print('\x1b[1;33;40mCongratulations%s, you guessed the letter %s%s%s of %s%d%s attempts!' % (white, blue, str[nr], white, blue, count + 1, white))
    print('\n\033[4mPress\033[0m%s\n1)for a new round\n2)for the end of the game\nAnswer: ' % white, end = "")
    op = int(input())
    while op != 1 and op != 2:
        print('\n%s\033[4mOption unavailable\033[0m%s!%s\nRe-enter one of the options above: ' % (red, red, white), end = "")
        op = int(input())
    if op is 1:
        os.system('CLS')
        function(rond + 1)
    else:
        sys.exit()
function(rond)
