def is_interconnected(list1):
    is_it = [True , ""]
    if list1 == None:
        return is_it
    for pc in list1:
        for pc2 in list1:
            if pc == pc2:
                continue
            if not pc2 in dict[pc]:
                is_it = [False , pc2]
    return is_it

with open('input23.txt') as fin:
    dict = {}
    for line in fin:
        comps = line.rstrip("\n").split("-")
        for i in range(2):
            if comps[i] in dict:
                dict[comps[i]].append(comps[(i+1)%2])
            else:
                dict[comps[i]] = [(comps[(i+1)%2])    ]

    largest_list = []
    for key in dict:
        for pc in dict[key]:
            assumption = sorted(list(set(dict[key]).intersection(set(dict[pc]))))
            check_con = is_interconnected(assumption)
            while not check_con[0]:
                assumption = assumption.remove(check_con[1])
                check_con = is_interconnected(assumption)

            if assumption == None:
                continue
            if is_interconnected(assumption):
                if len(assumption) +2 >  len(largest_list):
                    largest_list = sorted(assumption + [key , pc])

    string = ""
    for pc in largest_list:
        string += pc + ","

    string = string.rstrip(",")
    print(string)
