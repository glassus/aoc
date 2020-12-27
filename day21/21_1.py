raw_data = open("input.txt").read().split('\n')[:-1]
#raw_data = open("input_test.txt").read().split('\n')[:-1]

line ='mxmxvkd kfcds sqjhc nhms (contains dairy, fish)'

d = {}

def extract(line):
    p = line.split(' (contains')
    ingred = p[0].split(' ')
    p = p[1][1:-1]
    allerg = p.split(', ')
    return ingred, allerg

for line in raw_data:
    ingred, allerg = extract(line)
    for al in allerg :
        if al not in d :
            d[al] = set(ingred)
        else :
            d[al] = d[al].intersection(set(ingred))

found = []
def tour():
    for al in d :
        if len(d[al]) == 1 and d[al] not in found :
            found.append(d[al])
    for al in d :
        if len(d[al]) > 1 :
            for ing in found :
                d[al]= d[al] - ing
        
while len(found) != 8 :
    tour()
    
print(d)
tot_ing = []
val = list(d.values())
for h in val :
    for k in h :
        tot_ing.append(k)


def compte_ing(line):
    s = 0
    lst = extract(line)[0]
    for mot in tot_ing:
        s += lst.count(mot)
    return len(lst) - s

s = 0
for line in raw_data:
    s += compte_ing(line)
    