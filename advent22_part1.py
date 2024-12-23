with open('input22.txt') as fin:
    sum = 0
    for line in fin:
        code = int(line.strip("\n"))
        for i in range(2000):
            code = ((code*64)^code)%16777216
            code = (int(code/32)^code)%16777216
            code = ((code*2048)^code)%16777216
        sum +=code
    print(sum)
