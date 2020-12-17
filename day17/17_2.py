import numpy as np

raw_data = open("input.txt").read().split('\n')
#raw_data = open("input_test.txt").read().split('\n')


def create_start_matrix(raw_data):
    m = len(raw_data)
    n = len(raw_data[0])
    M = np.zeros((1,1,m,n)).astype(int)
    for x in range(m):
        for y in range(n) :
            if raw_data[x][y] == '#':
                M[0][0][x][y] = 1
    return M

def plongement(M):
    q, p, m, n = M.shape
    N = np.zeros((q + 4, p + 4, m + 4, n + 4)).astype(int)
    for h in range(q):
        for k in range(p):
            for i in range(m):
                for j in range(n):
                    N[h+2][k + 2][i + 2][j + 2] = M[h][k][i][j]    
    return N
    
def nb_voisins(M, h, k, i, j):
    voisins = 0
    for f in (h - 1, h, h + 1):
        for z in (k - 1, k, k + 1):
            for x in (i - 1, i , i + 1):
                for y in (j - 1, j , j + 1):
                    if M[f][z][x][y] == 1 and (f, z, x, y) != (h, k, i, j):
                        voisins += 1
    return voisins
                
def life_cycle(M):
    M = plongement(M)
    N = M.copy()
    q, p, m, n = N.shape
    for h in range(1, q - 1):
        for k in range(1, p - 1):
            for i in range(1, m - 1):
                for j in range(1, n - 1):
                    nb = nb_voisins(M, h, k ,i ,j)
                    if M[h][k][i][j] == 1 and nb in (2,3):
                        N[h][k][i][j] = 1
                    else :
                        N[h][k][i][j] = 0
                    if M[h][k][i][j] == 0 and nb == 3:
                        N[h][k][i][j] = 1
    return N


M = create_start_matrix(raw_data)
for _ in range(6):
    M = life_cycle(M)
sol = M.sum()
print(sol)
