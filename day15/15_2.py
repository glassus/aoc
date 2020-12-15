lst = [2,1,10,11,0,6]

n = 30000000
    
d = {}

for k in range(len(lst)):
    d[lst[k]] = k

val = 0

for i in range(len(lst),n-1):
    if val in d :
        new = i - d[val]
    else :
        new = 0
    d[val] = i
    val = new

print(val)