# f = open("Day2/testInput2.txt", "r")
f = open("Day2/input2.txt", "r")
listOfSum = []
i = 0
data = f.read().splitlines()
for line in data:
    minimum = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    i+=1
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
            for key in minimum:
                if line[1].startswith(key):
                    if lastNumber > minimum[key]:
                        minimum[key] = lastNumber
        line[1] = line[1][1:]
    sumOfMinimum = minimum["red"] * minimum["green"] * minimum["blue"]
    listOfSum.append(sumOfMinimum)
    
total = 0
for item in listOfSum:
    total += item
print(total)

    
