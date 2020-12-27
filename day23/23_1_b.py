data = '792845136'

lst = [int(k) for k in data]
n = len(lst)

d = {}
for k in range(len(lst)) :
    d[lst[k]] = k

i = lst[0]
def move(d):
    global i
    #print(lst)
    curr_cup = i
    #print("curr", curr_cup)
    cup1 = lst[(i + 1) % n]
    cup2 = lst[(i + 2) % n]
    cup3 = lst[(i + 3) % n]
    #print('pick up :', cup1, cup2, cup3)
    lst.remove(cup1)
    lst.remove(cup2)
    lst.remove(cup3)
    
    dest_cup = curr_cup - 1
    if dest_cup < min(lst):
        dest_cup = max(lst)
    while dest_cup in (cup1, cup2, cup3):
        dest_cup -= 1
        if dest_cup < min(lst):
            dest_cup = max(lst)
    #print('destination :', dest_cup)
    
    i_dest = lst.index(dest_cup)
    lst.insert((i_dest + 1)%n, cup1)
    lst.insert((i_dest + 2)%n, cup2)   
    lst.insert((i_dest + 3)%n, cup3)
    
    i = lst.index(curr_cup)
    i = (i+1)%n
    
    
for _ in range(100):
    #print("-------")
    #print("move ", _+1)
    move(lst)
    
i1 = lst.index(1)
final = lst[i1+1:] + lst[:i1]
mot = "".join([str(k) for k in final])
print(mot)