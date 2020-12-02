l = open("input.txt").read().split('\n')[:-1]

def sep(s):
    t = s.split(" ")
    bornes = t[0].split("-")
    inf = int(bornes[0])
    sup = int(bornes[1])
    car = t[1][0]
    ch = t[2]
    return inf, sup, car, ch

def valid(s):
    ans = sep(s)
    inf = ans[0]
    sup = ans[1]
    car = ans[2]
    ch = ans[3]
    if inf <= ch.count(car) <= sup :
        return 1
    else :
        return 0

tot = 0
for s in l :
    tot += valid(s)
print(tot)
