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



def evaluate(lst):
    #print("eval : ", lst)
    val = int(lst[0])
    for i in range(1, len(lst)-1, 2):
        #print(lst[i])
        if lst[i] == '+':
            val += int(lst[i + 1])
        if lst[i] == '*':
            val *= int(lst[i + 1])
    return val

def simplify_value(line):
    #print(line)
    open_last_idx = None
    close_last_idx = None
    line_save = line
    line = line.replace('(','( ')
    line = line.replace(')',' )')
    lst = line.split(' ')
    #print(lst)
#     for i in range(len(lst)):
#         if lst[i] == '(':
#             open_last_idx = i
#         if lst[i] == ')':
#             close_last_idx = i
    open_last_idx, close_last_idx = index_search(lst)      
    if open_last_idx is None:
        return (0, line_save)
    #print(open_last_idx, close_last_idx)
    exp = lst[open_last_idx + 1 : close_last_idx ]
    #print("exp", exp)
    str_remplacement = str(evaluate(exp))
    lst = lst[:open_last_idx] + [str_remplacement] + lst[close_last_idx+1:]
    #print(lst)
    new_line = "".join(car for car in lst)
    new_line = new_line.replace('+',' + ')
    new_line = new_line.replace('*',' * ')
    #print(new_line)
    return (1, new_line)

def resolution(line):
    line = simplify_value(line)
    while line[0] != 0 :
        line = simplify_value(line[1])
        #print(line)
    line = line[1]
    #print('env : ', line)
    line = line.split(' ')
    return evaluate(line)


somme = sum([resolution(line) for line in raw_data])
print(somme)