
raw_data = open("input.txt").read().split('\n')
#raw_data = open("input_test.txt").read().split('\n')


d = {}
pos = {}

# tribute to frfaure32, clever comme never
d['w'] = lambda z : z + complex(-2,0)
d['e'] = lambda z : z + complex(2,0)
d['ne'] = lambda z : z + complex(1,1)
d['nw'] = lambda z : z + complex(-1,1)
d['sw'] = lambda z : z + complex(-1,-1)
d['se'] = lambda z : z + complex(1,-1)

def update_pos(pos, z):
    if z not in pos:
        pos[z] = 1
    else :
        pos[z] = (pos[z] + 1) % 2

def parcours_line(line, pos):
    z = complex(0,0)
    
    while len(line) != 0:
        if line[0] == 'e':
            z = d['e'](z)
            line = line[1:]
        elif line[0] == 'w':
            z = d['w'](z)
            line = line[1:]        
        elif line[0:2] == 'ne':
            z = d['ne'](z)
            line = line[2:]
        elif line[0:2] == 'nw':
            z = d['nw'](z)
            line = line[2:]
        elif line[0:2] == 'se':
            z = d['se'](z)
            line = line[2:]
        elif line[0:2] == 'sw':
            z = d['sw'](z)
            line = line[2:]
    update_pos(pos, z)

for line in raw_data:
    parcours_line(line, pos)

def nb_voisins(z):
    v_w = z + complex(-2,0)
    v_e = z + complex(2,0)
    v_ne =  z + complex(1,1)
    v_nw =  z + complex(-1,1)
    v_sw = z + complex(-1,-1)
    v_se = z + complex(1,-1)
    s = 0
    for v in (v_w, v_e, v_ne, v_nw, v_sw, v_se):
        if v in pos :
            s += pos[v]
    return s 


def cycle(pos):
    temp_z = []
    for z in pos :
        v_w = z + complex(-2,0)
        v_e = z + complex(2,0)
        v_ne =  z + complex(1,1)
        v_nw =  z + complex(-1,1)
        v_sw = z + complex(-1,-1)
        v_se = z + complex(1,-1)
        for v in (v_w, v_e, v_ne, v_nw, v_sw, v_se):
            if v not in pos :
                temp_z.append(v)
    
    for z in temp_z:
        pos[z] = 0
    
    pos_cp = pos.copy()
    for z in pos_cp:
        n = nb_voisins(z)
        if pos[z] == 1 and (n == 0 or n > 2):
            pos_cp[z] = 0
        elif pos[z] == 0 and n == 2:
            pos_cp[z] = 1
        else :
            pos_cp[z] = pos[z]
    
    pos = pos_cp.copy()
    return pos


def nb_black(pos):
    return sum(k for k in pos.values())
   
for k in range(100):
    pos = cycle(pos)
print(k+1, nb_black(pos))