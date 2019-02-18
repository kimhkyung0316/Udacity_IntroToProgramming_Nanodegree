// Select color input
const color = document.getElementById("colorPicker")
// Select size input
const height = document.getElementById("inputHeight").value
const width = document.getElementById("inputWidth").value
// When size is submitted by the user, call makeGrid()
const submit = document.getElementById("Button")
submit.addEventListener('click', makeGrid )

console.log(height, width)


function makeGrid(event) {
    event.preventDefault();
// Your code goes here!
    const board = document.querySelector('#pixelCanvas');

    for (var i=0; i<height; i=i+1) {
        var container = document.createElement('div');
        container.class = 'container';
        container.id = 'row'+i;
        container.style.display = 'flex';
        container.style.height = '5px';
        board.appendChild(container)
        for (var j=0; j<width; j=j+1) {
            var cell = document.createElement('div')
            cell.class = 'box'
            cell.id = 'row'+i+'_col'+j;
            cell.style.width = '5px';
            cell.style.height = '5px';
            container.appendChild(cell)
        }
    };
    document.getElementsByClassName('box').style = "solid black"
};
