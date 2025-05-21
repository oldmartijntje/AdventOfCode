var tempPuzzleInput = puzzleInput;
let floor = 0;
let foundBasement = false;

for (let index = 0; index < tempPuzzleInput.length; index++) {
    if (tempPuzzleInput[0] == "(") {
        floor++;

    } else if (tempPuzzleInput[0] == ")") {
        floor--;
        if (!foundBasement && floor == -1) {
            foundBasement = true;
            alert(index + 1)
        }
    }
    tempPuzzleInput = tempPuzzleInput.substring(1);

}