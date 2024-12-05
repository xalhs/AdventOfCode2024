def reorder(number_list , rules_list):
	curated_rules_list = []
	for rule in rules_list:
		if rule[0] in number_list and rule[1] in number_list:
			curated_rules_list.append(rule)
	o_dict = {}
	for numb in number_list:
		o_dict[numb] = []		
	for rule in curated_rules_list:
		o_dict[rule[0]].append(rule[1])		

	max_el = rule[1]
	while len(o_dict[max_el]) >0:
		max_el = o_dict[max_el][0]
		
	max_el = rule[1]
	ordering = []
	while len(number_list) > len(ordering):
		if all(x in ordering for x in o_dict[max_el]):
			ordering.insert(0,max_el)
			if len(number_list) == len(ordering):
				break
			max_el = [x for  x in number_list if x not in ordering][0]
		else:
			max_el = [x for  x in o_dict[max_el] if x not in ordering][0] 	
	return ordering			

def is_valid(number_list , rules_list):
	valid = True
	dict1 = {}
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
	return valid						


with open('input5.txt') as fin:
	line_list = []
	sum = 0
	rules_list = []
	for line in fin:
		if line == "\n":
			break
		line_list = line.rstrip("\n").split("|")
		rules_list.append(line_list)
	for line in fin:
		valid = True
		number_list = line.rstrip("\n").split(",")
		if not is_valid(number_list , rules_list):
			ordering = reorder(number_list , rules_list)
			sum += int(ordering[int(len(ordering)/2)])
	print(sum)


