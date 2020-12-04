l = open("input.txt").read().split('\n\n')[:-1]


def create_dict_from_many_lines(list_of_lines):
    dct = {}
    for line in list_of_lines :
        temp_list = line.split(" ")
        for k in temp_list :
            decomp = k.split(":")
            dct[decomp[0]] = decomp[1]
    return dct

lst = []
for lines in l :
    list_of_lines = lines.split('\n')  
    lst.append(create_dict_from_many_lines(list_of_lines))


def valid1(passport) :
    champs_requis = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for champ in champs_requis :
        if champ not in passport.keys() :
            return False
    return True


def valid2(passport) :
    if not valid1(passport):
        return False
    
    if not 1920 <= int(passport['byr']) <= 2002 :
        return False

    if not 2010 <= int(passport['iyr']) <= 2020 :
        return False

    if not 2020 <= int(passport['eyr']) <= 2030 :
        return False
    
    if passport['hgt'][-2:] not in ["cm", "in"] :
        return False
    if passport['hgt'][-2:] == "cm" :
        if  not 150 <= int(passport['hgt'][:-2]) <= 193 :
            return False
    if passport['hgt'][-2:] == "in" :
        if  not 59 <= int(passport['hgt'][:-2]) <= 76 :
            return False
        
        
    if not passport['hcl'][0] == "#" :
        return False
    for car in passport['hcl'][1:] :
        if car not in "0123456789abcdef" :
            return False
        
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] :
        return False
    
    if len(passport['pid']) != 9 :
        return False
    for c in passport['pid'] :
        if c not in "0123456789" :
            return False

    return True



tot = 0
for passport in lst :
    if valid2(passport) :
        tot += 1

print(tot)
