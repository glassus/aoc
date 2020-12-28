raw_data = open("input.txt").read().split('\n\n')
#raw_data = open("input_test.txt").read().split('\n\n')

rp1 = raw_data[0].split('\n')[1:]
rp2 = raw_data[1].split('\n')[1:-1]


p1 = [int(v) for v in rp1]
p2 = [int(v) for v in rp2]


def game(p1, p2):
    has_winner = False
    same_again = False
    mem_game = []
    k = 0
    #print("new game !!!")
    
    while has_winner ==  False:
        
        id_round = ''.join(str(k) for k in p1) + '/' + ''.join(str(k) for k in p2)
        if id_round in mem_game :
            return ("p1", None)
        else :
            mem_game.append(id_round)
        k += 1
        #print("--- round", k)
        #print("p1 : ", p1)
        #print("p2 : ", p2)
        #print('--------')
        
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        
        if v1 <= len(p1) and v2 <= len(p2):
            #print("recursive combat")
            new_game = game(p1[:v1], p2[:v2])
            if new_game[0] == 'p1':
                p1.append(v1)
                p1.append(v2)
            else :
                p2.append(v2)
                p2.append(v1)
        else :
        
            if v1 > v2:
                p1.append(v1)
                p1.append(v2)
            else :
                p2.append(v2)
                p2.append(v1)
            
        if p1 == [] or p2 == []:
                has_winner = True
    
    if p1 == []:
        return ("p2", p2)
    else :
        return ("p1", p1)


def score(p):
    s = 0
    p.reverse()
    for k in range(len(p)):
        s += (k+1)*p[k]
    return s


jeu = game(p1, p2)
print("vainqueur : ", jeu[0])
print("score : ", score(jeu[1]))