import time
c = time.time()
raw_nb = open("input.txt").read().split('\n')[:-1]
#raw_nb= open("input_test2.txt").read().split('\n')

print(len(raw_nb))
print(len(set(raw_nb)))



lst = [0] + [int(k) for k in raw_nb]
m = max(lst)+3
lst.append(m)
lst.sort()

#print(lst)
# diff = [0 for k in range(4)]
# 
# for i in range(len(lst)-1):
#     delta = lst[i+1]-lst[i]
#     diff[delta] += 1
# 
# diff[3] += 1
# print(diff)
# print(diff[1]*diff[3])

dict_bifurcations = {}
for k in range(len(lst)-2):
    val_possibles = []
    i = k + 2
    while (lst[i] <= lst[k] + 3) and  i < len(lst)-1:
        val_possibles.append(i)
        i += 1
    if len(val_possibles) >= 1 :
        dict_bifurcations[k] = val_possibles
print(dict_bifurcations)

M = max(dict_bifurcations)
#print(M)

tot = 0
def parcours(i):
    global tot
    #print(lst[i])
    if i in dict_bifurcations :
        #tot += len(dict_bifurcations[i])-1
        
        #print("bif en ",i, "détectée")
        for k in dict_bifurcations[i]:
            parcours(k)
    elif i > M:
        tot += 1
        if tot % 10**7 == 0:
            print(tot)
        #print("FINI")
        return None
    
    parcours(i+1)
    return tot 
        
    

#print(parcours(0)) -> code récursif beaucoup trop long

# fin de l'énigme à la main en observant le dict_bifurcations et en multipliant les différents facteurs de chaque cluster


