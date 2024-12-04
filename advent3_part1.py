with open('input3.txt') as fin:
	sum = 0
	for line in fin:
		seg1 = line.split("mul(")[1:]
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
