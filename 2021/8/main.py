def ex1(digits, output): #digit k uses (->) n signals: 1 -> 2, 4 -> 4, 7 -> 3, 8 -> 7
    return sum( [ sum( [ 1 if len(digit) in (2,4,3,7) else 0 for digit in line] ) for line in output ] )

def ex2(digits, output):
    res = 0
    for i in range(0, len(digits)):
        lengths = {len(digit): set(digit) for digit in digits[i]} # here we only care about unique (with unique length) numbers to help us distinguish between those not unique 
        n = ''
        for number in output[i]:
            num = set(number)
            if len(num) == 2:
                n += '1'
            elif len(num) == 4:
                n += '4'
            elif len(num) == 3:
                n += '7'
            elif len(num) == 7:
                n += '8'
            elif len(num) == 6:
                if len(num.intersection(lengths.get(4))) == 4: # 4 -> 4
                    n += '9'
                elif len(num.intersection(lengths.get(2))) == 1: # 2 -> 1
                    n += '6'
                else:
                    n += '0'
            else:
                if len(num.intersection(lengths.get(4))) == 2: # 2 -> 1
                    n += '2'
                elif len(num.intersection(lengths.get(2))) == 2: # 4 -> 4
                    n += '3'
                else:
                    n += '5'
        res += int(n)
    return res
        
with open("./8/data.txt", "r") as f:
    lines = [row.split("|") for row in f]
    digits = [line[0].split() for line in lines]
    output = [line[1].split() for line in lines]

print(ex1(digits, output))
print(ex2(digits, output))
'''
digit k uses n signals [a,b,c,d,e,f,g]
0: 6
1: 2 unique
2: 5
3: 5
4: 4 unique
5: 5
6: 6
7: 3 unique
8: 7 unique
9: 6

     069
06         09
      69
069       069
     069

     235
5           23
     235
2           35
     235
'''