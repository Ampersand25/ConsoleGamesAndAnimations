'''
print('\x1b[1;31;40m') 4 red txt
print('\x1b[1;32;40m') 4 green txt
print('\x1b[1;33;40m') 4 yellow txt
print('\x1b[1;34;40m') 4 blue txt
print('\x1b[1;35;40m') 4 pink txt
print('\x1b[1;36;40m') 4 cyan txt
print('\x1b[1;37;40m') 4 white txt
2 4 8 16 32 64 128 256 512 1024 2048 - the positive powers of 2 until 2048 (except 1)
'''
import pygame, sys, os, random, time, pickle
from pygame.locals import *
def win_game(matrix):
    for i in range(4):
        if matrix[i][i] == 2048:
            return True
        for j in range(i + 1, 4):
            if matrix[i][j] == 2048 or matrix[j][i] == 2048:
                return True
    return False
def is_full(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
    return True
def game_over(matrix):
    if is_full(matrix) == False:
        return False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1]:
                return False
    for i in range(4):
        for j in range(3):
            if matrix[j][i] == matrix[j + 1][i]:
                return False
    return True
def nr_cif(cont):
    if not cont:
        return 1
    var = 0
    while cont:
        var += 1
        cont //= 10
    return var
def el_max(matrix, col):
    mx = 0
    for i in range(4):
        if matrix[i][col] > mx:
            mx = matrix[i][col]
    return mx
def red():
    print('\x1b[1;31;40m', end = "")
def green():
    print('\x1b[1;32;40m', end = "")
def yellow():
    print('\x1b[1;33;40m', end = "")
def blue():
    print('\x1b[1;34;40m', end = "")
def pink():
    print('\x1b[1;35;40m', end = "")
def cyan():
    print('\x1b[1;36;40m', end = "")
def white():
    print('\x1b[1;37;40m', end = "")
def convert(elem):
    if elem == 2 or elem == 128:
        red()
    elif elem == 4 or elem == 256:
        green()
    elif elem == 8 or elem == 512:
        yellow()
    elif elem == 16 or elem == 1024:
        blue()
    elif elem == 32 or elem == 4096:
        pink()
    elif elem == 64 or elem == 8192:
        cyan()
def special():
    print('\x1b[1;31;40m2', end = "")
    print('\x1b[1;32;40m0', end = "")
    print('\x1b[1;35;40m4', end = "")
    print('\x1b[1;36;40m8', end = "")
def color(ind):
    if ind == 0:
        white()
    elif ind % 6 == 0:
        red()
    elif ind % 6 == 1:
        green()
    elif ind % 6 == 2:
        yellow()
    elif ind % 6 == 3:
        blue()
    elif ind % 6 == 4:
        pink()
    else:
        cyan()
def type(matrix, score, val):
    print('Move nr: %d' % num)
    print('\x1b[1;37;41mHigh-Score\x1b[1;37;40m %d' % hs)
    print('\x1b[1;37;41mScore\x1b[1;37;40m ', end = "")
    color(val)
    print('%d\n\x1b[1;37;40m' % score[0])
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != 0 and matrix[i][j] != 2048:
                convert(matrix[i][j])
                print('%d' % matrix[i][j], end = "")
                print('\x1b[1;37;40m', end = "")
            elif matrix[i][j] == 2048:
                special()
                print('\x1b[1;37;40m', end = "")
            else:
                print('*', end = "")
            k = nr_cif(el_max(matrix, j)) - nr_cif(matrix[i][j]) + 1
            print(' ' * k, end = "")
        if i == 3:
            print()
        else:
            print('\n')
def up(matrix, score):
    for i in range(4):
        if matrix[0][i] != 0 and matrix[1][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[1][i] = 0
            if matrix[2][i] != 0 and matrix[2][i] == matrix[3][i]:
                matrix[2][i] *= 2
                score[0] += matrix[2][i]
                matrix[3][i] = 0
        elif matrix[0][i] != 0 and matrix[1][i] == 0 and matrix[2][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[2][i] = 0
        elif matrix[0][i] != 0 and matrix[1][i] == 0 and matrix[2][i] == 0 and matrix[3][i] == matrix[0][i]:
            matrix[0][i] *= 2
            score[0] += matrix[0][i]
            matrix[3][i] = 0
        elif matrix[1][i] != 0 and matrix[2][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[2][i] = 0
        elif matrix[1][i] != 0 and matrix[2][i] == 0 and matrix[3][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[3][i] = 0
        elif matrix[2][i] != 0 and matrix[3][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[3][i] = 0
    for i in range(4):
        if matrix[2][i] == 0 and matrix[3][i] != 0:
            matrix[2][i] = matrix[3][i]
            matrix[3][i] = 0
        if matrix[1][i] == 0 and matrix[2][i] != 0:
            matrix[1][i] = matrix[2][i]
            matrix[2][i] = 0
            if matrix[3][i] != 0:
                matrix[2][i] = matrix[3][i]
                matrix[3][i] = 0
        if matrix[0][i] == 0 and matrix[1][i]:
            matrix[0][i] = matrix[1][i]
            matrix[1][i] = 0
            if matrix[2][i] != 0:
                matrix[1][i] = matrix[2][i]
                matrix[2][i] = 0
                if matrix[3][i] != 0:
                    matrix[2][i] = matrix[3][i]
                    matrix[3][i] = 0
def down(matrix, score):
    for i in range(4):
        if matrix[3][i] != 0 and matrix[2][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[2][i] = 0
            if matrix[1][i] != 0 and matrix[1][i] == matrix[0][i]:
                matrix[1][i] *= 2
                score[0] += matrix[1][i]
                matrix[0][i] = 0
        elif matrix[3][i] != 0 and matrix[2][i] == 0 and matrix[1][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[1][i] = 0
        elif matrix[3][i] != 0 and matrix[2][i] == 0 and matrix[1][i] == 0 and matrix[0][i] == matrix[3][i]:
            matrix[3][i] *= 2
            score[0] += matrix[3][i]
            matrix[0][i] = 0
        elif matrix[2][i] != 0 and matrix[1][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[1][i] = 0
        elif matrix[2][i] != 0 and matrix[1][i] == 0 and matrix[0][i] == matrix[2][i]:
            matrix[2][i] *= 2
            score[0] += matrix[2][i]
            matrix[0][i] = 0
        elif matrix[1][i] != 0 and matrix[0][i] == matrix[1][i]:
            matrix[1][i] *= 2
            score[0] += matrix[1][i]
            matrix[0][i] = 0
    for i in range(4):
        if matrix[1][i] == 0 and matrix[0][i] != 0:
            matrix[1][i] = matrix[0][i]
            matrix[0][i] = 0
        if matrix[2][i] == 0 and matrix[1][i] != 0:
            matrix[2][i] = matrix[1][i]
            matrix[1][i] = 0
            if matrix[0][i] != 0:
                matrix[1][i] = matrix[0][i]
                matrix[0][i] = 0
        if matrix[3][i] == 0 and matrix[2][i]:
            matrix[3][i] = matrix[2][i]
            matrix[2][i] = 0
            if matrix[1][i] != 0:
                matrix[2][i] = matrix[1][i]
                matrix[1][i] = 0
                if matrix[0][i] != 0:
                    matrix[1][i] = matrix[0][i]
                    matrix[0][i] = 0
def left(matrix, score):
    for i in range(4):
        if matrix[i][0] != 0 and matrix[i][1] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][1] = 0
            if matrix[i][2] != 0 and matrix[i][2] == matrix[i][3]:
                matrix[i][2] *= 2
                score[0] += matrix[i][2]
                matrix[i][3] = 0
        elif matrix[i][0] != 0 and matrix[i][1] == 0 and matrix[i][2] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][2] = 0
        elif matrix[i][0] != 0 and matrix[i][1] == 0 and matrix[i][2] == 0 and matrix[i][3] == matrix[i][0]:
            matrix[i][0] *= 2
            score[0] += matrix[i][0]
            matrix[i][3] = 0
        elif matrix[i][1] != 0 and matrix[i][2] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][2] = 0
        elif matrix[i][1] != 0 and matrix[i][2] == 0 and matrix[i][3] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][3] = 0
        elif matrix[i][2] != 0 and matrix[i][3] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][3] = 0
    for i in range(4):
        if matrix[i][2] == 0 and matrix[i][3] != 0:
            matrix[i][2] = matrix[i][3]
            matrix[i][3] = 0
        if matrix[i][1] == 0 and matrix[i][2] != 0:
            matrix[i][1] = matrix[i][2]
            matrix[i][2] = 0
            if matrix[i][3] != 0:
                matrix[i][2] = matrix[i][3]
                matrix[i][3] = 0
        if matrix[i][0] == 0 and matrix[i][1]:
            matrix[i][0] = matrix[i][1]
            matrix[i][1] = 0
            if matrix[i][2] != 0:
                matrix[i][1] = matrix[i][2]
                matrix[i][2] = 0
                if matrix[i][3] != 0:
                    matrix[i][2] = matrix[i][3]
                    matrix[i][3] = 0
def right(matrix, score):
    for i in range(4):
        if matrix[i][3] != 0 and matrix[i][2] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][2] = 0
            if matrix[i][1] != 0 and matrix[i][1] == matrix[i][0]:
                matrix[i][1] *= 2
                score[0] += matrix[i][1]
                matrix[i][0] = 0
        elif matrix[i][3] != 0 and matrix[i][2] == 0 and matrix[i][1] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][1] = 0
        elif matrix[i][3] != 0 and matrix[i][2] == 0 and matrix[i][1] == 0 and matrix[i][0] == matrix[i][3]:
            matrix[i][3] *= 2
            score[0] += matrix[i][3]
            matrix[i][0] = 0
        elif matrix[i][2] != 0 and matrix[i][1] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][1] = 0
        elif matrix[i][2] != 0 and matrix[i][1] == 0 and matrix[i][0] == matrix[i][2]:
            matrix[i][2] *= 2
            score[0] += matrix[i][2]
            matrix[i][0] = 0
        elif matrix[i][1] != 0 and matrix[i][0] == matrix[i][1]:
            matrix[i][1] *= 2
            score[0] += matrix[i][1]
            matrix[i][0] = 0
    for i in range(4):
        if matrix[i][1] == 0 and matrix[i][0] != 0:
            matrix[i][1] = matrix[i][0]
            matrix[i][0] = 0
        if matrix[i][2] == 0 and matrix[i][1] != 0:
            matrix[i][2] = matrix[i][1]
            matrix[i][1] = 0
            if matrix[i][0] != 0:
                matrix[i][1] = matrix[i][0]
                matrix[i][0] = 0
        if matrix[i][3] == 0 and matrix[i][2]:
            matrix[i][3] = matrix[i][2]
            matrix[i][2] = 0
            if matrix[i][1] != 0:
                matrix[i][2] = matrix[i][1]
                matrix[i][1] = 0
                if matrix[i][0] != 0:
                    matrix[i][1] = matrix[i][0]
                    matrix[i][0] = 0
def copy(m1, m2):
    for i in range(4):
        for j in range(4):
            m1[i][j] = m2[i][j]
def same(m1, m2):
    for i in range(4):
        for j in range(4):
            if m1[i][j] != m2[i][j]:
                return False
    return True
def maximum(matrix):
    cmax = 0
    for i in range(4):
        for j in range(4):
            if cmax < matrix[i][j]:
                cmax = matrix[i][j]
    return cmax
def stats_display():
    f = open('stats.txt','w')
    f.write('Total number of games played: %d' % m)
    f.write('\nAll time highest score: %d' % hss)
    f.write('\nThe highest number displayed in a game: %d' % hn)
    f.write('\nNumber of victories (= number of times a player achieved the target of 2048): %d' % vs)
    f.write('\nNumber of moves it takes to achieved 2048: ')
    if len(steps) == 0:
        f.write('-')
    for i in range(len(steps)):
        f.write('%d' % steps[i])
        if i < len(steps) - 1:
            f.write(',')
        f.write(' ')
    f.close()
#main function
try:
    with open('high_score.txt', 'rb') as file:
        hs = pickle.load(file)
except:
    hs = 0
try:
    with open('highest_score.txt', 'rb') as file:
        hss = pickle.load(file)
except:
    hss = hs
try:
    with open('matches_count.txt', 'rb') as file:
        m = pickle.load(file)
except:
    m = 0
try:
    with open('victories_count.txt', 'rb') as file:
        vs = pickle.load(file)
except:
    vs = 0
try:
    with open('highest_number.txt', 'rb') as file:
        hn = pickle.load(file)
except:
    hn = 0
try:
    with open('steps.txt', 'rb') as file:
        steps = pickle.load(file)
except:
    steps = []
print('\x1b[1;37;40m\nWelcome to ', end = "")
special()
print('\x1b[1;37;40m!\n\n\x1b[1;31;40m\033[4mHOW TO PLAY\033[0m\x1b[1;37;40m:\nUse the arrow keys or the W/A/S/D on your keyboard to move the tiles in the direction you want.\nWhen two tiles with the same number touch, they merge into one!\n')
print('Created by \x1b[1;31;40mGabriele Cirulli\x1b[1;37;40m.\nBased on 1024 by Veewo Studio and conceptually similar to Threes by Asher Vollmer.\n')
mat = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]
cmat = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
l = random.randint(0, 3)
c = random.randint(0, 3)
mat[l][c] = 2
l = random.randint(0, 3)
c = random.randint(0, 3)
while mat[l][c] != 0:
    l = random.randint(0, 3)
    c = random.randint(0, 3)
mat[l][c], val, ok = 2, 0, True
score, typo, num = [0], 0, 1
print('\033[4m\x1b[1;31;40mNote\033[0m\x1b[1;37;40m: if you want to reset your high-score during the game press R in pygame console.\n')
os.system('PAUSE')
os.system('CLS')
pygame.init()
m += 1
with open('matches_count.txt', 'wb') as file:
    pickle.dump(m, file)
stats_display()
Window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("2048 Pyton Version by Cristian Stanciu")
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Gray = (128, 128, 128)
Lime = (0, 255, 0)
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('WELCOME TO 2048!', True, Lime, Black)
textRect = text.get_rect()
textRect.centerx = Window.get_rect().centerx
textRect.centery = Window.get_rect().centery
Window.blit(text, textRect)
pygame.display.update()
Window.fill(Black)
type(mat, score, val)
while game_over(mat) == False:
    if maximum(mat) > hn:
        hn = maximum(mat)
        with open('highest_number.txt', 'wb') as file:
            pickle.dump(hn, file)
        stats_display()
    copy(cmat, mat)
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
                stats_display()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                okok = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up(mat, score)
                    text = basicFont.render('UP', True, White, Black)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down(mat, score)
                    text = basicFont.render('DOWN', True, White, Black)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left(mat, score)
                    text = basicFont.render('LEFT', True, White, Black)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right(mat, score)
                    text = basicFont.render('RIGHT', True, White, Black)
                elif event.key == pygame.K_ESCAPE:
                    text = basicFont.render('QUITTING...', True, Gray, Black)
                    textRect = text.get_rect()
                    textRect.centerx = Window.get_rect().centerx
                    textRect.centery = Window.get_rect().centery
                    Window.blit(text, textRect)
                    pygame.display.update()
                    time.sleep(1.5)
                    stats_display()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    okok = False
                    hs = score[0]
                    with open('high_score.txt', 'wb') as file:
                        pickle.dump(hs, file)
                    stats_display()
                    os.system('CLS')
                    type(mat, score, val)
                else:
                    okok = False
                    text = basicFont.render('INVALID COMMAND', True, Red, Black)
                textRect = text.get_rect()
                textRect.centerx = Window.get_rect().centerx
                textRect.centery = Window.get_rect().centery
                Window.blit(text, textRect)
                pygame.display.update()
                if not okok:
                    Window.fill(Black)
    if same(cmat,mat) == False:
        l = random.randint(0, 3)
        c = random.randint(0, 3)
        while mat[l][c] != 0:
            l = random.randint(0, 3)
            c = random.randint(0, 3)
        mat[l][c] = 2
        num += 1
    if score[0] != typo:
        val += 1
        typo = score[0]
        if score[0] >= hs:
            hs = score[0]
            with open('high_score.txt', 'wb') as file:
                pickle.dump(hs, file)
            stats_display()
        if hs >= hss:
            hss = hs
            with open('highest_score.txt', 'wb') as file:
                pickle.dump(hss, file)
            stats_display()
    if same(cmat,mat) == False:
        os.system('CLS')
        type(mat, score, val)
    if win_game(mat) == True and ok == True:
        vic += 1
        steps.append(num)
        with open('steps.txt', 'wb') as file:
            pickle.dump(steps, file)
        with open('victories_count.txt', 'wb') as file:
            pickle.dump(vic, file)
        stats_display()
        text = basicFont.render('CONGRATULATIONS!', True, Yelloww, Black)
        textRect = text.get_rect()
        textRect.centerx = Window.get_rect().centerx
        textRect.centery = Window.get_rect().centery
        Window.blit(text, textRect)
        pygame.display.update()
        print('\n\x1b[1;37;43mCongratulations, you succesfully achieved the objective of the game!\x1b[1;37;40m')
        ok = False
    Window.fill(Black)
print('\n\x1b[1;37;41mGame over!\x1b[1;37;40m')
text = basicFont.render('GAME OVER!', True, Gray, Black)
textRect = text.get_rect()
textRect.centerx = Window.get_rect().centerx
textRect.centery = Window.get_rect().centery
Window.blit(text, textRect)
pygame.display.update()
time.sleep(1.5)
stats_display()
pygame.quit()
sys.exit()
