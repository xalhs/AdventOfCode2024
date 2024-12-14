def list_mod(list1 , mod1 , mod2):
    return [list1[0]%mod1 , list1[1]%mod2]


def list_mul(list1 , mul):
    return [x*mul for x in list1]

def list_add(list1 , list2):
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        return list3

def has_neighbor(position , new_pos):
    for i in range(-1, 1):
        for j in range(-1,1):
            if i ==0 and j==0:
                continue
            if [position[0]+i,position[1]+j] in new_pos:
                return True
    return False

with open('input14.txt') as fin:
    pos = []
    vel = []
    horizontal = 101
    vertical = 103
    for line in fin:
        l = line.rstrip('\n').split(" ")
        pos.append([ int(x) for x in l[0].split("p=")[1].split(",")])
        vel.append([ int(x) for x in  l[1].split("v=")[1].split(",")])


    num_of_neighbors = 0
    for i in range(len(pos)):
        if has_neighbor(pos[i] , pos):
            num_of_neighbors += 1
        max1 = num_of_neighbors
        maxs = 0

    new_pos = pos

    for s in range(1, horizontal*vertical):
        num_of_neighbors = 0
        for i in range(len(pos)):
            new_pos[i] = list_mod(list_add(new_pos[i] , vel[i]), horizontal ,vertical)

        all_neighbors = True
        for i in range(len(pos)):
            if has_neighbor(new_pos[i] , new_pos):
                num_of_neighbors += 1
        if num_of_neighbors > max1:
            max1 = num_of_neighbors
            maxs = s
    print(maxs)
