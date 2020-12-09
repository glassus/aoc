from copy import deepcopy
import time
c =time.time()

raw_lines = open("input.txt").read().split('\n')[:-1]
#raw_lines = open("input_test.txt").read().split('\n')[:-1]

def line_to_list(line):
    lst = [0,0,0]
    mots = line.split(' ')
    lst[0] = mots[0]
    if mots[1][0] == '+':
        lst[1] = int(mots[1][1:])
    else:
        lst[1] = -int(mots[1][1:])
    return lst

inst = [line_to_list(line) for line in raw_lines]


def exec(inst):

    i = 0
    val_acc = 0
    while i < len(inst):
        if inst[i][2] == 1:
            return [0, val_acc] # infinite loop
        instruction = inst[i][0]
        inst[i][2] = 1
        if instruction == 'nop':
            pass
        if instruction == 'acc':
            val_acc += inst[i][1]
        if instruction == 'jmp':
            i += inst[i][1]
        else:
            i += 1
    return [1, val_acc] # eof

def parcours(inst):
    for i in range(len(inst)):
        inst_cp = deepcopy(inst)
        if inst[i][0] == 'nop':
            inst_cp[i][0] = 'jmp'
            res = exec(inst_cp)
            if res[0] == 1:
                return res[1]
        if inst[i][0] == 'jmp':
            inst_cp[i][0] = 'nop'
            #print(i, 'jmp to nop')
            res = exec(inst_cp)
            if res[0] == 1:
                return res[1]


print(parcours(inst))
print(time.time()-c)
    