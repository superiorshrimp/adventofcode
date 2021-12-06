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

def ex1(fish, days = 80):
    stack = Stack()
    counter = len(fish)
    for f in fish:
        stack.put([0, f]) #0 - day of birth
    while stack.empty() is False:
        (b,f) = stack.get()
        if b+f+1<=days:
            counter += 1
            stack.put((b+f+1, 8))
        for i in range(b+f+8, days+1, 7):
            counter += 1
            stack.put((i, 8))
    return counter

def ex2(fish, days = 256):
    day = [0 for _ in range(9)]
    for f in fish:
        day[f] += 1
    for i in range(days):
        rem = day[0]
        for j in range(8):
            day[j] = day[j+1]
        day[8] = rem
        day[6] += rem
    return sum(day)

with open("./6/data.txt", "r") as f:
    input = [row.split(",") for row in f]
    input = [int(el) for el in input[0]]

print(ex1(input))
print(ex2(input))