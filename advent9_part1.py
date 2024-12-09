with open('input9.txt') as fin:
    dict1 = {}

    antinodes = []
    uncompact = []
    for line in fin:
        i=0
        for char in line.rstrip('\n'):
            if i%2 == 0:
                uncompact+= [str(int(i/2))]*int(char)
            else:

                uncompact+= ["."]*int(char)
            i+=1
    uncompact += "."
    for j in range(len(uncompact)):
        if not uncompact[-j-1] == ".":
            position = uncompact.index(".")
            if position > len(uncompact) -j -1:
                break

            uncompact = uncompact[:position] +[ uncompact[-j-1] ]+ uncompact[position+1:-j-1]+ ["."]+ uncompact[-j:]

    sum = 0
    for k in range(len(uncompact)):
        if uncompact[k] == ".":
            break
        sum += k*int(uncompact[k])
    print(sum)
