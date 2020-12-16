
raw_data = open("input.txt").read().split('\n\n')

#raw_data = open("input_test.txt").read().split('\n\n')
#raw_data = open("input_test2.txt").read().split('\n\n')


fields = raw_data[0].split('\n')
yours = raw_data[1].split('\n')
nearby = raw_data[2].split('\n')[1:-1]


def parse_fields(line):
    name, vals = line.split(': ')
    vals = vals.split(' or ')
    vals0 = vals[0].split('-')
    m1 = int(vals0[0])
    m2 = int(vals0[1])
    vals1 = vals[1].split('-')
    m3 = int(vals1[0])
    m4 = int(vals1[1])
    return name, m1, m2, m3, m4

test = {}
for line in fields:
    name, m1, m2, m3, m4 = parse_fields(line)
    test[name] = lambda x, m_1=m1, m_2=m2, m_3=m3, m_4=m4 : (m_1 <= x <= m_2) or (m_3 <= x <= m_4)
    
    
def parse_nearby(line):
    raw = line.split(',')
    val = [int(k) for k in raw]
    return val

def test_total(n):
    for test_key in test:
        if test[test_key](n) == True :
            return True
    return False


invalid = []
for line in nearby:
    val = parse_nearby(line)
    for k in val :
        if test_total(k) == False:
            invalid.append(k)

valid_nearby = [parse_nearby(line) for line in nearby \
                if len(set(invalid).intersection(set(parse_nearby(line) ))) == 0]

find_col = [[] for k in range(20)]
for col in range(len(valid_nearby[0])):
    champs_possibles = [ftest for ftest in test]
    for voisins in valid_nearby:
        champs = [ftest for ftest in test if test[ftest](voisins[col]) == True]
        champs_possibles = list(set(champs_possibles).intersection(set(champs)))
    find_col[col] = champs_possibles

#print(find_col)
traited = []
fixed = 'arrival platform'
while len(traited) != 20:
    print(fixed)
    for choix in find_col:
        if len(choix) > 1 and fixed in choix:
            choix.remove(fixed)
            #print("removed")
    traited.append(fixed)
    for choix in find_col:
        if len(choix) == 1 and choix[0] not in traited :
            fixed = choix[0]
            break

for k in range(20):
    print(k, find_col[k])
    
val_tick = yours[1].split(',')

p = 1
for k in range(20):
    if 'departure' in find_col[k][0]:
        p *= int(val_tick[k])
print(p)
