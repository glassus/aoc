lst = open("input.txt").read().split('\n')[:-1]

for k in lst :
    if str(2020-int(k)) in lst :
        print(int(k)*(2020-int(k)))