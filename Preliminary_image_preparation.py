import sys
import math
import numpy as np
ciner = input()
H_W = ciner.split(" ")
W = int(H_W[0])
H = int(H_W[1])
mat = np.zeros((H, W, 7))
#0 - R
#1 - G
#2 - B
#3 - P
#4 - New_R
#5 - New_G
#6 - New_B
ciner = input()
bred = ciner.split(' ')
scetbred = 0
for i in range(H) :
    for j in range(W) :
        mat[i][j][0] = int(bred[scetbred][0:2], 16)
        mat[i][j][1] = int(bred[scetbred][2:4], 16)
        mat[i][j][2] = int(bred[scetbred][4:6], 16)
        scetbred = scetbred + 1
com1 = input()
com2 = input()



'''print('Orig:')
for i in range(0,H):
    for j in range(0,W):
        print(i,j,":",mat[i][j][0:7])
print()'''
#фильтр, основанный на вычислении среднего геометрического;
if com1 == '1':
    for i in range(1, H - 1) :
        for j in range(1, W - 1) :
            mat[i][j][4] = math.floor((mat[i - 1][j - 1][0] * mat[i - 1][j][0] * mat[i - 1][j + 1][0] * mat[i][j - 1][0] * mat[i][j][0] * mat[i][j + 1][0] * mat[i + 1][j - 1][0] * mat[i + 1][j][0] * mat[i + 1][j + 1][0])** (1. / 9.))
            mat[i][j][5] = math.floor((mat[i - 1][j - 1][1] * mat[i - 1][j][1] * mat[i - 1][j + 1][1] * mat[i][j - 1][1] * mat[i][j][1] * mat[i][j + 1][1] * mat[i + 1][j - 1][1] * mat[i + 1][j][1] * mat[i + 1][j + 1][1])** (1. / 9.))
            mat[i][j][6] = math.floor((mat[i - 1][j - 1][2] * mat[i - 1][j][2] * mat[i - 1][j + 1][2] * mat[i][j - 1][2] * mat[i][j][2] * mat[i][j + 1][2] * mat[i + 1][j - 1][2] * mat[i + 1][j][2] * mat[i + 1][j + 1][2])**(1. / 9.))

#медианный фильтр.
elif com1=='2':
    for i in range(1, H - 1) :
        for j in range(1, W - 1):
            lis = [mat[i - 1][j - 1][0], mat[i - 1][j][0], mat[i - 1][j + 1][0], mat[i][j - 1][0], mat[i][j][0], mat[i][j + 1][0], mat[i + 1][j - 1][0], mat[i + 1][j][0], mat[i + 1][j + 1][0]]
            lis.sort()
            mat[i][j][4] = lis[4]
            lis = [mat[i - 1][j - 1][1], mat[i - 1][j][1], mat[i - 1][j + 1][1], mat[i][j - 1][1], mat[i][j][1], mat[i][j + 1][1], mat[i + 1][j - 1][1], mat[i + 1][j][1], mat[i + 1][j + 1][1]]
            lis.sort()
            mat[i][j][5] = lis[4]
            lis = [mat[i - 1][j - 1][2], mat[i - 1][j][2], mat[i - 1][j + 1][2], mat[i][j - 1][2], mat[i][j][2], mat[i][j + 1][2], mat[i + 1][j - 1][2], mat[i + 1][j][2], mat[i + 1][j + 1][2]]
            lis.sort()
            mat[i][j][6] = lis[4]

'''print('После подавления шума:')
for i in range(11,14):
    for j in range(0,2):
        print(i,j,":",mat[i][j][0:7])
print()'''
#использование cреднего арифметического;
if com2 == '1':
    for i in range(H) :
        for j in range(W) :
            if (i == 0) or (j == 0) or (i == H - 1) or (j == W - 1):
                mat[i][j][3] = (mat[i][j][0] + mat[i][j][1] + mat[i][j][2])/ 3
            else :
                mat[i][j][3] = (mat[i][j][4] + mat[i][j][5] + mat[i][j][6])/ 3
            mat[i][j][3] = math.floor(mat[i][j][3])

# использование средневзвешенного;
elif com2 == '2' :
    for i in range(H) :
        for j in range(W) :
            if (i == 0) or (j == 0) or (i == H - 1) or (j == W - 1):
                mat[i][j][3] = 0.299*mat[i][j][0] + 0.587*mat[i][j][1] + 0.114*mat[i][j][2]
            else :
                mat[i][j][3] = 0.299*mat[i][j][4] + 0.587*mat[i][j][5] + 0.114*mat[i][j][6]
            mat[i][j][3]=math.floor(mat[i][j][3])

# использование ближайшей точки на нейтральной оси;
elif com2 == '3' :
    for i in range(H) :
        for j in range(W) :
            if (i == 0) or (j == 0) or (i == H - 1) or (j == W - 1):
                mat[i][j][3] = (max(mat[i][j][0], max(mat[i][j][2], mat[i][j][1])) + min(mat[i][j][0], min(mat[i][j][2], mat[i][j][1]))) / 2
            else :
                mat[i][j][3] = (max(mat[i][j][4], max(mat[i][j][6], mat[i][j][5])) + min(mat[i][j][4], min(mat[i][j][6], mat[i][j][5]))) / 2
            mat[i][j][3] = math.floor(mat[i][j][3])

#определение величины яркости.
elif com2 == '4' :
    for i in range(H) :
        for j in range(W) :
            if (i == 0) or (j == 0) or (i == H - 1) or (j == W - 1):
                mat[i][j][3] = max(mat[i][j][0], max(mat[i][j][2], mat[i][j][1]))
            else:
                mat[i][j][3] = max(mat[i][j][4], max(mat[i][j][6], mat[i][j][5]))

'''print('Итог:')
for i in range(11,14):
    for j in range(0,2):
        print(i,j,":",mat[i][j][0:7])
print()'''
min=256
max=0
for i in range(H) :
    for j in range(W) :
        if max<mat[i][j][3]:
            max=mat[i][j][3]
        if min>mat[i][j][3]:
            min=mat[i][j][3]
print(int(min), int(max))
