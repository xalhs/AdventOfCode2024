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

def count_partitions(partition , prev_parts):
    global sum
    global letters_list
    global already_tried
    global cur_lin
    if tuple(partition) in memory:
        return memory[tuple(partition) ]
    local_sum = 0
    if partition == []:
        return 1
    for i in range(len(partition)+1):
        if "".join(partition[:i]) in letters_list:
            new_prev_parts = prev_parts + ["".join(partition[:i])]
            if not tuple(new_prev_parts) in already_tried:
                already_tried[  tuple(new_prev_parts) ] = []
            elif partition[i:] in  already_tried[ tuple(new_prev_parts) ]:
                continue
            already_tried[ tuple(new_prev_parts) ].append(partition[i:])
            local_sum += count_partitions(partition[i:] , new_prev_parts)

    memory[tuple(partition) ] = local_sum
    return local_sum

def count_string(string  , list1):
    global sum
    global refined_list
    if string == "":
        sum += count_partitions(list1 ,  [])
        return True
    for i,letter in enumerate(refined_list):
        if string.startswith(letter):
            count_string(string.split(letter , 1)[1] , list1+[letter])

with open('input19.txt') as fin:
    global memory
    memory = {}
    global sum
    sum = 0
    global letters_list
    letters_list = []
    global refined_list
    refined_list = []
    global already_tried
    already_tried = {}
    for line in fin:
        if line == "\n":
            break
        letters_list = line.rstrip("\n").split(", ")
    global starting_string
    for string in letters_list:
        starting_string = string
        if not is_string_doable(string , True):
            refined_list.append(string)

    for line in fin:
        line = line.rstrip("\n")
        if is_string_doable(line):
            #print(sum)
            already_tried = {}
            count_string(line , [])
    print(sum)
