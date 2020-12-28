import time
c = time.time()
data = '389125467'
data = '792845136'

t_lst = [int(k) for k in data]
lst = t_lst + [int(k) for k in range(10, 10**6 +1)]
n = len(lst)

i = 0
def move(lst):
    #test = lst.copy()
    global i
    #print(lst)
    curr_cup = lst[i]
    #print("curr", curr_cup)
    cup1 = lst.pop((i + 1) % n)
    cup2 = lst.pop((i + 1) % n)
    cup3 = lst.pop((i + 1) % n)
    #print('pick up :', cup1, cup2, cup3)
    #lst.remove(cup1)
    #lst.remove(cup2)
    #lst.remove(cup3)
    
    dest_cup = curr_cup - 1
    if dest_cup == 0:
        dest_cup = 10**6
    while dest_cup in (cup1, cup2, cup3):
        dest_cup -= 1
        if dest_cup == 0:
            dest_cup = 10**6
    #print('destination :', dest_cup)
    
    i_dest = lst.index(dest_cup)
    lst.insert((i_dest + 1)%n, cup1)
    lst.insert((i_dest + 2)%n, cup2)   
    lst.insert((i_dest + 3)%n, cup3)
    
    i = lst.index(curr_cup)
    i = (i+1)%n
    
    
for _ in range(10**3):
    #print("-------")
    #print("move ", _+1)
    #print(lst)
    move(lst)
    
i1 = lst.index(1)
final = lst[(i1+1) %n] * lst[(i1+2) % n]

print(final)
print(time.time()-c)
#bf 19 secondes pour 10**7