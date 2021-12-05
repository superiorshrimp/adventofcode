
def ex1(lines):
    Map = {} #Map is a dictionary: {key = (x,y); value = counter}
    counter = 0
    for line in lines:
        if line[0] == line[2]: #vertical
            x = line[0]
            for y in range(min(line[1],line[3]), max(line[1],line[3])+1):
                if (x,y) not in Map:
                    Map[(x,y)] = 1
                elif Map.get((x,y)) == 1:
                    counter += 1
                    Map.pop((x,y))
                    Map[(x,y)] = 2
        elif line[1] == line[3]: #horizontal
            y = line[1]
            for x in range(min(line[0],line[2]), max(line[0],line[2])+1):
                if (x,y) not in Map:
                    Map[(x,y)] = 1
                elif Map.get((x,y)) == 1:
                    counter += 1
                    Map.pop((x,y))
                    Map[(x,y)] = 2
    return counter

def ex2(lines):
    Map = {} #Map is a dictionary: {key = (x,y); value = counter}
    counter = 0
    for line in lines:
        if line[0] == line[2]: #vertical
            x = line[0]
            for y in range(min(line[1],line[3]), max(line[1],line[3])+1):
                if (x,y) not in Map:
                    Map[(x,y)] = 1
                elif Map.get((x,y)) == 1:
                    counter += 1
                    Map.pop((x,y))
                    Map[(x,y)] = 2
        elif line[1] == line[3]: #horizontal
            y = line[1]
            for x in range(min(line[0],line[2]), max(line[0],line[2])+1):
                if (x,y) not in Map:
                    Map[(x,y)] = 1
                elif Map.get((x,y)) == 1:
                    counter += 1
                    Map.pop((x,y))
                    Map[(x,y)] = 2
        elif abs(line[0]-line[1]) == abs(line[2]-line[3]) or line[0]+line[1] == line[2]+line[3]: #diagonal
            if line[0]<line[2]:
                x = line[0]
                y = line[1]
                if line[1]<line[3]: #diag from left down to right up
                    for i in range(abs(x-line[2])+1):
                        if (x+i, y+i) not in Map:
                            Map[(x+i,y+i)] = 1
                        elif Map.get((x+i,y+i)) == 1:
                            counter += 1
                            Map.pop((x+i,y+i))
                            Map[(x+i,y+i)] = 2
                else: #diag from left up to right down
                    for i in range(abs(x-line[2])+1):
                        if (x+i, y-i) not in Map:
                            Map[(x+i,y-i)] = 1
                        elif Map.get((x+i,y-i)) == 1:
                            counter += 1
                            Map.pop((x+i,y-i))
                            Map[(x+i,y-i)] = 2
            else:
                x = line[2]
                y = line[3]
                if line[1]>line[3]: 
                    for i in range(abs(x-line[0])+1):
                        if (x+i, y+i) not in Map:
                            Map[(x+i,y+i)] = 1
                        elif Map.get((x+i,y+i)) == 1:
                            counter += 1
                            Map.pop((x+i,y+i))
                            Map[(x+i,y+i)] = 2
                else:
                    for i in range(abs(x-line[0])+1):
                        if (x+i, y-i) not in Map:
                            Map[(x+i,y-i)] = 1
                        elif Map.get((x+i,y-i)) == 1:
                            counter += 1
                            Map.pop((x+i,y-i))
                            Map[(x+i,y-i)] = 2
    return counter

with open('./5/data.txt', 'r') as f:
    input = [row.split() for row in f]
lines = [None for _ in range(len(input))]
for i in range(len(input)):
    lines[i] = [input[i][0].split(","), input[i][2].split(",")]
for i in range(len(input)):
    lines[i] = [int(lines[i][0][0]), int(lines[i][0][1]), int(lines[i][1][0]), int(lines[i][1][1])]

print(ex1(lines))
print(ex2(lines))