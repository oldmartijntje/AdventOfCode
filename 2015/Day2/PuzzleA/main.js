var tempPuzzleInput = puzzleInput;
console.log(tempPuzzleInput);

let rows = tempPuzzleInput.split('\n')
let total = 0;
rows.forEach(element => {
    let dimensions = element.split('x');
    dimensions[0] = Number(dimensions[0]);
    dimensions[1] = Number(dimensions[1]);
    dimensions[2] = Number(dimensions[2]);
    let surfaces = [];
    surfaces.push(dimensions[0] * dimensions[1] * 2);
    surfaces.push(dimensions[2] * dimensions[1] * 2);
    surfaces.push(dimensions[0] * dimensions[2] * 2);
    let slack = Math.min(surfaces[0], surfaces[1], surfaces[2]) / 2;
    // alert(`${slack}, ${dimensions}`)
    total += slack + surfaces[0] + surfaces[1] + surfaces[2]
});
alert(total)