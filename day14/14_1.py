
raw_data = open("input.txt").read().split('\n')[:-1]
#raw_data = open("input_test.txt").read().split('\n')[:-1]

mem = {}


def get_mask(line):
    return list(line[7:])

def get_value(n):
    b = bin(n)[2:]
    npad = 36 - len(b)
    return list('0'*npad + b)

def bitmask(value, mask):
    result = [0]*36
    for k in range(36):
        if mask[k] != 'X':
            result[k] = int(mask[k])
        else :
            result[k] = int(value[k])
    string_result = ''.join([str(n) for n in result])
    
    return int(string_result,2)

def parse_mem(line):
    chunk = line.split(' = ')
    val = int(chunk[1])
    addr_mem = int(chunk[0][4:-1])
    return addr_mem, val

def treat_line(line):
    global mem, mask
    if "mask" in line:
        mask = get_mask(line)
    else :
        ad_mem, val = parse_mem(line)
        mem[ad_mem] = bitmask(get_value(val), mask)
    
for line in raw_data:
    treat_line(line)

sol = sum([mem[k] for k in mem])
