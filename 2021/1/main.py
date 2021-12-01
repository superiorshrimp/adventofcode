def ex1(file):
    with open(file, "r") as file:
        lines = [int(row) for row in file]
    counter = 0
    for i in range(1,len(lines)):
        if lines[i]>lines[i-1]:
            counter+=1
    return counter

def ex2(file):
    with open(file, "r") as file:
        lines = [int(row) for row in file]
    counter = 0
    for i in range(len(lines)-3):
        if lines[i+3] > lines[i]:
            counter +=1
    return counter

print(ex1('./1/data.txt'))
print(ex2('./1/data.txt'))