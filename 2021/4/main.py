def sum_missing(seq, arr):
    suma = 0
    for row in arr:
        suma += sum(row)
    for el in seq:
        for row in arr:
            if el in row:
                suma -= el
    return suma

def ex1(seq, lines):
    min, max = seq[0], seq[0] #you can see that in this game the seq numbers are in a rather small range 
    for num in seq:
        if num<min:
            min = num
        elif num>max:
            max = num
    numbers = [[] for _ in range(max-min)]
    for row in range(len(lines)):
        for col in range(5):
            numbers[lines[row][col]-min-1].append([row, col])
    row_found = [0 for _ in range(len(lines))]
    col_found = [0 for _ in range(len(lines))]
    i = 0
    for num in seq:
        for coord in numbers[num-min-1]:
            row_found[coord[0]] += 1
            col_found[5*(coord[0]//5) + coord[1]] +=1
            if row_found[coord[0]] == 5 or col_found[5*(coord[0]//5) + coord[1]] == 5:
                return num*sum_missing(seq[:i+1], lines[5*(coord[0]//5):5*(coord[0]//5) +5])
        i+=1

def ex2(seq, lines):
    min, max = seq[0], seq[0] #you can see that in this game the seq numbers are in a rather small range    
    for num in seq:
        if num<min:
            min = num
        elif num>max:
            max = num
    numbers = [[] for _ in range(max-min)]
    for row in range(len(lines)):
        for col in range(5):
            numbers[lines[row][col]-min-1].append([row, col])
    boards = [0 for _ in range(len(lines)//5)] # 1 = won
    row_found = [0 for _ in range(len(lines))]
    col_found = [0 for _ in range(len(lines))]
    i = 0
    ended = 0
    for num in seq:
        for coord in numbers[num-min-1]:
            if boards[coord[0]//5] == 0:
                row_found[coord[0]] += 1
                col_found[5*(coord[0]//5) + coord[1]] +=1
                if row_found[coord[0]] == 5 or col_found[5*(coord[0]//5) + coord[1]] == 5:
                    boards[coord[0]//5] = 1
                    ended += 1
                    if ended == len(boards):
                        return num * sum_missing(seq[:i+1], lines[5*(coord[0]//5):5*(coord[0]//5) +5])
        i+=1    
    

with open('./4/data.txt', 'r') as f:
    temp = [row.split() for row in f]

seq = temp[0][0].split(",")
seq = [int(seq[i]) for i in range(len(seq))]

lines = [None for _ in range(5*len(temp)//6)]
j = 0
for i in range(1,len(temp)):
    if i%6 != 1:
        lines[j] = [int(temp[i][k]) for k in range(5)]
        j += 1

print(ex1(seq, lines))
print(ex2(seq, lines))