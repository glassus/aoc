raw_data = open("input.txt").read().split('\n\n')
raw_data = open("input_test.txt").read().split('\n\n')

rp1 = raw_data[0].split('\n')[1:]
rp2 = raw_data[1].split('\n')[1:-1]


p1 = [int(v) for v in rp1]
p2 = [int(v) for v in rp2]
mem_round = []
k = 0
while len(p1) * len(p2) != 0:
    k += 1
    #print("--- round", k)
    #print("p1 : ", p1)
    #print("p2 : ", p2)
    #print('--------')
    
    v1 = p1.pop(0)
    v2 = p2.pop(0)
    
    if v1 > v2:
        p1.append(v1)
        p1.append(v2)
    else :
        p2.append(v2)
        p2.append(v1)
    
    id_round = ''.join(str(k) for k in p1) + '/' + ''.join(str(k) for k in p2)
    mem_round.append(id_round)

def score(p):
    s = 0
    p.reverse()
    for k in range(len(p)):
        s += (k+1)*p[k]
    return s



if len(p1) > len(p2):
    print(score(p1))
else :
    print(score(p2))