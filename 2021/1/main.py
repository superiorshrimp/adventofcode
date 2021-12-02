def ex1(lines):
    counter = 0
    for i in range(1,len(lines)):
        if lines[i]>lines[i-1]:
            counter+=1
    return counter

def ex2(lines):
    counter = 0
    for i in range(len(lines)-3):
        if lines[i+3] > lines[i]:
            counter +=1
    return counter

with open('./1/data.txt', "r") as f:
    lines = [int(row) for row in f]

print(ex1(lines))
print(ex2(lines))