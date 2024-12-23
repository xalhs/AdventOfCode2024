def add_points(coord2 , coord1 , add = True ):
    if add == True:
        return[coord2[0]+ coord1[0] , coord2[1]+coord1[1]]
    else:
        return[coord2[0]- coord1[0] , coord2[1]-coord1[1]]

def reset_positions():
	global cur_pos
	cur_pos = [ [3,2]]
	for i in range(dim-1):
			cur_pos.append([0,2])

	global cur_char
	cur_char = "A"

def letters_to_coords(letters):
	return add_points(keypad[letters[1]] ,  keypad[letters[0]] , False)

def symbols_to_coords(symbols):
	return add_points(movepad[symbols[1]] ,  movepad[symbols[0]] , False)

keypad = {"A": [3,2] , "0":[3,1] , "3":[2,2] , "2":[2,1] , "1":[2,0], "6":[1,2],"5":[1,1] , "4":[1,0] , "9":[0,2] , "8":[0,1] , "7":[0,0]}
movepad = {"A":[0,2], "^":[0,1], ">":[1,2] , "v":[1,1] , "<":[1,0]}
dict1 = {(-1,0):"^" , (0,-1) : "<" , (1,0):"v" , (0,1):">"}

memory = [{} ]

# vertical first
b = {}
for let1 in keypad:
	for let2 in keypad:
		# -- horisontal
		# +- horizontal ###
		# ++ vertical
		# -+ vertical
		if letters_to_coords((let1 , let2))[1] >0:
			b[(let1 , let2)] = True
		else:
			b[(let1 , let2)] = False

b[("7" , "A")] = False  #should be these to not go out of the keypad
b[("4" , "A")] = False
b[("1" , "A")] = False
b[("7" , "0")] = False
b[("4" , "0")] = False
b[("1" , "0")] = False

b[( "A" , "7")] = True
b[( "A", "4" )] = True
b[( "A" ,"1" )] =True
b[( "0" , "7")] =True
b[( "0", "4" )] = True
b[( "0" ,"1" )] =True


memory_0 = [{}]
memory_0[0] = {}

b4 = {}
for key in movepad:
	for key2 in movepad:
		b4[tuple([key , key2])]  = True

#True = horizontal first
b4[("A" , "<")] = False #should be these to not go out of the directional keypad
b4[("<" , "A")] = True
b4[("<" , "^")] = True
b4[("^" , "<")] = False

b4[("A" , "v")] = True #true = optimal
b4[("v" , "A")] = False #false = optimal
b4[("^" , ">")] = False #doesn't matter????
b4[(">" , "^")] = True #true = optimal

for key in b4:
	coords = symbols_to_coords(list(key))
	if not b4[key]:
		memory_0[0][key] = ""
		for i in range( abs(coords[0])):
			vert = tuple( [ int(coords[0]/abs(coords[0])) , 0])
			memory_0[0][key] += (dict1[vert])
		for j in range(abs(coords[1])):
			hor =tuple( [0, int(coords[1]/abs(coords[1])) ])
			memory_0[0][key] += (dict1[hor])
		memory_0[0][key] += ("A")
	else:
		memory_0[0][key] = ""
		for j in range(abs(coords[1])):
			hor =tuple( [0, int(coords[1]/abs(coords[1])) ])
			memory_0[0][key] += (dict1[hor])
		for i in range( abs(coords[0])):
			vert = tuple( [ int(coords[0]/abs(coords[0])) , 0])
			memory_0[0][key] += (dict1[vert])
		memory_0[0][key] += ("A")

for key in b:
	coords = letters_to_coords(list(key))
	if b[key] == True:
		memory[0][key] = ""
		for i in range( abs(coords[0])):
			vert = tuple( [ int(coords[0]/abs(coords[0])) , 0])
			memory[0][key] += (dict1[vert])
		for j in range(abs(coords[1])):
			hor =tuple( [0, int(coords[1]/abs(coords[1])) ])
			memory[0][key] += (dict1[hor])
		memory[0][key] += ("A")
	else:
		memory[0][key] = ""
		for j in range(abs(coords[1])):
			hor =tuple( [0, int(coords[1]/abs(coords[1])) ])
			memory[0][key] += (dict1[hor])
		for i in range( abs(coords[0])):
			vert = tuple( [ int(coords[0]/abs(coords[0])) , 0])
			memory[0][key] += (dict1[vert])
		memory[0][key] += ("A")

def get_result(input):
	summest = 0
	cur_charest = "A"
	for lin in input:
		resultest = ""
		reset_positions()
		numberest = 0
		numest = int(lin.strip("A\n"))
		for charest in lin.strip("\n"):
			target_charest = charest
			resultest += memory[dim-2][tuple([cur_charest , target_charest])]
			cur_charest = charest
		print(len(resultest))
		for charest in resultest:
			target_charest = charest
			numberest += len(memory_0[dim-2][tuple([cur_charest , target_charest])])
			cur_charest = charest
		summest += numberest*numest
		print(numberest)
	print(summest)

with open('input21.txt') as fin:
	dim = 14
	global cur_pos
	cur_pos = [ [3,2],[0,2],[0,2],[0,2]]
	global cur_char
	cur_char = "A"

	finalest_sum = 0
	reset_positions()
	for c in range(1,dim-1):
		memory.append({})
		memory_0.append({})
		for key in memory[0]:
			reset_positions()
			memory[c][key] = ""
			for char in memory[c-1][key]:
				target_char = char
				memory[c][key] += memory_0[0][tuple([cur_char , target_char])]
				cur_char = char #####
		for key in memory_0[0]:
			reset_positions()
			memory_0[c][key] = ""
			for char in memory_0[c-1][key]:
				target_char = char
				memory_0[c][key] += memory_0[0][tuple([cur_char , target_char])]
				cur_char = char
	in_put = []
	for line in fin:
		in_put.append(line.rstrip("\n"))
		min_sum = float('inf')

		result = ""
		reset_positions()
		number = 0
		num = int(line.strip("A\n"))
		for char in line.strip("\n"):
			target_char = char
			result += memory[dim-2][tuple([cur_char , target_char])]
			cur_char = char

	#	print(len(result))
		for char in result:
			target_char = char
			number += len(memory_0[dim-2][tuple([cur_char , target_char])])
			cur_char = char
		#print(number)
		finalest_sum += number*num
	#	print(number*num)

	print(finalest_sum)
