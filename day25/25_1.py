card_pk = 16616892
door_pk = 14505727

def calcul_ek(sn, loop):
    pv = 20201227
    return sn**loop % pv

pv = 20201227
# loop = 0
# val = 1
# while val != card_pk:
#     val = val*7 % pv
#     loop += 1

n = 16243648
val = 1
# n = 8
# val = 1
for i in range(n):
    val = val*14505727 % pv
print(val)