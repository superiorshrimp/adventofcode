def req_fuel(crabs, loc):
    suma = 0
    for key in crabs.keys():
        suma += crabs.get(key)*arithm_sum(0, abs(key-loc))
    return suma

def distribute(locations):
    minimum, maksimum = locations[0], locations[0]
    crabs_at = {}
    counter = 1
    for i in range(1,len(locations)):
        minimum, maksimum = min(minimum, locations[i]), max(maksimum, locations[i])
        if locations[i] == locations[i-1]:
            counter += 1
        else:
            crabs_at[locations[i-1]] = counter
            counter = 1
    if locations[len(locations)-1] == locations[len(locations)-2]:
        crabs_at[locations[len(locations)-1]] = counter + 1
    else:
        crabs_at[locations[len(locations)-2]] = counter
        crabs_at[locations[len(locations)-1]] = 1
    return crabs_at, minimum, maksimum

def arithm_sum(x, cmedian): #from crab median
    return (1+abs(cmedian-x))*abs(cmedian-x)//2

def ex1(locations):
    locations.sort()
    median = locations[len(locations)//2]
    return sum( [ abs(loc-median) for loc in locations] )

def ex2(locations):
    locations.sort()
    median = locations[len(locations)//2]
    crabs, minimum, maksimum = distribute(locations)
    left, right = 0, 0
    for key in crabs.keys():
        if key < median:
            left += crabs.get(key)*arithm_sum(median-key, median)
        elif key > median:
            right += crabs.get(key)*arithm_sum(median, median+key)
    fuel = left + right
    for crab_median in range(minimum, maksimum + 1):
        fuel = min(fuel, req_fuel(crabs, crab_median))
    return fuel
    
 
with open("./7/data.txt", "r") as f:
    input = [row.split(",") for row in f]
    input = [int(el) for el in input[0]]

print(ex1(input))
print(ex2(input))    