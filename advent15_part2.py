def next_space(pos,direct , map_area):
	if direct == "left":
		for i in range(pos[1]-1 , 0 , -1):
			if map_area[pos[0]][i] == "#" or map_area[pos[0]][i] == ".":
				return [[pos[0],i] , map_area[pos[0]][i]]
	if direct == "up":
		for i in range(pos[0]-1 , 0 , -1):
			if map_area[i][pos[1]] == "#" or map_area[i][pos[1]]  == ".":
				return [[i, pos[1]] , map_area[i][pos[1]]]
				
	if direct == "right":
		for i in range(pos[1]+1 , len(map_area[pos[0]])):
			if map_area[pos[0]][i] == "#" or map_area[pos[0]][i]  == ".":
				return [[pos[0],i] , map_area[pos[0]][i]]		
	if direct == "down":
		for i in range(pos[0]+1 , len(map_area)):
			if map_area[i][pos[1]] == "#" or map_area[i][pos[1]] == ".":
				return [[i, pos[1]] , map_area[i][pos[1]]]
									
	return [[] , "#"]									



def list_add(list1 , list2):
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        return list3

def recursion(box_pos , dire):
	new_pos = list_add(box_pos , dict2[dire])
	mark_area[box_pos[0]][box_pos[1]] = "M"
	
	
	if map_area[new_pos[0]][new_pos[1]] == "[":
		res = recursion([new_pos[0] ,new_pos[1]] , dire)
		if res == False:
			return False
	elif map_area[new_pos[0]][new_pos[1]] == "]":
		res = recursion([new_pos[0] , new_pos[1] -1] , dire)
		if res == False:
			return False
	elif map_area[new_pos[0]][new_pos[1]] == "#":
		return False
				
	if map_area[new_pos[0]][new_pos[1]+1] == "[":
		res = recursion([new_pos[0] ,new_pos[1]+1] , dire)
		if res == False:
			return False
	elif map_area[new_pos[0]][new_pos[1]+1] == "#":
		return False 

def move_everything(direct , show = False):
	global map_area
	if direct == "up":
		new_map = list(map(list, zip(*map_area)))
		for i in range(1,len(map_area)):
			for j in range(len(map_area[i])):
				if mark_area[i][j] == "M":
					#new_map[j][i]
					new_map[j].pop(i-1)
					new_map[j].insert(i, ".")
					new_map[j+1].pop(i-1)
					new_map[j+1].insert(i, ".")
				if mark_area[i][j] == "A":
					new_map[j].pop(i-1)
					new_map[j].insert(i, ".")	
			if show:
				sa = convert_to_string()
				print(sa, end=f'\r')
				time.sleep(1)			
					
	if direct == "down":
		new_map = list(map(list, zip(*map_area)))
		for i in range(len(map_area)-1 , 0 , -1):
			for j in range(len(map_area[i])):
				if mark_area[i][j] == "M":
					#new_map[j][i]
					new_map[j].pop(i+1)
					new_map[j].insert(i, ".")
					new_map[j+1].pop(i+1)
					new_map[j+1].insert(i, ".")	
				if mark_area[i][j] == "A":
					new_map[j].pop(i+1)
					new_map[j].insert(i, ".")
			if show:
				sa = convert_to_string()
				print(sa, end=f'\r')
				time.sleep(1)							
	map_area = list(map(list, zip(*new_map)))

def reset_marks():
	global mark_area
	mark_area = [["X"]*len(map_area[i]) for i in range(len(map_area))] 
		
def convert_to_string():
	global map_area
	string_area = []
	for i in range(len(map_area)):
		string_area.append("".join(map_area[i]))
	return string_area			

def find_marks():
	for i in range(len(mark_area)):
		for j in range(len(mark_area[i])):
			if mark_area[i][j] != "X":
				print([i,j])

def num_of_boxes():
	count = 0
	for i in range(len(map_area)):
		for j in range(len(map_area[i])):
			if map_area[i][j] == "[":
				count +=1
	return count	
			
with open('input15.txt') as fin:
	dict1 = {"<":"left" , ">":"right" , "^": "up" , "v" : "down"}
	global dict2
	dict2 = {"left": [0,-1] , "right" :[ 0,1] , "up": [-1,0], "down": [1,0]}
	global map_area
	map_area=[]
	global mark_area
	mark_area = []
	i=0
	for line in fin:
		if line == "\n":
			break
		map_area.append([])
		for j,char in enumerate(line.rstrip("\n")):
			if char == "#":	
				map_area[i] += ["#"]*2
			elif char == "O":
				map_area[i] += ["[","]"]
			elif char == ".":	
				map_area[i] += ["."]*2		
			elif char == "@":
				map_area[i] += ["@","."]
				starting_pos = [i,j*2] 	

		i+=1
	pos = starting_pos
	reset_marks()
	#import time
	timer = 0
	for line in fin:
		for char in line.rstrip("\n"):
			timer +=1
			direct = dict1[char]
			next = next_space(pos,direct , map_area)

			
			
			if next[1] == ".":
				if direct == "left" or direct == "right":
				
					map_area[next[0][0]].pop(next[0][1])
					map_area[pos[0]].insert(pos[1] , ".")
					pos = list_add(pos , dict2[dict1[char]])
				if direct == "up" or direct == "down":
					res = False
					new_pos = list_add(pos , dict2[dict1[char]])
					if map_area[new_pos[0]][new_pos[1]] == "[":
						res = recursion(new_pos , direct)
					elif map_area[new_pos[0]][new_pos[1]] == "]":
						res = recursion([new_pos[0] , new_pos[1]-1] , direct)
					elif map_area[new_pos[0]][new_pos[1]] == ".":
						new_map = list(map(list, zip(*map_area)))
						new_map[new_pos[1]].pop(new_pos[0])
						new_map[pos[1]].insert(pos[0] , ".")
						map_area = list(map(list, zip(*new_map)))
						pos = new_pos	
					if res != False:
						mark_area[pos[0]][pos[1]] = "A"
						move_everything(direct)
						pos = new_pos
		
					reset_marks()
					
					
					
			#sa = convert_to_string()
			#print(sa)
			#time.sleep(0.001)
	sum = 0		
	for i,row in enumerate(map_area):
		for j,char in enumerate(row):
			if char == "[":
				sum += 100*i+j
	print(sum)			
			
	
	
