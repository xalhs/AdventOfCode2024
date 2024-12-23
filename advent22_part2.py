with open('input22.txt') as fin:
    sum = 0
    import copy
    dict = {}
    for line in fin:
        last_four = []
        flag = {}
        code = int(line.strip("\n"))
        for i in range(2000):
            prev_code = copy.copy(code)
            code = ((code*64)^code)%16777216
            code = (int(code/32)^code)%16777216
            code = ((code*2048)^code)%16777216
            dif = code%10 - prev_code%10
            last_four.append(dif)
            if len(last_four) > 4:
                last_four.pop(0)
            if len(last_four) == 4:
                if tuple(last_four) in dict:
                    if not tuple(last_four) in flag:
                        dict[tuple(last_four)] += code%10
                        flag[tuple(last_four)] = True
                else:
                    dict[tuple(last_four)]  = code%10
                    flag[tuple(last_four)] = True
    max_banan = 0
    max_key = ""
    for key in dict:
        if dict[key] > max_banan:
            max_banan = dict[key]
            max_key = key

    print(max_banan)
