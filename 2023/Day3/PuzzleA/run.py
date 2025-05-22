f = open("2023/Day3/PuzzleA/input.txt", "r")
characters = {'.': 15297, '7': 386, '8': 365, '5': 356, 
              '4': 371, '0': 235, '1': 354, '2': 387, 
              '9': 347, '3': 374, '\n': 140, '/': 41, 
              '*': 390, '6': 361, '&': 56, '+': 34, 
              '$': 54, '-': 47, '%': 38, '=': 33, 
              '@': 36, '#': 38}

isNotCharacter = "0123456789."

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
    if y > len(map) or y < 0:
        return None
    if x > len(map[y]) or x < 0:
        return None
    return map[y][x]

# CountAllCharacters(f.read())
rows = f.read().split("\n")
print(IsAdjacent(0, 0, rows))
# print(rows)