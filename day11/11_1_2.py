from copy import deepcopy

raw_tab = open("input.txt").read().split('\n')
#raw_tab = open("input_test.txt").read().split('\n')

tab = []
for rangee in raw_tab :
    tp = []
    for car in rangee:
        tp.append(car)
    tab.append(tp)

haut = len(tab)
larg = len(tab[0])

def count_symbol1(tab, x, y, symb):
    if (0 < x < haut-1) and (0 < y < larg-1) :
        list_voisins = [tab[x-1][y-1], tab[x-1][y], tab[x-1][y+1],tab[x][y-1],tab[x][y+1],tab[x+1][y-1],tab[x+1][y],tab[x+1][y+1]]
          
    if (x == 0) and (0 < y < larg-1) :
        list_voisins = [tab[x][y-1],tab[x][y+1],tab[x+1][y-1],tab[x+1][y],tab[x+1][y+1]]
  
        
    if (x==haut-1) and (0 < y < larg-1) :
        list_voisins = [tab[x-1][y-1], tab[x-1][y], tab[x-1][y+1],tab[x][y-1],tab[x][y+1]]
   
 
    if (0 < x < haut-1) and (y == 0) :
        list_voisins = [tab[x-1][y], tab[x-1][y+1],tab[x][y+1],tab[x+1][y],tab[x+1][y+1]]
        
    if (0 < x < haut-1) and (y == larg-1) :
         list_voisins = [tab[x-1][y-1], tab[x-1][y],tab[x][y-1],tab[x+1][y-1],tab[x+1][y]]       
 
    if (x == haut-1) and (y == larg-1) :
         list_voisins = [tab[x-1][y-1], tab[x-1][y],tab[x][y-1]]  

    if (x == 0) and (y == larg-1) :
        list_voisins = [tab[x][y-1],tab[x+1][y-1],tab[x+1][y]]

    if (x == 0) and (y == 0) :
        list_voisins = [tab[x][y+1],tab[x+1][y],tab[x+1][y+1]]

        
    if (x==haut-1) and (y == 0) :
        list_voisins = [ tab[x-1][y], tab[x-1][y+1],tab[x][y+1]]
   

    count = list_voisins.count(symb)
    return count




def count_N(tab, x, y):
    while x>0:
        x -= 1
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_S(tab, x, y):
    while x<haut-1:
        x += 1
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_E(tab, x, y):
    while y<larg-1:
        y += 1
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_W(tab, x, y):
    while y>0:
        y -= 1
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0


def count_SE(tab, x, y):
    while y < larg-1 and x < haut-1:
        x += 1
        y += 1
        
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_SW(tab, x, y):
    while y > 0 and x < haut-1:
        x += 1
        y -= 1
        
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_NW(tab, x, y):
    while y > 0 and x >0:
        x -= 1
        y -= 1
        
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_NE(tab, x, y):
    while y < larg-1 and x >0:
        x -= 1
        y += 1
        
        if tab[x][y] == '#':
            return 1
        if tab[x][y] == 'L':
            return 0
    return 0

def count_symbol2(tab, x, y):
    return count_S(tab, x, y) + count_N(tab, x, y) +count_E(tab, x, y) +count_W(tab, x, y) +count_SE(tab, x, y) +count_SW(tab, x, y) +count_NE(tab, x, y) +count_NW(tab, x, y)


def maj_tab(tab):
    new_tab =[[0]*larg for x in range(haut)] 
    for x in range(haut):
        for y in range(larg):
            if tab[x][y] == 'L' and count_symbol2(tab,x,y)==0:
                new_tab[x][y] = '#'
            elif tab[x][y] == '#' and count_symbol2(tab,x,y) >= 5:
                new_tab[x][y] = 'L'
            else :
                new_tab[x][y] = tab[x][y]
    return new_tab

def are_equal(tab1,tab2):
    for x in range(haut):
        for y in range(larg):
            if tab1[x][y] != tab2[x][y]:
                return False
    return True

def solution1(tab):
    new_tab = maj_tab(tab)
    i = 1
    while not are_equal(new_tab, tab):
        #print(new_tab)
        tab = deepcopy(new_tab)
        new_tab = maj_tab(tab)
        i +=1
    return comptage(new_tab, '#')


def comptage(tab, symb):
    i = 0
    for x in range(haut):
        for y in range(larg):
            if tab[x][y] == symb:
                i +=1
    return i

print(solution1(tab))

