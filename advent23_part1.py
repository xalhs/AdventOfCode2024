with open('input23.txt') as fin:
    sum = 0
    dict = {}
    line_list = []
    for line in fin:
        comps = line.rstrip("\n").split("-")
        line_list.append(comps)
        for i in range(2):
            if comps[i] in dict:
                dict[comps[i]].append(comps[(i+1)%2])
            else:
                dict[comps[i]] = [(comps[(i+1)%2])    ]
    triplet = []
    for doublet in line_list:
        for pc in dict[doublet[0]]:
            if pc in dict[doublet[1]]:
                new_list = [doublet[0] , doublet[1] , pc]
                new_list = sorted(new_list)
                if not new_list in triplet:
                    triplet.append(new_list)

    for trip in triplet:
        contains_T = False
        for computer in trip:
            if computer.startswith("t"):
                contains_T = True

        if contains_T:
            sum+=1
    print(sum)
