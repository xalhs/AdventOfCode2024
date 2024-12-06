def find_el(list1 , el , direction , alot=10000):
	if direction == "positive":
		adj = 1
	else:
		adj = -1	
	if direction == "negative":	
		extremal_el =  alot
		for element in list1:
			if element < extremal_el and element > el:
				extremal_el = element
	else:
		extremal_el =  -1
		for element in list1:
			if element > extremal_el and element < el:
				extremal_el = element
	if extremal_el == alot or extremal_el == -1:
		return None
							
	return extremal_el+adj	

with open('input6.txt') as fin:
	line_list = []
	
	map_area = []
	i=0
	hor_obs = []
	ver_obs = []
	for line in fin:
		if i == 0:
			for char in line:
				ver_obs.append([])
		hor_obs.append([])
		for j,char in enumerate(line):
			if char == "#":
				hor_obs[i].append(j)
				ver_obs[j].append(i)
				
		map_area.append(line.rstrip("\n")+"$")
		if "^" in line:
			starting_pos = [i,line.index("^")]
	
		i+=1
	map_area.append("$"*len(map_area[-1]))
		
	
	sum = 0
	direc = ["left" , "down" , "right" "up"]
	direc = ["up" , "right", "down" , "left"]
	dict1 = {'left': [hor_obs , "positive" ] , 
		"down":[ver_obs , "negative"] , 
		"right": [hor_obs, "negative"],"up": [ver_obs , "positive"]}
	size = len(map_area)
import copy			
for i in range(len(map_area)-1):
	for j in range(len(map_area[0])-1):
		if [i,j] == starting_pos:
			continue
		hor_obs[i].append(j)
		ver_obs[j].append(i)	
		direct = 0
		inside = True
		cur_pos = copy.copy(starting_pos)
		obs_visited = []
		while inside:
			if direc[direct] == "up" or direc[direct] == "down":
				relevant_el = cur_pos[1]
				other_el = cur_pos[0]
				size = len(map_area)
			else:
				relevant_el = cur_pos[0]
				other_el = cur_pos[1]
				size = len(map_area[0])	
				
			next = find_el(dict1[direc[direct]][0][relevant_el] ,other_el  , dict1[direc[direct]][1] , size+3)	
			
			if next == None:
				inside = False
			else:
				if direc[direct] == "up" or direc[direct] == "down":
					 cur_pos[0] = next
				else:
					cur_pos[1] = next
				if [cur_pos , direct] in obs_visited:
					inside = False
					sum +=1	
				obs_visited.append([copy.copy(cur_pos) , direct])	
				direct = (direct+1)%4
		hor_obs[i].pop()
		ver_obs[j].pop()		
print(sum)
