numbers = []
first = -1
last = -1
total = 0
rename = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

f = open("Day1/input.txt", "r")
data = f.read().splitlines()
print(data)

for line in data:
    first = -1
    last = -1
    for x in range(len(line)):
        if line[0].isdigit():
            if first == -1:
               first = int(line[0])
            else:
               last = int(line[0])
        else:
            for key in rename:
                if line.startswith(key):
                    if first == -1:
                        first = rename[key]
                    else:
                        last = rename[key]
        line = line[1:]
        
    if last == -1:
        last = first
    numbers.append(f"{first}{last}")

for number in numbers:
    total += int(number)
print(total)