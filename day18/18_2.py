from math import prod

raw_data = open("input.txt").read().split('\n')[:-1]
#raw_data = open("input_test.txt").read().split('\n')

line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

def index_search(lst):
    for i in range(len(lst)):
        i_open = i
        if lst[i] == '(':
            for j in range(i+1, len(lst)):
                if lst[j] == '(':
                    i_open = j
                if lst[j] == ')':
                    return i_open,j
    return None, None


#lst =['1','+','2','*','3','+','4','*','5','+','6']
def evaluate(lst):
    while lst.count('+') != 0:
        i = lst.index('+')
        val = int(lst[i-1]) + int(lst[i+1])
        lst = lst[:i-1] + [str(val)] + lst[i+2:]
    
    return prod([int(k) for k in lst if k != '*'])



def simplify_value(line):
    
    open_last_idx = None
    close_last_idx = None
    line_save = line
    line = line.replace('(','( ')
    line = line.replace(')',' )')
    lst = line.split(' ')

    open_last_idx, close_last_idx = index_search(lst)      
    if open_last_idx is None:
        return (0, line_save)
    
    exp = lst[open_last_idx + 1 : close_last_idx ]
    
    str_remplacement = str(evaluate(exp))
    lst = lst[:open_last_idx] + [str_remplacement] + lst[close_last_idx + 1:]
    
    new_line = "".join(car for car in lst)
    new_line = new_line.replace('+',' + ')
    new_line = new_line.replace('*',' * ')
    
    return (1, new_line)

def resolution(line):
    line = simplify_value(line)
    while line[0] != 0 :
        line = simplify_value(line[1])
        
    line = line[1]
    
    line = line.split(' ')
    return evaluate(line)


somme = sum([resolution(line) for line in raw_data])
print(somme)