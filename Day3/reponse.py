from itertools import chain


characters = ["0","1","2","3","4","5","6","7","8","9"]
array = []
# flag_fin = 0
sum = 0

def Day3part1():
    print("Day3 part1")

    with open('puzzle.txt') as file:
        for line in file:
            array.append(list(line))

    coor = []
    sum = 0
    for coor_ligne, line in enumerate(array):
        flag_debut = 0
        flag_fin = 0
        coor = []
        for coor_colonne, char in enumerate(line):
            if char in characters and flag_debut == 0:
                coor = [coor_ligne, coor_colonne]
                flag_debut = 1
            if (char not in characters or char in ['.', '\n']) and flag_debut == 1:
                if coor[0] != 0:
                    if check_before_or_after(array[coor_ligne - 1], coor, coor_colonne):
                        sum += list_to_int(line[coor[1]:(coor_colonne)])
                        flag_fin = 1
                if check_around(array[coor_ligne], coor, coor_colonne):
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                if char not in characters and char not in ['.', '\n']:
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                if coor_ligne < (len(array)-1) and check_before_or_after(array[coor_ligne+1], coor, coor_colonne):
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                else:
                    flag_fin = 1
                    
            if flag_fin == 1 or char == '\n':
                coor = []
                flag_debut = 0
                flag_fin = 0
    print(sum)

# utils
def list_to_int(list):
    temp_string = ''
    for chiffre in list:
        temp_string+=chiffre
    return int(temp_string)

def check_before_or_after(list, coor, coor_colonne):
    coor_avant = int(coor[1]) - 1 if (int(coor[1]) - 1) >= 0 else 0
    taille_ligne = len(list) - 1
    coor_apres = int(coor_colonne) + 1 if (int(coor_colonne) + 1) < taille_ligne else taille_ligne
    for char_lign_avant in list[coor_avant:coor_apres]:
        if char_lign_avant not in characters and char_lign_avant not in ['.', '\n']:
            return True
    return False

def check_around(list, coor, coor_colonne):
    coor_avant = int(coor[1]) - 1 if (int(coor[1]) - 1) > 0 else 0
    if coor[1] > 0 and list[coor_avant] not in characters and list[coor_avant] not in ['.', '\n']:
        return True
    return False


# Day3part1()

def Day3part2():
    print("Day3 part2")

    with open('puzzle.txt') as file:
        for line in file:
            array.append(list(line))

    coor = []
    sum = 0
    for coor_ligne, line in enumerate(array):
        numbers = []
        flag_debut = 0
        flag_fin = 0
        coor = []
        for coor_colonne, char in enumerate(line):
            if char == "*" and flag_debut == 0:
                coor = [coor_ligne, coor_colonne]
                flag_debut = 1
            if flag_debut == 1:
                #check la ligne d'avant
                if coor[0] != 0:
                    search_coor = []
                    i = 1
                    j = 0
                    k = 0
                    if array[coor[0]-1][coor[1]-1] in characters:
                        while array[coor[0]-1][coor[1]-i] in characters and coor[1]-i > 0 and array[coor[0]][coor[1]-(i+1)] in characters:
                            i += 1
                        while array[coor[0]-1][coor[1]+j] in characters and coor[1]+j < len(array[coor[0]-1]):
                            j += 1
                        if j < 0:
                            while array[coor[0]-1][coor[1]+k] in characters and coor[1]+k < len(array[coor[0]-1]):
                                k += 1
                        maximum = max(j,k)
                        numbers.append(list_to_int(array[coor[0]-1][coor[1]-i:coor[1]+maximum]))
                    if array[coor[0]-1][coor[1]] in characters and array[coor[0]-1][coor[1]-1] not in characters:
                        i = 0
                        while array[coor[0]-1][coor[1]+i] in characters and coor[1]+i < len(array[coor[0]-1]):
                            i += 1
                        numbers.append(list_to_int(array[coor[0]-1][coor[1]:coor[1]+i]))
                    if array[coor[0]-1][coor[1]+1] in characters and array[coor[0]-1][coor[1]] not in characters:
                        i = 1
                        while array[coor[0]-1][coor[1]+i] in characters and coor[1]+i < len(array[coor[0]-1]):
                            i += 1
                        numbers.append(list_to_int(array[coor[0]-1][coor[1]+1:coor[1]+i]))
                #On check les cotés
                if array[coor[0]][coor[1]-1] in characters:
                    i = 1
                    while array[coor[0]][coor[1]-i] in characters and coor[1]-i > 0 and array[coor[0]][coor[1]-(i+1)] in characters:
                        i += 1
                    numbers.append(list_to_int(array[coor[0]][coor[1]-i:coor[1]]))
                if array[coor[0]][coor[1]+1] in characters:
                    i = 1
                    while array[coor[0]][coor[1]+i] in characters and coor[1]+i < len(array[coor[0]]):
                        i += 1
                    numbers.append(list_to_int(array[coor[0]][coor[1]+1:coor[1]+i]))
                #On check après
                if (coor[0] + 1) < len(array):
                    search_coor = []
                    i = 1
                    j = 0
                    k = 0
                    if array[coor[0]+1][coor[1]-1] in characters:
                        while array[coor[0]+1][coor[1]-i] in characters and coor[1]-i > 0 and array[coor[0]+1][coor[1]-(i+1)] in characters:
                            i += 1
                        while array[coor[0]+1][coor[1]+j] in characters and coor[1]+j < len(array[coor[0]+1]):
                            j += 1
                        if j < 0:
                            while array[coor[0]+1][coor[1]+k] in characters and coor[1]+k < len(array[coor[0]+1]):
                                k += 1
                        maximum = max(j,k)
                        numbers.append(list_to_int(array[coor[0]+1][coor[1]-i:coor[1]+maximum]))
                    if array[coor[0]+1][coor[1]] in characters and array[coor[0]+1][coor[1]-1] not in characters:
                        i = 0
                        while array[coor[0]+1][coor[1]+i] in characters and coor[1]+i < len(array[coor[0]+1]):
                            i += 1
                        numbers.append(list_to_int(array[coor[0]+1][coor[1]:coor[1]+i]))
                    if array[coor[0]+1][coor[1]+1] in characters and array[coor[0]+1][coor[1]] not in characters:
                        i = 1
                        while array[coor[0]+1][coor[1]+i] in characters and coor[1]+i < len(array[coor[0]+1]):
                            i += 1
                        numbers.append(list_to_int(array[coor[0]+1][coor[1]+1:coor[1]+i]))
                flag_debut = 0
        if len(numbers) > 1:
            sum += multiplyList(numbers)
    print(sum)

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

Day3part2()
