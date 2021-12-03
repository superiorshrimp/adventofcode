def ex1(lines):
    depth, horizontal = 0, 0
    for i in range(len(lines)):
        if lines[i][0][0] == 'f':
            horizontal += int(lines[i][1])
        elif lines[i][0][0] == 'd':
            depth += int(lines[i][1])
        else:
            depth -= int(lines[i][1])
    return depth*horizontal

def ex2(lines):
    horizontal, depth, aim = 0, 0, 0
    for i in range(len(lines)):
        if lines[i][0][0] == 'f':
            horizontal += int(lines[i][1])
            depth += aim*int(lines[i][1])
        elif lines[i][0][0] == 'd':
            aim += int(lines[i][1])
        else:
            aim -= int(lines[i][1])
    return depth*horizontal
    
with open('./2/data.txt', 'r') as f:
    lines = [row.split() for row in f]

print(ex1(lines))
print(ex2(lines))