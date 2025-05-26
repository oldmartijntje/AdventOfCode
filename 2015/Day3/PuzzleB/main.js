var tempPuzzleInput = puzzleInput;
console.log(tempPuzzleInput);

let x1 = 0;
let x2 = 0;
let y1 = 0;
let y2 = 0;
let roboMove = true;
let presentLocations = {}
presentLocations[`${x1}.${y1}`] = 1;

for (let index = 0; index < tempPuzzleInput.length; index++) {
    roboMove = !roboMove;
    const element = tempPuzzleInput[index];
    console.log(element)
    switch (element) {
        case "^":
            if (roboMove) {
                y1 += 1;
            } else {
                y2 += 1;
            }
            break;
        case "v":
            if (roboMove) {
                y1 -= 1;
            } else {
                y2 -= 1;
            }
            break;
        case "<":
            if (roboMove) {
                x1 -= 1;
            } else {
                x2 -= 1;
            }
            break;
        case ">":
            if (roboMove) {
                x1 += 1;
            } else {
                x2 += 1;
            }
            break;
        default:
            alert("error")
            break;
    }
    if (roboMove) {
        if (presentLocations[`${x1}.${y1}`] == undefined) {
            presentLocations[`${x1}.${y1}`] = 1;
        } else {
            presentLocations[`${x1}.${y1}`] += 1;
        }
    } else {
        if (presentLocations[`${x2}.${y2}`] == undefined) {
            presentLocations[`${x2}.${y2}`] = 1;
        } else {
            presentLocations[`${x2}.${y2}`] += 1;
        }
    }

}
alert(Object.keys(presentLocations).length)