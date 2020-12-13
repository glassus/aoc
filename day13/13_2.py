from arithm import *
raw_data = open("input.txt").read().split('\n')
raw_data = open("input_test.txt").read().split('\n')


bus_ids = raw_data[1].split(',')

bus_delay = {}
for k in range(len(bus_ids)):
    if bus_ids[k] != 'x':
        bus_delay[int(bus_ids[k])] = k

bus = list(bus_delay.keys())

N = 1
for k in bus:
    N *= k

somme = 0
for ni in bus:
    nic = N // ni
    vi = euclid(ni, nic)[1]
    ei = vi * nic
    somme += (ni - bus_delay[ni]) % ni * ei
print(somme % N)




