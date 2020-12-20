import numpy as np

#raw_data = open("input.txt").read().split('\n\n')
raw_data = open("input_test.txt").read().split('\n\n')





mats = []
corr = []
for line in raw_data:
    corr.append(line.split('\n')[0])
    mats.append(line.split('\n')[1:])
    
matrix = [np.zeros((10,10)).astype(int) for k in range(9)]

for k in range(len(mats)):
    for i in range(len(mats[0])):
        for j in range(len(mats[0][0])):
            if mats[k][i][j] == '#':
                matrix[k][i][j] = 1
    
matrix_flipV = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipV[k][i][j] = matrix[k][9-i][j]
            
matrix_flipH = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipH[k][i][j] = matrix[k][i][9-j]
            
matrix_flipVH = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipVH[k][i][j] = matrix[k][9-i][9-j]
            
            
matrix_flipR1 = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR1[k][i][j] = matrix[k][j][9-i]
            
matrix_flipR2 = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR2[k][i][j] = matrix[k][9-j][i]
            
            
matrix_flipR3 = [np.zeros((10,10)).astype(int) for k in range(9)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR3[k][i][j] = matrix[k][9-j][9-i]
            
            
start = 0
cible = matrix[start][:,9]
for k in range(9):
    for mat in (matrix_flipH, matrix_flipV, matrix_flipVH, \
                matrix_flipR1, matrix_flipR2, matrix_flipR3):
        if all(mat[k][:,0] == cible):
            print(mat[k])
        