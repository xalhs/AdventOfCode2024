def is_string_doable(string , early = False):
    global letters_list
    global refined_list
    global starting_string
    if early:
        counting_list = letters_list
    else:
        counting_list = refined_list
    if string == "":
        return True
    for i,letter in enumerate(counting_list):
        if letter == starting_string:
            continue
        if string.startswith(letter):

            if is_string_doable(string.split(letter , 1)[1] , early):

                return True

    return False

with open('input19.txt') as fin:
    global letters_list
    letters_list = []
    global refined_list
    refined_list = []
    for line in fin:
        if line == "\n":
            break
        letters_list = line.rstrip("\n").split(", ")
    sum = 0
    global starting_string
    for string in letters_list:
        starting_string = string
        if string == "bw":
            pass
        if not is_string_doable(string , True):
            refined_list.append(string)

    for line in fin:
        line = line.rstrip("\n")
        starting_string = line
        if is_string_doable(line):
            sum+=1
    print(sum)
