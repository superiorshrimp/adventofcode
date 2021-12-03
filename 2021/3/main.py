def opposite_positive(a, length):
    return 2**length-1-a

def to_decimal(A, length):
    a = 0
    for bit_no in range(length):
        a += 2**(length-bit_no-1)*(A[bit_no]%2)
    return a

def ox_gen_rating(lines):
    i = 0
    while len(lines) != 1:
        counter = 0
        for line in lines:
            counter += int(line[i])
        if counter>=len(lines)//2 + len(lines)%2:
            condition = 1
        else:
            condition = 0
        Filter = []
        for j in range(len(lines)):
            if int(lines[j][i]) == condition:
                Filter.append(lines[j])
        lines = Filter.copy()
        i+=1
    return to_decimal([int(lines[0][j]) for j in range(len(lines[0]))], len(lines[0]))

def CO2_scr_rating(lines):
    i = 0
    while len(lines) != 1:
        counter = 0
        for line in lines:
            counter += int(line[i])
        if counter<len(lines)//2 + len(lines)%2:
            condition = 1
        else:
            condition = 0
        Filter = []
        for j in range(len(lines)):
            if int(lines[j][i]) == condition:
                Filter.append(lines[j])
        lines = Filter.copy()
        i+=1
    return to_decimal([int(lines[0][j]) for j in range(len(lines[0]))], len(lines[0]))

def ex1(lines):
    length = len(lines[0])
    counter = [0 for _ in range(length)]
    for line in lines:
        for bit_no in range(length):
            counter[bit_no] += int(line[bit_no])
            
    counter = [0 if counter[i]<len(lines)//2 else 1 for i in range(len(counter))]
    a = to_decimal(counter, length)
    return a*opposite_positive(a, length)

def ex2(lines):
    lines_cpy = [lines[i] for i in range(len(lines))]
    return ox_gen_rating(lines)*CO2_scr_rating(lines_cpy) 

with open('./3/data.txt', 'r') as f:
    lines = f.read().splitlines()

print(ex1(lines))
print(ex2(lines))