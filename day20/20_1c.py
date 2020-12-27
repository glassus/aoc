import numpy as np

raw_data = open("input.txt").read().split('\n\n')
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


mpos = [[(122, 4), (30, 4), (86, 2), (45, 6), (104, 3), (133, 3), (111, 3), (95, 0), (131, 1), (71, 2), (39, 0), (58, 5)],\
        [(72, 1), (59, 4), (127, 1), (81, 0), (75, 1), (68, 3), (61, 3), (101, 3), (24, 0), (129, 2), (87, 3), (67, 3)],\
        [(82, 4), (107, 2), (80, 6), (84, 3), (57, 3), (11, 2), (77, 2), (138, 3), (114, 1), (51, 3), (118, 2), (63, 4)],\
        [(117, 2), (142, 6), (54, 2), (64, 0), (29, 1), (15, 4), (43, 1), (8, 5), (12, 5), (13, 3), (47, 3), (94, 4)],\
        [(130, 4), (28, 1), (83, 1), (44, 2), (85, 1), (35, 6), (66, 6), (49, 6), (7, 2), (19, 2), (79, 5), (50, 5)],\
        [(124, 6), (123, 0), (55, 5), (69, 1), (78, 6), (37, 4), (20, 5), (112, 4), (140, 5), (113, 4), (10, 0), (125, 3)],\
        [(25, 5), (115, 2), (14, 0), (119, 5), (42, 3), (93, 1), (96, 0), (33, 1), (34, 6), (128, 6), (62, 2), (16, 2)],\
        [(134, 6), (48, 4), (1, 5), (88, 0), (17, 2), (90, 5), (9, 3), (92, 4), (6, 6), (23, 5), (97, 6), (46, 6)],\
        [(136, 4), (26, 6), (76, 0), (60, 6), (103, 4), (53, 3), (4, 6), (18, 5), (100, 5), (141, 1), (139, 4), (132, 5)],\
        [(21, 6), (121, 2), (109, 2), (143, 4), (73, 6), (74, 3), (105, 3), (38, 6), (36, 5), (91, 3), (70, 6), (110, 2)],\
        [(126, 1), (135, 1), (2, 5), (56, 5), (27, 4), (137, 1), (65, 3), (5, 5), (31, 6), (102, 3), (52, 4), (108, 3)],\
        [(106, 4), (89, 6), (32, 6), (22, 4), (99, 2), (116, 0), (98, 5), (0, 1), (40, 6), (3, 5), (120, 4), (41, 6)]]


def crop(mt):
    return mt[1:9,1:9]

pic = np.zeros((96,96)).astype(int)

def copy_mat_2_pic(i, j, mat):
    global pic
    mat = crop(mat)
    dec_x = 8 * j
    dec_y = 8 * i
    for x in range(8):
        for y in range(8):
            pic[x + dec_x, y + dec_y] = mat[x , y]
            

for i in range(12):
    for j in range(12):
        target = mpos[i][j]
        mat = total_matrix[target[0]][target[1]]
        copy_mat_2_pic(i,j,mat)
        
dragon = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],\
                   [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],\
                   [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])

def is_drag(mat):
    for i in range(3):
        for j in range(20):
            if dragon[i,j] == 1:
                if mat[i,j] != 1:
                    return False
    return True

def test_drag(picture):
    k = 0
    for i in range(94):
        for j in range(77):
            zone = picture[i:i+3,j:j+20]
            if is_drag(zone):
                print("dragon !")
                k = k + 1
    return k     
#test_drag(pic)


pic_flipV = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipV[i][j] = pic[95-i][j]

#test_drag(pic_flipV)

pic_flipH = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipH[i][j] = pic[i][95-j]

#test_drag(pic_flipH)

pic_flipVH = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipVH[i][j] = pic[95-i][95-j]

#test_drag(pic_flipVH)

pic_flipR1 = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipR1[i][j] = pic[j][95-i]

#test_drag(pic_flipR1)

pic_flipR2 = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipR2[i][j] = pic[95-j][i]

#test_drag(pic_flipR2)

pic_flipR3 = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipR3[i][j] = pic[95-j][95-i]

#test_drag(pic_flipR3)

pic_flipR1V = np.zeros((96,96)).astype(int)
for i in range(96):
    for j in range(96):
        pic_flipR1V[i][j] = pic_flipR1[95-i][j]

print(test_drag(pic_flipR1V))