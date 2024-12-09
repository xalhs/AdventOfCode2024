def add_points(coord2 , coord1 , add = True ):
    if add == True:
        return[coord2[0]+ coord1[0] , coord2[1]+coord1[1]]
    else:
        return[coord2[0]- coord1[0] , coord2[1]-coord1[1]]
        
def is_inbounds(coord , bounds):
    if coord[0] < 0 or coord[0]>bounds[0] or coord[1] <0 or coord[1] > bounds[1]:
        return False
    return True

from math import gcd

with open('input8.txt') as fin:
    dict1 = {}
    i=0
    antinodes = []
    for line in fin:
        for j,char in enumerate(line.rstrip("\n")):
            if char != ".":
                if char in dict1:
                    dict1[char].append([i,j])
                else:
                    dict1[char] = [[i,j]]
        i +=1
    bounds = [i-1 , len(line.rstrip("\n"))-1]
    for type in dict1:
        for j,pos1 in enumerate(dict1[type]):
            for k in range(j+1, len(dict1[type])):
                pos2 = dict1[type][k]
                dif = add_points(pos2 , pos1 , False )
                globalcooldown = gcd(dif[0], dif[1])
                reduced_dif = [int(dif[0]/globalcooldown) ,  int(dif[1]/globalcooldown)]
                new_pos = pos1
                while is_inbounds(new_pos , bounds):
                    if not new_pos in antinodes:
                        antinodes.append(new_pos)
                    new_pos = add_points(new_pos , reduced_dif )
                new_pos = add_points(pos1 , reduced_dif , False )
                while is_inbounds(new_pos , bounds):
                    if not new_pos in antinodes:
                        antinodes.append(new_pos)
                    new_pos = add_points(new_pos , reduced_dif , False )

    print(len(antinodes))
