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
    
    test = 0
    if (ch[inf-1] == car) ^ (ch[sup-1] == car) :
        test = 1
    
    return test
 
assert valid('1-3 a: abcde') ==  True
assert valid('1-3 b: cdefg') ==  False
assert valid('2-9 c: ccccccccc') ==  False
 

tot = 0
for s in l :
    tot += valid(s)
print(tot)
