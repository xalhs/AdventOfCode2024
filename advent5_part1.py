with open('input5.txt') as fin:
	line_list = []
	sum = 0
	rules_list = []
	for line in fin:
		rules_list.append(line.rstrip("\n").split("|"))
		if line == "\n":
			break
	for line in fin:
		valid = True
		dict1 = {}
		number_list = line.rstrip("\n").split(",")
		for i,num in enumerate(number_list):
			dict1[num] = i
		for rule in rules_list:
			try:
				if dict1[rule[0]] < dict1[rule[1]]:
					pass
				else:
					valid = False
					break	
			except:
				pass		
		if valid == True:
			sum += int(number_list[int(len(number_list)/2)])
	print(sum)
