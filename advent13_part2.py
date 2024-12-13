with open('input13.txt') as fin:
	dict1 = {}
	sum = 0
	A = "A:"
	B = "B:"
	p = "prize"
	for line in fin:
		if line == "\n":
			D = dict1[A][0]*dict1[B][1] - dict1[B][0]*dict1[A][1]
			Dx = dict1[B][0]*dict1[p][1] - dict1[p][0]*dict1[B][1]
			Dy = dict1[A][0]*dict1[p][1] - dict1[p][0	]*dict1[A][1]
			if D == 0:
				continue
			if int(Dx/D) != Dx/D or int(Dy/D) != Dy/D:
				continue	
			moves  = [int(-Dx/D) , int(Dy/D)]
			sum += 3*moves[0] + moves[1]	
		if "Button" in line:
			dict1[line.split(" ")[1]] = [int(x) for x in line.rstrip("\n").replace(", Y" , "").split("+")[1:] ]
		elif "Prize" in line:
			dict1["prize"] = [int(x)+10000000000000 for x in  line.rstrip("\n").replace(", Y" , "").split("=")[1:] ]	
			
	D = dict1[A][0]*dict1[B][1] - dict1[B][0]*dict1[A][1]
	Dx = dict1[B][0]*dict1[p][1] - dict1[p][0]*dict1[B][1]
	Dy = dict1[A][0]*dict1[p][1] - dict1[p][0	]*dict1[A][1]
	if D == 0:
		pass
	elif int(Dx/D) != Dx/D or int(Dy/D) != Dy/D:
		pass	
	else:
		moves  = [int(-Dx/D) , int(Dy/D)]
		sum += 3*moves[0] + moves[1]		
		
	print(sum)
