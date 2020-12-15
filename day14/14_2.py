from time import time
from copy import deepcopy
c=time()
raw_data = open("input.txt").read().split('\n')[:-1]
#raw_data = open("input_test2.txt").read().split('\n')[:-1]

mem = {}


def get_mask(line):
    return list(line[7:])

def get_addr(n):
    b = bin(n)[2:]
    npad = 36 - len(b)
    return list('0'*npad + b)

def bitmask(addr, mask):
    result = [0]*36
    for k in range(36):
        if mask[k] == '0':
            result[k] = addr[k]
        if mask[k] == '1':
            result[k] = '1'
        if mask[k] == 'X':
            result[k] = 'X'
    #string_result = ''.join([n for n in result])
    return result

def parse_mem(line):
    chunk = line.split(' = ')
    val = int(chunk[1])
    addr_mem = int(chunk[0][4:-1])
    return addr_mem, val

def generate_from_floating_list(f_list, val):
    global mem
    nb = f_list.count('X')
    lst_bin = []
    for k in range(2**nb):
        b = bin(k)[2:]
        s = '0'*(nb-len(b))+b
        lst_bin.append(s)
        
    #print(nb)
    #print(lst_bin)
    for k in range(len(lst_bin)):
        work_list = deepcopy(f_list)
        word = lst_bin[k]
        h = 0
        for i in range(len(f_list)):
            if f_list[i] == 'X':
                work_list[i] = word[h]
                h += 1
        string_result = ''.join([n for n in work_list])
        new_place = int(string_result,2)
        mem[new_place] = val

def treat_line(line):
    global mem, mask
    if "mask" in line:
        mask = get_mask(line)
    else :
        ad_mem, val = parse_mem(line)
        floating_list = bitmask(get_addr(ad_mem), mask)
        #print(floating_list)
        generate_from_floating_list(floating_list, val)




for line in raw_data:
    treat_line(line)
    #print('---------')
#
sol = sum([mem[k] for k in mem])
print(sol)
print(time()-c)