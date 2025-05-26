var tempPuzzleInput = puzzleInput;
console.log(tempPuzzleInput);

let x = 0;
let y = 0;
let presentLocations = {}
presentLocations[`${x}.${y}`] = 1;

for (let index = 0; index < tempPuzzleInput.length; index++) {
    const element = tempPuzzleInput[index];
    console.log(element)
    switch (element) {
        case "^":
            y += 1;
            break;
        case "v":
            y -= 1;
            break;
        case "<":
            x -= 1;
            break;
        case ">":
            x += 1;
            break;
        default:
            alert("error")
            break;
    }
    if (presentLocations[`${x}.${y}`] == undefined) {
        presentLocations[`${x}.${y}`] = 1;
    } else {
        presentLocations[`${x}.${y}`] += 1;
    }
}
alert(Object.keys(presentLocations).length)