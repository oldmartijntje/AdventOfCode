var tempPuzzleInput = puzzleInput;
function countInstances(string, word) {
    return string.split(word).length - 1;
}

alert(countInstances(tempPuzzleInput, "(") - countInstances(tempPuzzleInput, ")"))