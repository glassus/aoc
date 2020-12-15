lst = [0,3,6]
#lst = [2,1,10,11,0,6]
n = 2020
    
def search_back(lst):
    val = lst[-1]
    for k in range(len(lst)-2, -1, -1):
        if lst[k] == val:
            return len(lst) - k - 1
    return 0

for _ in range(n-len(lst)):
    lst.append(search_back(lst))
    #print(lst)

print(lst[-1])