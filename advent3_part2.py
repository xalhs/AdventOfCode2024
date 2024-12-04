with open('input3.txt') as fin:
	sum = 0
	active = True
	for line in fin:
		print(active)
		first_split = line.split("don't()")
		if active == True:
			active_seg = first_split[0]
			first_split.pop(0)
		else:
			active_seg= ""	
		for part1 in first_split:
			try:
				second_split = part1.split("do()" , 1)[1]
				active_seg += "."+second_split
			except:
				pass
		if "do()" in first_split[-1]:
			active = True
		else:
			active = False			
		seg1 = active_seg.split("mul(")[1:]
		for part in seg1:
			inside = part.split(")",1)[0]
			inps = inside.split(",",1)
			try:
				inp1 = int(inps[0])
				inp2 = int(inps[1])
				sum += inp1*inp2
			except:
				pass
	print(sum)
