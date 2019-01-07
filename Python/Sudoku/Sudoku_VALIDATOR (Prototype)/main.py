import sys
def verif(li, lf, ci, cf):
    car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(li, lf):
        for j in range(ci, cf):
            if matrix[i][j] == 0:
                continue
            if car[matrix[i][j]] == 1:
                print('Incorrect!')
                sys.exit()
            car[matrix[i][j]] = 1
def main():
    for i in range(9):
        car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            if matrix[i][j] == 0:
                continue
            if car[matrix[i][j]] == 1:
                print('Incorrect!')
                sys.exit()
            car[matrix[i][j]] = 1
    for i in range(9):
        car = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            if matrix[j][i] == 0:
                continue
            if car[matrix[j][i]] == 1:
                print('Incorrect!')
                sys.exit()
            car[matrix[j][i]] = 1
    verif(0, 3, 0, 3)
    verif(0, 3, 3, 6)
    verif(0, 3, 6, 9)
    verif(3, 6, 0, 3)
    verif(3, 6, 3, 6)
    verif(3, 6, 6, 9)
    verif(6, 9, 0, 3)
    verif(6, 9, 3, 6)
    verif(6, 9, 6, 9)
    print('Correct!')
f = open('matrix.in','r')
matrix = [[int(num) for num in line.split(' ')] for line in f]
f.close()
main()
