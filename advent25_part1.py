with open('input25.txt') as fin:
    sum = 0
    i = 0
    patterns = []
    patterns.append([])
    locks = []
    keys = []
    keys_stats = []
    locks_stats = []
    for line in fin:
        if line == "\n":
            patterns.append([])
            i+=1
            continue
        patterns[i].append(line.rstrip("\n"))

    for pattern in patterns:
        if pattern[0] == "."*len(pattern[0]):
            keys.append(pattern)
            stats = []
            for row in list(map(list, zip(*pattern))):
                stats.append(row.count("#"))
            keys_stats.append(stats)

        else:
            locks.append(pattern)
            stats = []
            for row in list(map(list, zip(*pattern))):
                stats.append(row.count("#"))
            locks_stats.append(stats)

    for key in keys_stats:
        for lock in locks_stats:
            fit = True
            for i in range(len(key)):
                if key[i]+lock[i] > 7:
                    fit = False
            if fit:
                sum+=1

    print(sum)
