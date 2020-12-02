l = open("input.txt").read().split('\n')[:-1]
lst = [int(k) for k in l]

for i in range(len(lst)) :
    for j in range(i+1, len(lst)) :
        for k in range(j+1, len(lst)):

            if lst[i] + lst[j] + lst[k] == 2020 :
                print(lst[i] * lst[j] * lst[k])