groupes_raw = open("input.txt").read().split('\n\n')
groupes = [g.split('\n') for g in groupes_raw]


def convert_list_to_set(groupe):
    total_string = "".join(part for part in groupe)
    groupe_set = set(total_string)
    return groupe_set

def nb_answers_yes(groupe):
    return len(convert_list_to_set(groupe))


sol = 0
for groupe in groupes:
 sol += nb_answers_yes(groupe)
print(sol)
