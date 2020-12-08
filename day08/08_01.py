raw_lines = open("input.txt").read().split('\n')[:-1]
#raw_lines = open("input_test.txt").read().split('\n')[:-1]

ex = 'nop -453'
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
    while inst[i][2] == 0:
        instruction = inst[i][0]
        inst[i][2] = 2
        if instruction == 'nop':
            pass
        if instruction == 'acc':
            val_acc += inst[i][1]
        if instruction == 'jmp':
            i += inst[i][1]
        else:
            i += 1
    

print(val_acc)
        
    
    