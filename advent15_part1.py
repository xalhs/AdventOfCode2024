def next_space(pos,direct , map_area):
	if direct == "left":
		for i in range(pos[1]-1 , 0 , -1):
			if map_area[pos[0]][i] != "O":
				return [[pos[0],i] , map_area[pos[0]][i]]
	if direct == "up":
		for i in range(pos[0]-1 , 0 , -1):
			if map_area[i][pos[1]] != "O":
				return [[i, pos[1]] , map_area[i][pos[1]]]
				
	if direct == "right":
		for i in range(pos[1]+1 , len(map_area[pos[0]])):
			if map_area[pos[0]][i] != "O":
				return [[pos[0],i] , map_area[pos[0]][i]]		
	if direct == "down":
		for i in range(pos[0]+1 , len(map_area)):
			if map_area[i][pos[1]] != "O":
				return [[i, pos[1]] , map_area[i][pos[1]]]
									
	return [[] , "#"]									

def list_add(list1 , list2):
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        return list3
        
def convert_to_string():
	global map_area
	string_area = []
	for i in range(len(map_area)):
		string_area.append("".join(map_area[i]))
	return string_area			        

with open('input15.txt') as fin:
	dict1 = {"<":"left" , ">":"right" , "^": "up" , "v" : "down"}
	dict2 = {"left": [0,-1] , "right" :[ 0,1] , "up": [-1,0], "down": [1,0]}
	global map_area
	region_index = -1
	regions_area = []
	regions_connections = []
	map_area=[]
	i=0
	for line in fin:
		if line == "\n":
			break#len_map_area
		map_area.append([])
		for j,char in enumerate(line.rstrip("\n")):
			map_area[i].append(char)
			if char == "@":
				starting_pos = [i,j] 

		i+=1
	pos = starting_pos	
	#import time
	for line in fin:
		for char in line.rstrip("\n"):
			direct = dict1[char]
			next = next_space(pos,direct , map_area)
			if next[1] == ".":
				if direct == "left" or direct == "right":
				
					map_area[next[0][0]].pop(next[0][1])
					map_area[pos[0]].insert(pos[1] , ".")
					pos = list_add(pos , dict2[dict1[char]])
				if direct == "up" or direct == "down":	
					new_map = list(map(list, zip(*map_area)))
					new_map[next[0][1]].pop(next[0][0])
					new_map[pos[1]].insert(pos[0] , ".")
					pos = list_add(pos , dict2[dict1[char]])
					map_area = list(map(list, zip(*new_map)))
			#sa = convert_to_string()
			#print(sa)
			#time.sleep(0.001)			
	sum = 0		
	for i,row in enumerate(map_area):
		for j,char in enumerate(row):
			if char == "O":
				sum += 100*i+j
	print(sum)			
			
	
	
