def list_add(list1 , list2):
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        return list3

with open('input20.txt') as fin:
	map_area=[]
	value_area = []
	directions = [[1,0] , [0,1] , [-1,0] , [0,-1]]
	i=0
	for line in fin:
		map_area.append([])
		value_area.append([])
		j = 0
		for char in line.strip("\n"):
			map_area[i].append(char)
			if char == "S":
				starting_point = [i,j]
				value_area[i].append(0)
			else:
				value_area[i].append("NaN")
			if char == "E":
				ending_point = [i,j]
			j+=1
		value_area[i].append("NaN")
		i+=1
	value_area.append(["NaN"]*len(value_area[-1]))
	path = [starting_point]
	cur_pos = starting_point
	while cur_pos!= ending_point:

		for dir in directions:
			next_pos = list_add(cur_pos , dir)
			if (map_area[next_pos[0]][next_pos[1]] == "." or map_area[next_pos[0]][next_pos[1]] == "E") and value_area[next_pos[0]][next_pos[1]] == "NaN":
				value_area[next_pos[0]][next_pos[1]] = value_area[cur_pos[0]][cur_pos[1]] +1
				cur_pos = next_pos
				path.append(cur_pos)

	sum = 0
	for point in path:
		for i in range(-20,21):
			rem = 20-abs(i)
			for j in range(-rem , rem+1):
				jump_pos = list_add(point , [i,j])
				if 0 < jump_pos[0] and 0<jump_pos[1] and jump_pos[0] < len(value_area) and jump_pos[1] < len(value_area[0]):
					if value_area[jump_pos[0]][jump_pos[1]]!= "NaN" and value_area[jump_pos[0]][jump_pos[1]] - value_area[point[0]][point[1]] >= 100 +abs(i)+abs(j):
						sum+=1
	print(sum)
