class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Stack:
    def __init__(self):
        self.top=None
        self.count=0
    def stack_size(self):
        return self.count
    def empty(self):
        if self.count==0:
            return True
        else:
            return False
    def get(self):
        if self.stack_size()!=0:
            element=self.top
            self.top=element.next
            self.count-=1
            return element.val
    def put(self, element):
        new=Node(element)
        if self.stack_size()!=0:
            element=self.top
            new.next=element
            self.top=new
            self.count+=1
        else:
            self.count=1
            self.top=new

def minimum(tab, row, col):
    if tab[row][col] == 9:
        return 0
    if row == 0:
        if col == 0:
            if tab[row][col] < tab[row][col+1] and tab[row][col] < tab[row+1][col]:
                return tab[row][col] + 1
        elif col == len(tab[0])-1:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row+1][col]:
                return tab[row][col] + 1
        else:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row+1][col] and tab[row][col] < tab[row][col+1]:
                return tab[row][col] + 1
    elif row == len(tab)-1:
        if col == 0:
            if tab[row][col] < tab[row][col+1] and tab[row][col] < tab[row-1][col]:
                return tab[row][col] + 1
        elif col == len(tab[0])-1:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row-1][col]:
                return tab[row][col] + 1
        else:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row-1][col] and tab[row][col] < tab[row][col+1]:
                return tab[row][col] + 1
    else:
        if col == 0:
            if tab[row][col] < tab[row][col+1] and tab[row][col] < tab[row-1][col] and tab[row][col] < tab[row+1][col]:
                return tab[row][col] + 1
        elif col == len(tab[0])-1:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row-1][col] and tab[row][col] < tab[row+1][col]:
                return tab[row][col] + 1
        else:
            if tab[row][col] < tab[row][col-1] and tab[row][col] < tab[row-1][col] and tab[row][col] < tab[row][col+1] and tab[row][col] < tab[row+1][col]:
                return tab[row][col] + 1
    return 0

def DFS(tab, i, j, visited):
    stack = Stack()
    stack.put((i,j))
    counter = 1
    moves = ((0,1), (1,0), (-1,0), (0,-1))
    while stack.empty() is False:
        el = stack.get()
        for move in moves:
            nrow = el[0]+move[0]
            ncol = el[1]+move[1]
            if 0<=nrow<len(tab) and 0<=ncol<len(tab[0]) and not visited[nrow][ncol] and tab[nrow][ncol] != 9:
                stack.put((nrow,ncol))
                counter += 1
                visited[nrow][ncol] = True
    return counter

def ex1(tab):
    sum = 0
    for row in range(len(rows)):
        for col in range(len(rows[0])):
            sum += minimum(tab, row, col)
    return sum

def ex2(tab):
    visited = [[False for col in range(len(tab[0]))] for row in range(len(tab))]
    biggest = [0,0,0]
    for row in range(len(tab)):
        for col in range(len(tab[0])):
            if not visited[row][col] and tab[row][col] != 9:
                visited[row][col] = True
                res = DFS(tab, row, col, visited)
                biggest.append(res)
                biggest.sort()
                del biggest[0]
    return biggest[0]*biggest[1]*biggest[2]

with open("./9/data.txt", "r") as f:
    rows = [[int(row[i]) for i in range(len(row)-1)] for row in f]

print(ex1(rows))
print(ex2(rows))