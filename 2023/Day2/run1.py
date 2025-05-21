# f = open("Day2/testInput1.txt", "r")
f = open("Day2/input1.txt", "r")
maximum = {
    "red": 12,
    "green": 13,
    "blue": 14
} 
possible = 0
i = 0
data = f.read().splitlines()
for line in data:
    i+=1
    thisGameIsPossible = True
    line = line.split(": ")
    lastNumber = -1
    skip = 0
    for x in range(len(line[1])):
        if line[1][0].isdigit():
            if skip != 0:
                skip -= 1
            else:
                splitted = line[1].split(" ")
                skip = len(splitted[0]) -1
                lastNumber = int(splitted[0])
        else:
            for key in maximum:
                if line[1].startswith(key):
            
                    if lastNumber > maximum[key]:
                        thisGameIsPossible = False
        line[1] = line[1][1:]
    if thisGameIsPossible:
        print(f"Game {i} is possible")
        possible += i

print(possible)

    
