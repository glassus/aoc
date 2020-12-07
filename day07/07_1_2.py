import numpy as np

lines = open("input.txt").read().split('\n')[:-1]

color_dict = {}

def add_color_from_2_words(w1, w2, color_dict):
    color = w1 + ' ' + w2
    if color not in color_dict:
        color_id = len(color_dict)
        color_dict[color] = color_id
        

def extract_colors(line, color_dict):
    mots = line.split(' ')
    add_color_from_2_words(mots[0], mots[1], color_dict)
    for i in range(len(mots)):
        if mots[i] in "0123456789":
            add_color_from_2_words(mots[i+1], mots[i+2], color_dict)
  
def create_color_dict(color_dict):
    for line in lines:
        extract_colors(line, color_dict)

create_color_dict(color_dict)
n = len(color_dict)
M = np.zeros((n,n), int)

def info_to_matrix(line, M):
    mots = line.split(' ')
    i = color_dict[mots[0] + ' ' + mots[1]]
    for k in range(len(mots)):
        if mots[k] in "0123456789":
            j = color_dict[mots[k+1] + ' ' + mots[k+2]]
            nb = int(mots[k])
            M[i,j] = nb

def fulfill_matrix(M):
    for line in lines:
        info_to_matrix(line, M)

fulfill_matrix(M)

id_color = color_dict['shiny gold']

bags_sols = []
def remonte_arbre(j, bags_sols):
    if sum(M[:,j]) == 0:
        return 0
    else :
        for i in range(len(M[:,j])):
            if M[i,j] != 0:
                bags_sols.append(i)
                remonte_arbre(i, bags_sols)

# part1
#remonte_arbre(id_color, bags_sols)
#bags_sols = set(bags_sols)
#print(len(bags_sols))

# part2
tot_bags = []
def descend_arbre(i, nb, tot_bags):
    if sum(M[i,:]) == 0:
        return 0
    else :
        for j in range(len(M[i,:])):
            if M[i,j] != 0:
                tot_bags.append(nb*M[i,j])
                descend_arbre(j, nb*M[i,j], tot_bags)

descend_arbre(id_color, 1, tot_bags)
print(sum(tot_bags))




            