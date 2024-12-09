def add_points(coord2 , coord1 , add = True ):
    if add == True:
        return[coord2[0]+ coord1[0] , coord2[1]+coord1[1]]
    else:
        return[coord2[0]- coord1[0] , coord2[1]-coord1[1]]

def antinodes_finder(coord2 , coord1):
    dif = add_points(coord2 , coord1 , False )
    anti1 = add_points(coord2 , dif )
    anti2 = add_points(coord1, dif , False)

    return [anti1 , anti2 ]

def is_inbounds(coord , bounds):
    if coord[0] < 0 or coord[0]>bounds[0] or coord[1] <0 or coord[1] > bounds[1]:
        return False
    return True

with open('input8.txt') as fin:
    #sum = 0
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
                positions = antinodes_finder(pos1 , pos2)
                if not positions[0] in antinodes and is_inbounds(positions[0],bounds):
                    antinodes.append(positions[0])
                if not positions[1] in antinodes and is_inbounds(positions[1] , bounds):
                    antinodes.append(positions[1] )
    print(len(antinodes))
