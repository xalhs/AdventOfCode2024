def  pos_finder(list1 , size):
    for i,item in enumerate(list1):
        if item[0] == "." and item[1]>= size:
            return i
    return False

with open('input9.txt') as fin:
    dict1 = {}

    antinodes = []
    uncompact = []
    for line in fin:
        i=0
        for char in line.rstrip('\n'):
            if i%2 == 0:
                uncompact.append([str(int(i/2)) , int(char)])
            else:

                uncompact.append(["." , int(char)])
            i+=1
    uncompact.append( ["." , 1])
    length = len(uncompact)
    disallowed_val = 10
    for j in range(2*length):
        if j >= len(uncompact):
            break
        if not uncompact[-j-1][0] == ".":
            if disallowed_val <= uncompact[-j-1][1]:
                continue
            position = pos_finder(uncompact ,uncompact[-j-1][1] )
            position2 = uncompact.index(uncompact[-j-1])
            if position != False and position < position2:
                temp = uncompact[-j-1][0]
                uncompact[-j-1][0] = "."
                # if False or uncompact[position][1] == uncompact[-j-1][1]: #This part would check whether the block of dots would entirely disappear and if so it would remove it but it is not needed
                #     uncompact[position][0] = temp
                # else:
                #     uncompact[position][1] -= uncompact[-j-1][1]   #the code would work perfectly with only the part here
                #     uncompact = uncompact[:position] +[[ temp , uncompact[-j-1][1] ]]+ uncompact[position:]
                uncompact[position][1] -= uncompact[-j-1][1]
                uncompact = uncompact[:position] +[[ temp , uncompact[-j-1][1] ]]+ uncompact[position:]
            else:
                if uncompact[-j-1][1] < disallowed_val:
                    disallowed_val = uncompact[-j-1][1]

    sum = 0
    index = 0
    for k in range(len(uncompact)):
        if uncompact[k][0] == ".":
            index += uncompact[k][1]
            continue
        for l in range(uncompact[k][1]):
            sum += index*int(uncompact[k][0])
            index+=1
    print(sum)
