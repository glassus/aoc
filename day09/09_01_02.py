import time
c = time.time()
raw_nb = open("input.txt").read().split('\n')[:-1]
#raw_nb= open("input_test.txt").read().split('\n')[:-1]


lst_nb = [int(k) for k in raw_nb]

if len(raw_nb) > 50:
    n = 25
    N = 3199139634
    iN = 683
else :
    n = 5
    N = 127
    iN = 14


def recherche_somme(candidats, goal):
    for k in candidats :
        if (goal - k) in candidats :
            return True
    return False


def test_glissant(i):
    candidats = lst_nb[i-n:i]
    return recherche_somme(candidats, lst_nb[i])

def intrus():
    for i in range(n, len(lst_nb)):
        if test_glissant(i) == False :
            return lst_nb[i], i

def recherche_somme():
    for i in range(iN):
        somme = 0
        for k in range(iN-i):
            somme += lst_nb[i+k]
            if somme > N:
                break
            if somme == N:
                vals = lst_nb[i:i+k+1]
                return min(vals) + max(vals)
    return None

#part 1
#print(intrus())

print(recherche_somme())
print(time.time()-c)