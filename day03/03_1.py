l = open("input.txt").read().split('\n')[:-1]

x, y = 0, 0
nb_arbres = 0

while y < len(l) :
    if l[y][x] == '#' :
        nb_arbres += 1
    x = (x + 3) % len(l[0])
    y = y + 1

print(nb_arbres)