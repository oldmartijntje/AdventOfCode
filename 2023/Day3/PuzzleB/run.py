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

def CountAllCharacters(string):
    registry = {}
    for x in range(len(string)):
        char = string[x]
        if char not in registry:
            registry[char] = 1
        else:
            registry[char] += 1

    print(registry)

def GetCoordinate(x,y, map):
    if y > len(map) -1 or y < 0:
        return None
    if x > len(map[y]) -1 or x < 0:
        return None
    return map[y][x]

rows = f.read().split("\n")
for row in range(len(rows)):
    for char in range(len(rows[row])):
        character = rows[row][char]
        if character in isNumber:
            currentWord += f"{character}"
            lastOneWasNumber = True
        else:
            if lastOneWasNumber == True or currentWord != "":
                lastOneWasNumber = False
                found = False
                for length in range(len(currentWord)):
                    if IsAdjacent(char - length -1, row, rows):
                        found = True
                if found == True:
                    # print(currentWord)
                    total += int(currentWord)
                currentWord = ""
            else:
                pass
    if lastOneWasNumber == True or currentWord != "":
        lastOneWasNumber = False
        found = False
        for length in range(len(currentWord)):
            if IsAdjacent(char - length -1, row, rows):
                found = True
        if found == True:
            total += int(currentWord)
        currentWord = ""

print(total)