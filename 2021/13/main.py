class Node:
    def __init__(self, x, y, next):
        self.x = x
        self.y = y
        self.next = next

def create_node_from_array(T):
    head = Node(T[0][0], T[0][1] , None)
    copy = head 
    for k in T[1:]:
        new = Node(k[0], k[1], None)
        copy.next = new
        copy = copy.next
    return head

def ex1(coords, operation): #works only for 1 operation
    dict = {}
    for coord in coords:
        dict[(coord[0], coord[1])] = True
    if operation[0] == 'y':
        for coord in coords:
            if coord[1] > operation[1]:
                del dict[(coord[0], coord[1])]
                if (coord[0], abs(coord[1] - 2*operation[1])) not in dict.keys():
                    dict[(coord[0], abs(coord[1] - 2*operation[1]))] = True
    else:
        for coord in coords:
            if coord[0] > operation[1]:
                del dict[(coord[0], coord[1])]
                if (abs(coord[0] - 2*operation[1]), coord[1]) not in dict.keys():
                    dict[(abs(coord[0] - 2*operation[1]), coord[1])] = True
    return len(dict.keys())

def ex2(coords, ops):
    dict = {}
    for coord in coords:
        dict[(coord[0], coord[1])] = True
    hd = create_node_from_array(coords)
    for operation in ops:
        if operation[0] == 'y':
            prev = None
            head = hd
            while head is not None:
                coord = (head.x, head.y)
                if coord[1] > operation[1]:
                    del dict[coord]
                    if (coord[0], abs(coord[1] - 2*operation[1])) not in dict.keys():
                        dict[(coord[0], abs(coord[1] - 2*operation[1]))] = True
                        head.y = abs(coord[1] - 2*operation[1])
                    else:
                        if prev is not None:
                            prev.next = head.next
                            head = head.next
                        else:
                            hd = hd.next
                            head = hd
                            prev = None
                else:
                    prev = head
                    head = head.next
        else:
            prev = None
            head = hd
            while head is not None:
                coord = (head.x, head.y)
                if coord[0] > operation[1]:
                    del dict[coord]
                    if (abs(coord[0] - 2*operation[1]), coord[1]) not in dict.keys():
                        dict[(abs(coord[0] - 2*operation[1]), coord[1])] = True
                        head.x = abs(coord[0] - 2*operation[1])
                    else:
                        if prev is not None:
                            prev.next = head.next
                            head = head.next
                        else:
                            hd = hd.next
                            head = hd
                            prev = None
                else:
                    prev = head
                    head = head.next
    minx = None
    miny = None
    for operation in ops:
        if operation[0] == 'x':
            if minx == None:
                minx = operation[1]
            else:
                minx = min(minx, operation[1])
        else:
            if miny == None:
                miny = operation[1]
            else:
                miny = min(miny, operation[1])
    board = [['.' for col in range(minx+1)] for row in range(miny+1)]
    while hd is not None:
        board[hd.y][hd.x] = '#'
        hd = hd.next
    for row in board:
        print(row)
    return None

with open("./13/data.txt", "r") as f:
    rows = f.read().splitlines()
    coords = []
    ops = []
    i = 0
    while len(rows[i]) != 0:
        coords.append(rows[i].split(","))
        i += 1
    for j in range(i+1, len(rows)):
        ops.append(rows[j].split()[2].split("="))
    coords = [[int(el[0]), int(el[1])] for el in coords]
    ops = [[el[0], int(el[1])] for el in ops]

print(ex1(coords, ops[0]))
ex2(coords, ops) #result may not be visible after copying to vscode, but for me works after copying to notepad