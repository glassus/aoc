import numpy as np
import numpy.linalg as alg



raw_data = open("inputB.txt").read().split('\n')[:-1]
raw_data = open("input_test_B.txt").read().split('\n')[:-1]

instructions = [(data[0], int(data[1:])) for data in raw_data]


pos = np.array((0,0), int)
boussole = np.array((10,1),int)

mvt = {
    'N' : np.array((0,1), int),
    'S' : np.array((0,-1), int),
    'E' : np.array((1,0), int),
    'W' : np.array((-1,0), int)
    }

def mat_rot(angle):
    nb = angle // 90
    ang = np.radians(90)
    r = np.array(( (int(np.cos(ang)), int(-np.sin(ang))),
                   (int(np.sin(ang)),  int(np.cos(ang))) ))
    return alg.matrix_power(r,nb).astype(int)

for inst in instructions :
    lettre = inst[0]
    val = inst[1]
    if lettre in ['N','S','W','E']:
        boussole += val*mvt[lettre]
    if lettre == 'F':
        pos += val*boussole
    if lettre == 'L':
        boussole = boussole.dot(mat_rot(-val))
    if lettre == 'R':
        boussole = boussole.dot(mat_rot(val))
    print(boussole, pos)
    
print(abs(pos[0]) + abs(pos[1]))