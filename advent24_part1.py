def operations(list1):
    if list1[1] == "AND":
        return (dict[list1[0]] and dict[list1[2]])
    if list1[1] == "OR":
        return (dict[list1[0]] or dict[list1[2]])
    if list1[1] == "XOR":
        return (dict[list1[0]] ^ dict[list1[2]])


with open('input24.txt') as fin:
    sum = 0
    import copy
    dict = {}
    for line in fin:
        if line == "\n":
            break
        spl = line.rstrip("\n").split(": ")
        dict[spl[0]] = int(spl[1])
    instructions = []
    order = []
    for line in fin:
        instructions.append(line.rstrip("\n").split(" "))
        if instructions[-1][-1].startswith("z"):
            order.append(instructions[-1][-1])

    i = 0
    while instructions!= []:
        spl = instructions[i]
        if spl[0] in dict and spl[2] in dict:
            dict[spl[4]] = operations(spl)
            instructions.pop(i)

        if len(instructions) !=0:
            i = (i+1)%len(instructions)
    string = ""
    for el in reversed(sorted(order)):
        string += str(dict[el])

    print(int(string , 2))
