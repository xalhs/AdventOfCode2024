def list_mod(list1 , mod1 , mod2):
    return [list1[0]%mod1 , list1[1]%mod2]


def list_mul(list1 , mul):
    return [x*mul for x in list1]

def list_add(list1 , list2):
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        return list3

with open('input14.txt') as fin:
    pos = []
    vel = []
    horizontal = 101
    vertical = 103
    for line in fin:
        l = line.rstrip('\n').split(" ")
        pos.append([ int(x) for x in l[0].split("p=")[1].split(",")])
        vel.append([ int(x) for x in  l[1].split("v=")[1].split(",")])
    s = 0
    new_pos = []
    for i in range(len(pos)):
        new_pos.append(list_mod(list_add(pos[i] , list_mul(vel[i],100)), horizontal ,vertical)  )


    quadr1 =0
    quadr2 =0
    quadr3 =0
    quadr4 =0
    for el in new_pos:
        if el[0]< int(horizontal/2) and el[1] <  int(vertical/2):
            quadr1 +=1
        if el[0]> int(horizontal/2) and el[1] <  int(vertical/2):
            quadr2 +=1
        if el[0]< int(horizontal/2) and el[1] >  int(vertical/2):
            quadr3 +=1
        if el[0]> int(horizontal/2) and el[1] > int(vertical/2):
            quadr4 +=1
    print(quadr1*quadr2*quadr3*quadr4)
    grid = []
    for i in range(vertical):
        grid.append([])
        grid[i] = ""
        for j in range(horizontal):
            if [j,i] in new_pos:
                grid[i]+="X"
            else:
                grid[i]+="."
