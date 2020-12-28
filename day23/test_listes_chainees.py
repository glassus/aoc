data = '792845136'
#lst = [int(k) for k in data]

t_lst = [int(k) for k in data]
lst = t_lst + [int(k) for k in range(10, 10**6 +1)]

n = len(lst)
v_max = n
v_min = 1


class Nb:
    def __init__(self, val):
        self.val = val
        self.suiv = None

tot = []
for k in lst:
    tot.append(Nb(k))
for i in range(n):
    tot[i].suiv = tot[(i+1)%n]

curr = tot[0]

for k in range(10**7):
    cup1 = curr.suiv
    cup2 = cup1.suiv
    cup3 = cup2.suiv

    curr.suiv = cup3.suiv
    cup3.suiv = None

    dest_val = curr.val - 1
    if dest_val == 0:
        dest_val = v_max
    while dest_val in (cup1.val, cup2.val, cup3.val):
        dest_val -= 1
        if dest_val == 0:
            dest_val = v_max
            
    # recherche de dest_val
    if dest_val <= 9 :
        i = data.index(str(dest_val))
    else :
        i = dest_val -1
    
    
#     
#     for i in range(n):
#         if tot[i].val == dest_val:
#             break




    tot_ins = tot[i]
    tot_nxt = tot_ins.suiv
    tot_ins.suiv = cup1
    cup3.suiv = tot_nxt

    curr = curr.suiv


i1 = data.index('1')
k1 = tot[i1].suiv.val
k2 = tot[i1].suiv.suiv.val
print(k1*k2)


# for _ in range(9):
#     print(curr.val, end = '')
#     curr = curr.suiv

#     dest_cup = curr_cup - 1
#     if dest_cup == 0:
#         dest_cup = 10**6
#     while dest_cup in (cup1, cup2, cup3):
#         dest_cup -= 1
#         if dest_cup == 0:
#             dest_cup = 10**6
