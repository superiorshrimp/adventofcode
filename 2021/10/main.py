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

def ex1(rows):
    res = 0
    for row in rows:
        stack = Stack()
        for letter in row:
            if letter in ('(', '[', '{', '<'):
                stack.put(letter)
            else:
                el = stack.get()
                if letter == ')' and el != '(':
                    res += 3
                    break
                elif letter == ']' and el != '[':
                    res += 57
                    break
                elif letter == '}' and el != '{':
                    res += 1197
                    break
                elif letter == '>' and el != '<':
                    res += 25137
                    break
    return res

def ex2(rows):
    res = []
    for row in rows:
        stack = Stack()
        for letter in row.strip():
            if letter in ('(', '[', '{', '<'):
                stack.put(letter)
            else:
                el = stack.get()
                if letter == ')' and el != '(':
                    break
                elif letter == ']' and el != '[':
                    break
                elif letter == '}' and el != '{':
                    break
                elif letter == '>' and el != '<':
                    break
        else:
            s = 0
            while stack.empty() is False:
                el = stack.get()
                s *= 5
                if el == '(':
                    s += 1
                elif el == '[':
                    s += 2
                elif el == '{':
                    s += 3
                else:
                    s += 4
            res.append(s)
    res.sort()
    return res[len(res)//2]

with open("./10/data.txt", "r") as f:
    rows = [row for row in f] #[row[i] for i in range(len(row)-1)]

print(ex1(rows))
print(ex2(rows))