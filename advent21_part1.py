def recurs(coords , count , aaa = False):
	if count ==4:
		return
	global cur_pos
	list1 = []
	for i in range( abs(coords[0])):
		list1.append([ int(coords[0]/abs(coords[0])) , 0])

	for j in range(abs(coords[1])):
		list1.append([0, int(coords[1]/abs(coords[1])) ])

	random.shuffle(list1)
	for position in list1:
		dif = add_points(  movepad[dict1[tuple(position)]]     ,cur_pos[count] , False )
		if (add_points(cur_pos[count-1] , [ 0,coords[1]]) == [5,0]  or add_points(cur_pos[count-1] , position) == [3,0])  or False:
			sum[-1] +=float('inf')
		recurs(dif , count+1 )
		cur_pos[count] = movepad[dict1[tuple(position)]]
		cur_pos[count-1] = add_points(cur_pos[count-1] , position)
		sum[count] +=1

	dif = add_points(  movepad["A"]     ,cur_pos[count] , False)
	recurs(dif , count+1 )
	cur_pos[count] = movepad["A"]
	sum[count] +=1

def add_points(coord2 , coord1 , add = True ):
    if add == True:
        return[coord2[0]+ coord1[0] , coord2[1]+coord1[1]]
    else:
        return[coord2[0]- coord1[0] , coord2[1]-coord1[1]]

import random
with open('input21.txt') as fin:
	keypad = {"A": [3,2] , "0":[3,1] , "3":[2,2] , "2":[2,1] , "1":[2,0], "6":[1,2],"5":[1,1] , "4":[1,0] , "9":[0,2] , "8":[0,1] , "7":[0,0]}
	movepad = {"A":[0,2], "^":[0,1], ">":[1,2] , "v":[1,1] , "<":[1,0]}
	dict1 = {(-1,0):"^" , (0,-1) : "<" , (1,0):"v" , (0,1):">"}
	global cur_pos
	cur_pos = [ [3,2],[0,2],[0,2],[0,2]]
	global sum

	final_sum = 0
	for line in fin:

		min_sum = float('inf')
		decisions = []
		for dec1 in [True, False]:
			for dec2 in [True, False]:
				for dec3 in [True, False]:
					for dec4 in [True, False]:
						decisions.append([dec1,dec2,dec3,dec4])
		for k in range(100):
			for decision in decisions:
				cur_pos = [ [3,2],[0,2],[0,2],[0,2]]
				sum = [0,0,0,0]
				for letter in line.strip("\n")[:4]:
					recurs(add_points(keypad[letter]  , cur_pos[0] , False) , 1 , decision)
					cur_pos[0] = keypad[letter]
				if sum[-1] < min_sum:
					min_sum = sum[-1]

	#	print(min_sum)
		final_sum += min_sum*int(line.strip("A\n"))

	print(final_sum)
