l = open("input.txt").read().split('\n')[:-1]

def slope(mvt):
    x, y = 0, 0
    nb_arbres = 0

    while y < len(l) :
        if l[y][x] == '#' :
            nb_arbres += 1
        x = (x + mvt[0]) % len(l[0])
        y = y + mvt[1]
        
    return nb_arbres

pdt = 1
for mvt in [(1,1), (3,1), (5,1), (7,1), (1,2)] :
    pdt *= slope(mvt)

print(pdt)
