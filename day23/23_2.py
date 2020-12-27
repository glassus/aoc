data = '792845136'
N = 10**6
lst = [int(k) for k in data]
for m in range(10, N+1):
    lst.append(m)
n = len(lst)

i = 0
def move(lst):
    global i
    #print(lst)
    curr_cup = lst[i]
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
    
d = 1   
for k in range(10**7):
    if k == 10**d:
        print(k)
        d += 1
    #print("-------")
    #print("move ", _+1)
    move(lst)
    
i1 = lst.index(1)
mot1 = lst[i1+1]
mot2 = lst[i1+2]
print(mot1*mot2)