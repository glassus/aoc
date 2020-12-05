l = open("input.txt").read().split('\n')[:-1]


def F_L_action(bornes):
    new_max = (bornes[0] + bornes[1]) // 2
    return (bornes[0], new_max)


def B_R_action(bornes):
    new_min = 1 + (bornes[0] + bornes[1]) // 2
    return (new_min, bornes[1])


def determine_row(chaine_row):
    bornes = (0, 127)
    for lettre in chaine_row:
        if lettre == "F":
            bornes = F_L_action(bornes)
        if lettre == "B":
            bornes = B_R_action(bornes)
    return bornes[0]


def determine_column(chaine_column):
    bornes = (0, 7)
    for lettre in chaine_column:
        if lettre == "L":
            bornes = F_L_action(bornes)
        if lettre == "R":
            bornes = B_R_action(bornes)
    return bornes[0]


def seat_id(seat_string):
    chaine_row = seat_string[:7]
    chaine_column = seat_string[7:]
    row = determine_row(chaine_row)
    column = determine_column(chaine_column)
    s_id = row * 8 + column
    return s_id


assert seat_id("BFFFBBFRRR") == 567
assert seat_id("FFFBBBFRRR") == 119
assert seat_id("BBFFBBFRLL") == 820

# max_id = 0
# for boarding_pass in l :
#     max_id = max(max_id, seat_id(boarding_pass))
# print(max_id)

list_id = []
for boading_pass in l:
    list_id.append(seat_id(boading_pass))
list_id.sort()

for k in range(len(list_id)-1):
    if list_id[k] + 1 != list_id[k+1]:
        print(list_id[k] + 1)