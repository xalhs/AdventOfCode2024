def nested_loop(total, tar_val, rem_vals):
    if total > tar_val:
        return False
    if rem_vals == []:
        if total == tar_val:
            return True
        else:
            return False
    new_total = total + int(rem_vals[0])
    new_vals = rem_vals[1:]
    answer = nested_loop(new_total , tar_val , new_vals)
    if answer == True:
        return True

    new_total = total*int(rem_vals[0])
    new_vals = rem_vals[1:]
    answer = nested_loop(new_total , tar_val , new_vals)
    if answer == True:
        return True

    return False

with open('input7.txt') as fin:
    sum = 0
    for line in fin:
        parts = line.rstrip("\n").split(": ")
        tar_val = int(parts[0])
        vals = parts[1].split(" ")
        total = 0
        opers = ["" for i in range(len(vals)-1) ]
        if nested_loop(0 , tar_val , vals )== True:
            sum += tar_val
    print(sum)
