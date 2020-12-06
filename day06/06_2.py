groupes_raw = open("input.txt").read().split('\n\n')
groupes = [g.split('\n') for g in groupes_raw]


def convert_strings_to_sets(groupes):
    groupes_sets_lists = []
    for groupe in groupes:
        groupe_set_list = []
        for g in groupe:
            groupe_set_list.append(set(g))
        groupes_sets_lists.append(groupe_set_list)
    return groupes_sets_lists


def common_answers_for_one_group(groupe):
    answers = groupe[0]
    for s in groupe:
        answers = answers.intersection(s)
    return answers


def common_answers_for_each_group(groupes_sets_lists):
    common_answers = []
    for groupe in groupes_sets_lists:
        common_answers.append(common_answers_for_one_group(groupe))
    return common_answers


g_sets = convert_strings_to_sets(groupes)

sol = 0
common_sets = common_answers_for_each_group(g_sets)

for common_set in common_sets:
    sol += len(common_set)
print(sol)