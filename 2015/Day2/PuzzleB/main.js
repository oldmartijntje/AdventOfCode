var tempPuzzleInput = puzzleInput;
console.log(tempPuzzleInput);

function secondSmallestElement(arr) {
    arr.sort((a, b) => a - b);
    return arr[1];
}

let rows = tempPuzzleInput.split('\n')
let total = 0;
rows.forEach(element => {
    let dimensions = element.split('x');
    dimensions[0] = Number(dimensions[0]);
    dimensions[1] = Number(dimensions[1]);
    dimensions[2] = Number(dimensions[2]);
    let bow = dimensions[0] * dimensions[1] * dimensions[2];
    let length = 0;
    let smallest = Math.min(dimensions[0], dimensions[1], dimensions[2]);
    let second = secondSmallestElement(dimensions)
    length = smallest + smallest + second + second;
    total += length + bow;
});
alert(total)