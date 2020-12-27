import numpy as np

#raw_data = open("input.txt").read().split('\n\n')
#raw_data = open("input_test.txt").read().split('\n\n')

raw_mtx = open("mtrix.txt").read().split('\n')



mats = []
corr = []
for line in raw_data:
    corr.append(line.split('\n')[0])
    mats.append(line.split('\n')[1:])
    
matrix = [np.zeros((10,10)).astype(int) for k in range(144)]

for k in range(len(mats)):
    for i in range(len(mats[0])):
        for j in range(len(mats[0][0])):
            if mats[k][i][j] == '#':
                matrix[k][i][j] = 1
    
matrix_flipV = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipV[k][i][j] = matrix[k][9-i][j]
            
matrix_flipH = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipH[k][i][j] = matrix[k][i][9-j]
            
matrix_flipVH = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipVH[k][i][j] = matrix[k][9-i][9-j]
            
            
matrix_flipR1 = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR1[k][i][j] = matrix[k][j][9-i]
            
matrix_flipR2 = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR2[k][i][j] = matrix[k][9-j][i]
            
            
matrix_flipR3 = [np.zeros((10,10)).astype(int) for k in range(144)]
for k in range(len(matrix)):
    for i in range(10):
        for j in range(10):
            matrix_flipR3[k][i][j] = matrix[k][9-j][9-i]
            
total_matrix = [[] for k in range(144)]
for k in range(144):
    total_matrix[k].append(matrix[k])
    total_matrix[k].append(matrix_flipV[k])
    total_matrix[k].append(matrix_flipH[k])
    total_matrix[k].append(matrix_flipVH[k])
    total_matrix[k].append(matrix_flipR1[k])       
    total_matrix[k].append(matrix_flipR2[k])
    total_matrix[k].append(matrix_flipR3[k])
    

def search_h(start, version):
    
    already_used = [start]
    combs = [(start, version)]
    for k in range(11):
        cible = total_matrix[start][version][:,9]
        for base in range(144):
            if base in already_used :
                continue
            for vers in range(7):
                if all(total_matrix[base][vers][:,0] == cible) :
                    combs.append((base, vers))
                    already_used.append(base)
                    start, version = base, vers
    if len(combs) == 12 :
        return(combs)
    return None


#total_combsH = []
#for k in range(144):
#    for v in range(7):
#        rep = search_h(k,v)
#        if rep is not None:
#            total_combsH.append(rep)

def search_v(combi):
    start = combi[0]
    version = combi[1]
    already_used = [start]
    combs = [(start, version)]
    for k in range(11):
        cible = total_matrix[start][version][9,:]
        for base in range(144):
            if base in already_used :
                continue
            for vers in range(7):
                if all(total_matrix[base][vers][0,:] == cible) :
                    combs.append((base, vers))
                    already_used.append(base)
                    start, version = base, vers
    if len(combs) == 12 :
        return combs
    return None

#for combi in total_combsH:
#     #print(combi)
#    if (search_v(combi[0]) is not None) and  (search_v(combi[1]) is not None) and (search_v(combi[2]) is not None) :
#        print(combi)
#        print(search_v(combi[0]))
#        print(search_v(combi[1]))
#        print(search_v(combi[2]))