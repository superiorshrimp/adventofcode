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

def in_range(tab, row, col):
    return 0<=row<len(tab) and 0<=col<len(tab[0])

def ex1(tab):
    s = 0
    moves = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
    for step in range(100):
        visited = [[False for j in range(len(tab[0]))] for i in range(len(tab))]
        stack = Stack()
        for i in range(len(tab)):
            for j in range(len(tab)):
                tab[i][j] += 1
                if tab[i][j] > 9:
                    stack.put((i,j))
                    visited[i][j] = True
        while stack.empty() is False:
            s += 1
            (row,col) = stack.get()
            tab[row][col] = 0
            for move in moves:
                nrow = row + move[0]
                ncol = col + move[1]
                if in_range(tab, nrow, ncol) and not visited[nrow][ncol]:
                    tab[nrow][ncol] += 1
                    if tab[nrow][ncol] > 9:
                        visited[nrow][ncol] = True
                        stack.put((nrow,ncol))
    return s

def ex2(tab):
    n = len(tab)*len(tab[0]) #number of octopuses
    moves = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
    for step in range(1000):
        s = 0
        visited = [[False for j in range(len(tab[0]))] for i in range(len(tab))]
        stack = Stack()
        for i in range(len(tab)):
            for j in range(len(tab)):
                tab[i][j] += 1
                if tab[i][j] > 9:
                    stack.put((i,j))
                    visited[i][j] = True
        while stack.empty() is False:
            s += 1
            (row,col) = stack.get()
            tab[row][col] = 0
            for move in moves:
                nrow = row + move[0]
                ncol = col + move[1]
                if in_range(tab, nrow, ncol) and not visited[nrow][ncol]:
                    tab[nrow][ncol] += 1
                    if tab[nrow][ncol] > 9:
                        visited[nrow][ncol] = True
                        stack.put((nrow,ncol))
        if s == n:
            return step + 1

with open("./11/data.txt", "r") as f:
    rows = f.read().splitlines()
    rows = [[int(rows[i][j]) for j in range(len(rows[0]))] for i in range(len(rows))]
    rows_copy = [[rows[i][j] for j in range(len(rows[0]))] for i in range(len(rows))]

print(ex1(rows))
print(ex2(rows_copy))