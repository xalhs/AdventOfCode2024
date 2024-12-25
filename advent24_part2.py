def operations(list1 , dict1):
    if list1[1] == "AND":
        return (dict1[list1[0]] and dict1[list1[2]])
    if list1[1] == "OR":
        return (dict1[list1[0]] or dict1[list1[2]])
    if list1[1] == "XOR":
        return (dict1[list1[0]] ^ dict1[list1[2]])

def make_dict_fundamental(con_dict):
    prev_dict = {}
    while con_dict != prev_dict:
        prev_dict = copy.deepcopy(con_dict)
        for key in con_dict:
            if key in con_dict[key] or len(con_dict[key]) > 10*len(order):
                return
            leng = len(con_dict[key])
            for k in range(leng):
                element = con_dict[key][k]
                if element in con_dict:
                    con_dict[key].remove(element)
                    con_dict[key] += con_dict[element]
    return prev_dict

def eliminate_con_singular(con_dict , index):
    prev_dict = {}
    new_dict = copy.deepcopy(con_dict)
    if not sorted(order)[index] in accounted_for:
        accounted_for.append(sorted(order)[index])
    while new_dict != prev_dict:
        prev_dict = copy.deepcopy(new_dict)
        key = sorted(order)[index]
        leng = len(new_dict[key])
        for k in range(leng):
            element = new_dict[key][k]
            if element in new_dict:
                if not element in accounted_for:
                    accounted_for.append(element)
                new_dict[key].remove(element)
                new_dict[key] += new_dict[element]

def find_descendants(con_dict , index):
    prev_dict = {}
    new_dict = copy.deepcopy(con_dict)
    if not sorted(order)[index] in descendants:
        descendants.append(sorted(order)[index])
    while new_dict != prev_dict:
        prev_dict = copy.deepcopy(new_dict)
        key = sorted(order)[index]
        leng = len(new_dict[key])
        for k in range(leng):
            element = new_dict[key][k]
            if element in new_dict:
                if not element in descendants:
                    descendants.append(element)
                new_dict[key].remove(element)
                new_dict[key] += new_dict[element]

def find_odd_element(idk = False):
    for i in range(45):
        for k in range(max(i , 0), min(i+2 , 45)):
            a = 2**i
            b = 2**k-1
            res = make_calculation(a,b)
            ans = res ^ (a+b)
            if ans != 0:
                for j,char in enumerate(reversed( bin(ans).split("b")[1] )):
                    if char != "0":
                        if j<10:
                            return("0"+str(j))
                        else:
                            return(str(j))

    return "45"

def find_odd_element2(con_dict):
    for i,element in enumerate(sorted(order)):
        expected_elements = ['x00' , 'y00']
        if i >0 and i<(len(order) - 1):
            expected_elements += [x[i] , y[i]]
        for j in range(i-1):
            expected_elements += [x[j+1] , y[j+1]]*2

        if sorted(con_dict[element])   !=   sorted(expected_elements):
            return element.split("z")[1]
    return "45"

import random
def find_odd_element3(con_dict):
    for i in range(45):
        a = random.randint(0,2**45-1)
        b = random.randint(0,2**45-1)
        for k in range(max(i , 0), min(i+1 , 45)):
            res = make_calculation(a,b)
            ans = res ^ (a+b)
            if ans != 0:
                for j,char in enumerate(reversed(  bin(ans).split("b")[1]  )       ):
                    if char != "0":
                        if j<10:
                            return("0"+str(j))
                        else:
                            return(str(j))
    return "45"

def make_calculation(a,b):
    dict = {}
    a = str(bin(a)).split("b")[1]
    b = str(bin(b)).split("b")[1]
    for j in range(len(x)):
        if j < len(a):
            dict[sorted(x)[j]] = int(a[::-1][j])
        else:
            dict[sorted(x)[j]]  = 0
        if j < len(b):
            dict[sorted(y)[j]] = int(b[::-1][j])
        else:
            dict[sorted(y)[j]] = 0

    instr2 = copy.deepcopy(instructions)
    i = 0
    dict2 = dict
    prev_instr2 = []
    while instr2!= []:
        spl = instr2[i]
        if spl[0] in dict2 and spl[2] in dict2:
            dict2[spl[4]] = operations(spl , dict2)
            instr2.pop(i)

        if len(instr2) !=0:
            if i+1 == len(instr2) and prev_instr2== instr2:
                break
            elif i+1 == len(instr2):
                prev_instr2 = copy.deepcopy(instr2)
            i = (i+1)%len(instr2)

    string = ""
    for el in reversed(sorted(order)):
        if el in dict2:
            string += str(dict2[el])
        else:
            continue
    return int(string , 2)

def find_max_index(list1):
    for el in reversed(sorted(x)):
        if el in list1:
            return int(el[1:])

def find_pool(con_dict , index):
    pool = []
    for key in con_dict:
        if find_max_index(con_dict[key]) <= index:
             pool.append(key)
    return pool

with open('input24.txt') as fin:
    sum = 0
    import copy
    x = []
    y = []
    final = []
    con_dict = {}
    for line in fin:
        if line == "\n":
            break
        spl = line.rstrip("\n").split(": ")
        if spl[0].startswith("x"):
            x.append(spl[0])

        if spl[0].startswith("y"):
            y.append(spl[0])

    x = sorted(x)
    y = sorted(y)
    instructions = []
    order = []

    for line in fin:
        instructions.append(line.rstrip("\n").split(" "))

        con_dict[instructions[-1][-1]] = [instructions[-1][0] , instructions[-1][2] ]
        if instructions[-1][-1].startswith("z"):
            order.append(instructions[-1][-1])

    ogest_dict =   copy.deepcopy(con_dict)
    og_dict =  copy.deepcopy(con_dict)
    con_dict = make_dict_fundamental(con_dict)
    instructions_backup  = copy.deepcopy(instructions)

    el_ind = min(find_odd_element(con_dict), find_odd_element2(con_dict) , find_odd_element3(con_dict))
    min_el_ind = int(el_ind)

    for h in range(4):
        accounted_for = []
        for o in range(min_el_ind):
            eliminate_con_singular(ogest_dict , o)

        descendants = []
        find_descendants(ogest_dict ,int(el_ind))

        con_dict = copy.deepcopy(og_dict)
        con_dict = make_dict_fundamental(con_dict)
        pool = find_pool(con_dict , int(el_ind))
        rems = [p for p in pool if p not in accounted_for]
        rem1 = [p for p in descendants if p not in accounted_for]
        
        already_searched = []
        for key in rem1:
            already_searched.append(key)
            for key2 in [p for p in rems if p not in already_searched]:
                el_ind = copy.copy(min_el_ind)
                temp = og_dict[key]
                og_dict[key] = og_dict[key2]
                og_dict[key2] = temp
                for instruction in instructions:
                    if instruction[-1] == key:
                        instruction[-1] = key2
                    elif  instruction[-1] == key2:
                        instruction[-1] = key
                con_dict = copy.deepcopy(og_dict)
                con_dict = make_dict_fundamental(con_dict)
                if con_dict == None:
                    el_ind = "0"
                else:
                    el_ind = min(find_odd_element(con_dict), find_odd_element2(con_dict) , find_odd_element3(con_dict))
                if int(el_ind) > min_el_ind:
                    break
                og_dict =  copy.deepcopy(ogest_dict)
                instructions = copy.deepcopy(instructions_backup)
            if int(el_ind) > min_el_ind:
                ogest_dict =  copy.deepcopy(og_dict)
                print(key2 + "," + key)
                final += [key2, key]
                instructions_backup  = copy.deepcopy(instructions)
                min_el_ind = int(el_ind)
                print(min_el_ind)
                break

    final_str = ""
    for f in sorted(final):
        final_str += f + ","

    final_str = final_str.rstrip(",")
    print(final_str)
