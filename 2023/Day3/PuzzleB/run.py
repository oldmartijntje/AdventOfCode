f = open("2023/Day3/PuzzleA/input.txt", "r")
characters = {'.': 15297, '7': 386, '8': 365, '5': 356, 
              '4': 371, '0': 235, '1': 354, '2': 387, 
              '9': 347, '3': 374, '\n': 140, '/': 41, 
              '*': 390, '6': 361, '&': 56, '+': 34, 
              '$': 54, '-': 47, '%': 38, '=': 33, 
              '@': 36, '#': 38}

isNotCharacter = "0123456789."
isNumber = "0123456789"
total = 0
lastOneWasNumber = False
currentWord = ""
multipliers = {}
isMultiplier = False
currGearId = 0
gearIds = {}

def IsAdjacent(x, y, map):
    isAdjacent = False
    for xi in range(3):
        for yi in range(3):
            char = GetCoordinate(xi -1 + x, yi -1 + y, map)
            if char == None:
                pass
            elif f"{char}" not in isNotCharacter:
                isAdjacent = True
    return isAdjacent

def MarkAdjacent(x, y, gearId, map, multipliers):
    for xi in range(3):
        for yi in range(3):
            char = GetCoordinate(xi -1 + x, yi -1 + y, map)
            if char == None:
                pass
            elif f"{char}" in isNumber:
                multipliers[f"{xi -1 + x}.{yi -1 + y}"] = gearId
    return multipliers



def CountAllCharacters(string):
    registry = {}
    for x in range(len(string)):
        char = string[x]
        if char not in registry:
            registry[char] = 1
        else:
            registry[char] += 1

def GetCoordinate(x,y, map):
    if y > len(map) -1 or y < 0:
        return None
    if x > len(map[y]) -1 or x < 0:
        return None
    return map[y][x]

rows = f.read().split("\n")
gearId = 0
for row in range(len(rows)):
    for char in range(len(rows[row])):
        character = rows[row][char]
        if character == "*":
            multipliers = MarkAdjacent(char, row, gearId, rows, multipliers)
            gearId+=1

for row in range(len(rows)):
    for char in range(len(rows[row])):
        character = rows[row][char]
        if character in isNumber:
            currentWord += f"{character}"
            lastOneWasNumber = True
            if f"{char}.{row}" in multipliers:
                isMultiplier = True
                currGearId = multipliers[f"{char}.{row}"]
        else:
            if lastOneWasNumber == True or currentWord != "":
                lastOneWasNumber = False
                found = False
                for length in range(len(currentWord)):
                    if IsAdjacent(char - length -1, row, rows):
                        found = True
                if isMultiplier:
                    if currGearId in gearIds:
                        gearIds[currGearId]["nr2"] = int(currentWord)
                    else:
                        gearIds[currGearId] = {
                            "nr1": int(currentWord),
                            "nr2": None
                        }
                elif found == True:
                    # total += int(currentWord)
                    pass
                currentWord = ""
                isMultiplier = False
                currGearId = 0
            else:
                pass
    if lastOneWasNumber == True or currentWord != "":
        lastOneWasNumber = False
        found = False
        for length in range(len(currentWord)):
            if IsAdjacent(char - length -1, row, rows):
                found = True
        if isMultiplier:
            if currGearId in gearIds:
                gearIds[currGearId]["nr2"] = int(currentWord)
            else:
                gearIds[currGearId] = {
                    "nr1": int(currentWord),
                    "nr2": None
                }
        elif found == True:
            # total += int(currentWord)
            pass
        currentWord = ""

for item in gearIds.keys():
    # print(gearIds[item])
    if gearIds[item]["nr2"] == None:
        # total += gearIds[item]["nr1"]
        pass
    else:
        total += (gearIds[item]["nr1"] * gearIds[item]["nr2"])

print(total)