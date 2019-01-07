import random, sys
def zone(line, col):
    if line >= 0 and line <= 2 and col >= 0 and col <= 2:
        return 1
    if line >= 0 and line <= 2 and col >= 3 and col <= 5:
        return 2
    if line >= 0 and line <=2 and col >=6 and col <= 8:
        return 3
    if line >= 3 and line <= 5 and col >= 0 and col <= 2:
        return 4
    if line >= 3 and line <= 5 and col >= 3 and col <= 5:
        return 5
    if line >= 3 and line <=5 and col >=6 and col <= 8:
        return 6
    if line >= 6 and line <= 8 and col >= 0 and col <= 2:
        return 7
    if line >= 6 and line <= 8 and col >= 3 and col <= 5:
        return 8
    return 9
def type():
    g = open('file.out','w')
    for l in range(9):
        for c in range(9):
            g.write('%d' % matrix[l][c])
            if c < 8:
                g.write(' ')
        g.write('\n')
    g.close()
def white_spaces():
    count = 0
    for i in range(9):
        for j in range(9):
            if matrix[i][j] is 0:
                count += 1
    return count
#main function
f = open('file.in','r')
matrix = [[int(num) for num in line.split(' ')] for line in f]
f.close()
sp, p = white_spaces(), []
for i in range(9):
    for j in range(9):
        if matrix[i][j] is 0:
            a = [i, j]
            p.append(a)
okok = False
while okok is False:
    k, okok = 0, True
    while k < sp:
        line, col, v = p[k][0], p[k][1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if matrix[i][col]:
                v[matrix[i][col]] = 1
            if matrix[line][i]:
                v[matrix[line][i]] = 1
        if zone(line, col) is 1:
            for i in range(0, 3):
                for j in range(0, 3):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 2:
            for i in range(0, 3):
                for j in range(3, 6):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 3:
            for i in range(0, 3):
                for j in range(6, 9):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 4:
            for i in range(3, 6):
                for j in range(0, 3):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 5:
            for i in range(3, 6):
                for j in range(3, 6):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 6:
            for i in range(3, 6):
                for j in range(6, 9):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 7:
            for i in range(6, 9):
                for j in range(0, 3):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        elif zone(line, col) is 8:
            for i in range(6, 9):
                for j in range(3, 6):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if matrix[i][j]:
                        v[matrix[i][j]] = 1
        vs, cont = [], 0
        for i in range(1, 10):
            if v[i] == 0:
                cont += 1
                vs.append(i)
        if cont >= 1:
            val = random.randint(0, cont - 1)
            val = vs[val]
            matrix[line][col] = val
            k += 1
        else:
            okok = False
            break
type()
