def instruction(instruc, operand):
    global dict1
    global pointer
    global A
    global B
    global C
    global output
    global outputstr
    combo = {0:0 , 1:1 , 2:2 , 3:3 , 4:A , 5:B , 6:C}
    if instruc == 0:
        val = int(A/(2**combo[operand]))
        A= val
    if instruc == 1:
        B = B^operand
    if instruc == 2:
        B = combo[operand]%8
    if instruc == 3:
        if A != 0:
            pointer = operand-2
    if instruc == 4:
        B = B^C
    if instruc == 5:
        outputstr += str(combo[operand]%8)+","
        output.append(combo[operand]%8)
    if instruc == 6:
        val = int(A/(2**combo[operand]))
        B= val
    if instruc == 7:
        val = int(A/(2**combo[operand]))
        C= val

    pointer +=2

def run_for_A(value):
    global pointer
    global A
    global outputstr
    outputstr = ""
    global B
    global C
    B= 0
    C = 0
    A = value
    pointer = 0
    global program
    while pointer < len(program):
        instruction(program[pointer] , program[pointer+1])

    print(outputstr.rstrip(","))

with open('input17.txt') as fin:
    global dict1
    global A
    global B
    global C
    global output
    output = []
    global outputstr
    outputstr = ""
    dict1 = {"A" :0 , "B": 0 , "C":0}
    for line in fin:
        if line =="\n":
            break
        dict1[line.split(":")[0].split(" ")[1]] = int(line.strip("\n").split(" ")[2]    )

    B = dict1["B"]
    C = dict1["C"]
    global program
    for line in fin:
        program = [int(x) for x in line.strip("\n").split(" ")[1].split(",")]
        global pointer
        pos_vals1 =[""]
        pos_vals2 = [""]
        for digit in range(1,17):
            pos_vals1 = pos_vals2
            pos_vals2 = []
            for j,num in enumerate(pos_vals1):
                for i in range(8):
                    A = int(num + str(i) , 8)
                    output = []
                    B = dict1["B"]
                    C = dict1["C"]
                    pointer = 0
                    while pointer < len(program):
                        instruction(program[pointer] , program[pointer+1])
                    if output == program[-digit:]:
                        pos_vals2.append( num+ str(str(oct(i)).split("o")[1]))
                        #continue
        print(int(pos_vals2[0] , 8))
