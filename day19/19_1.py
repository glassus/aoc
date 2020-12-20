raw_data = open("input.txt").read().split('\n\n')
#raw_data = open("input_test.txt").read().split('\n\n')

raw_rules = raw_data[0].split('\n')
raw_strings = raw_data[1].split('\n')[:-1]

pos_a = '116'
pos_b = '119'

#pos_a = '4'
#pos_b = '5'


dic_rules = {}
for line in raw_rules:
    tmp = line.split(': ')
    cle = tmp[0]
    vals = tmp[1].split(' | ')
    for i  in range(len(vals)):
        vals[i] = vals[i].split(' ')
    dic_rules[cle] = vals
    dic_rules[pos_a] = 'a'
    dic_rules[pos_b] = 'b'


def test_nb(rule_nb, string):
    
    if rule_nb in (pos_a, pos_b) :
        #print("test", rule_nb, string)

        if string is None or dic_rules[rule_nb] not in string :
            #print("False")
            return (False, None)
        i = string.index(dic_rules[rule_nb])
        new_string = string[i+1:]
        #print("validé new_string :", new_string)
        if new_string == '':
            return (False, None)
        return (True, new_string)
        
    
    else :
        parcours = dic_rules[rule_nb]
        return test_parcours(parcours, string)
    
def test_parcours(parcours, string):
    #print("go to :", parcours)
    global new_string
    if len(parcours) == 1:
        if len(parcours[0]) == 1 :
            return test_nb(parcours[0][0], string)
        if len(parcours[0]) == 2 :
            rep, new_string = test_nb(parcours[0][0], string)
            if rep == False or new_string == '':
                return (False, None)
            else :
                return test_nb(parcours[0][1], new_string)
            
    if len(parcours) == 2:
        if len(parcours[0]) == 1 :
            #rep1, new_string1 = test_nb(parcours[0][0], string)
            rep1, new_string1 = test_parcours([parcours[0]], string) 
            #rep2, new_string2 = test_nb(parcours[1][0], string)
            rep2, new_string2 = test_parcours([parcours[1]], string)
            rep_finale = (rep1 or rep2)
            return (rep_finale, string)
        
        if len(parcours[0]) == 2 :
            rep1, new_string1 = test_parcours([parcours[0]], string)      
            rep2, new_string2 = test_parcours([parcours[1]], string) 
            rep_finale = (rep1 or rep2)
            return (rep_finale, string)
 
 
 
s = 0
for line in raw_strings:
    if test_nb('0',line)[0] == True :
        s += 1
print(s)
#print(test_nb('0', "jjjkkbaba"))
