import re

raw_data = open("input.txt").read().split('\n\n')
#raw_data = open("input_test.txt").read().split('\n\n')

raw_rules = raw_data[0].split('\n')
raw_strings = raw_data[1].split('\n')[:-1]

pos_a = '116'
pos_b = '119'

#pos_a = '4'
#pos_b = '5'


dic = {}
for line in raw_rules:
    tmp = line.split(': ')
    cle = tmp[0]
    vals = tmp[1].split(' | ')
    for i  in range(len(vals)):
        vals[i] = vals[i].split(' ')
    dic[cle] = vals
    dic[pos_a] = 'a'
    dic[pos_b] = 'b'

            
           
def generate_id(n):
    if n == pos_a :
        return "a"
    elif n == pos_b :
        return "b"
    else :
        return generate_lst(dic[n])

def generate_lst(lst):
    if len(lst) == 1:
        return "".join(generate_id(k) for k in lst[0])
    if len(lst) == 2:
        s = '(' + generate_lst([lst[0]]) + '|' + generate_lst([lst[1]]) + ')'
        return s
    
motif = generate_lst(dic['0'])

p = re.compile(motif)

t = 0
for line in raw_strings:
    k = p.match(line)
    if k is not None :
        if k.end() == len(line):
            t += 1
print(t)
            


