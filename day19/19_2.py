import re

raw_data = open("input.txt").read().split('\n\n')

#raw_data = open("input_test_2.txt").read().split('\n\n')

raw_rules = raw_data[0].split('\n')
raw_strings = raw_data[1].split('\n')[:-1]

pos_a = '116'
pos_b = '119'

#pos_a = '1'
#pos_b = '14'


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
    elif n == '42':
        return '[' + generate_lst(dic[n]) + ']'
    elif n == '31':
        return '{' + generate_lst(dic[n]) + '}'
    else :
        return generate_lst(dic[n])

def generate_lst(lst):
    if len(lst) == 1:
        if lst == [['42','31']] and False:
            return "{" + "".join(generate_id(k) for k in lst[0]) + "}"
        else :
            return "".join(generate_id(k) for k in lst[0])
    if len(lst) == 2:
        s = '(' + generate_lst([lst[0]]) + '|' + generate_lst([lst[1]]) + ')'
        return s
    
#motif = generate_lst(dic['0'])
#print(motif)

m42 = '((b(a(bb|ab)|b(a|b)(a|b))|a(bbb|a(bb|a(a|b))))b|(((aa|ab)a|bbb)b|((a|b)a|bb)aa)a)'
m31 = '(b(b(aba|baa)|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a(bab|(ba|bb)a)))'


m42 = '((a(b(b(a((a|b)(a|b)a|(ab|ba)b)|b(bba|abb))|a(((ba|bb)b|((a|b)b|ba)a)a|(bab|abb)b))|a(((b(a|b)(a|b)|a(ab|bb))a|(b(a(a|b)|ba)|a((a|b)b|ba))b)b|(((ab|bb)b|(ab|aa)a)a|(aaa|b(aa|b(a|b)))b)a))|b(a(((((a|b)b|aa)b|(aa|ba)a)a|(b(a(a|b)|ba)|a(ba|bb))b)b|((a(ab|ba)|b(aa|ba))b|((aa|ba)b|baa)a)a)|b(b(b(bbb|(ab|aa)a)|a(baa|(ab|bb)b))|a(b(baa|aaa)|a(a(ab|aa)|bbb)))))b|(a(b(a(b(a(ab|bb)|b((a|b)b|aa))|a(a(aa|ba)|b((a|b)b|aa)))|b(a(b(ab|bb)|a(a|b)(a|b))|b(baa|(ab|ba)b)))|a(a((bba|abb)b|a((a|b)b|ba)a)|b(b(b(a|b)(a|b)|a(ab|bb))|a(bab|aaa))))|b(a(a(b(a(ab|bb)|b((a|b)b|ba))|a((ab|ba)a|((a|b)b|aa)b))|b((abb|(aa|ba)a)a|((ab|aa)a|aab)b))|b(b(b(aaa|b(ba|bb))|a(b(a|b)(a|b)|a(ab|bb)))|a(b(b(ba|bb)|a(ab|aa))|a(b(ab|ba)|a(ab|bb))))))a)'
m31 = '(((a(b((bba|a(ab|aa))b|(aaa|b(ba|bb))a)|a((b(a(a|b)|ba)|aab)a|(bab|a((a|b)b|ba))b))|b(((((a|b)b|aa)b|baa)b|(a((a|b)b|aa)|bba)a)a|((bab|(aa|b(a|b))a)a|((a|b)(a|b)b|((a|b)b|ba)a)b)b))a|(((a((ba|bb)b|baa)|b((ba|bb)b|((a|b)b|ba)a))b|(((ab|bb)b|(ab|aa)a)a|(((a|b)b|ba)b|(a|b)(a|b)a)b)a)a|(b(b(bba|a(aa|b(a|b)))|a(a(ab|aa)|bbb))|a(b(((a|b)b|ba)b|aaa)|a(bbb|aaa)))b)b)b|((a(b((bbb|aaa)b|(bba|aaa)a)|a((aab|(a(a|b)|ba)a)a|((ab|ba)b|(a(a|b)|ba)a)b))|b(b((a(ab|ba)|bba)b|((ab|bb)b|bba)a)|a(aaba|b((ba|bb)a|((a|b)b|ba)b))))b|(((((ab|aa)a|(ab|ba)b)b|((ab|ba)a|(ab|aa)b)a)b|(a(aba|(a|b)(a|b)b)|b((a|b)(a|b)b|((a|b)b|ba)a))a)b|(((b(a|b)(a|b)|aaa)b|(b(ab|ba)|a(ab|bb))a)b|((a(a|b)(a|b)|baa)b|(aaa|b(aa|b(a|b)))a)a)a)a)a)'
#
#

motif = [0]*10
for i in range(1,10):
    q = str(i)
    motif[i] = m42 + '+' +  m42 + '{' + q + '}' + m31 + '{' + q + '}'


def calcul_motif(motif):
    t = 0
    p = re.compile(motif)
    for line in raw_strings:
        k = p.match(line)
        if k is not None :
            if k.end() == len(line):
                #print(line)
                t += 1
    return t

motif_val = [0]*10
for i in range(1,10):
    motif_val[i] = calcul_motif(motif[i])
    
print(sum(motif_val))


