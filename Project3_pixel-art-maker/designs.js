const submitPress = document.getElementById("Button");
const inputHeight = document.getElementById("inputHeight")
const inpuWidth = document.getElementById("inputWidth")

submitPress.addEventListener('click', function(event) {
    event.preventDefault();
    let height = inputHeight.value;
    let width = inputWidth.value;
    makeGrid(height, width);
})

/** 
 * @ description Generate grid and attach color function
 * @ param {number} h - the number of cells vertically
 * @ param {number} w - the number of cells horizontally 
 */ 
function makeGrid(h,w) {
    const board = document.querySelector('#pixelCanvas');
    var grid = "";
    for (let i=0; i<h; i=i+1) {
        grid += '<tr class="row'+i+'">';
        for (let j=0; j<w; j=j+1) {
            grid += '<td class="cell" id="row'+i+'_column'+j+'"></td>';
        }
    }
    grid += '</tr>';
    board.innerHTML = grid;
    colorEventToCells();
}
/**
 * @ description Attach event to cells to reflect the selected color
 */
function colorEventToCells() {
    var cells = document.getElementsByClassName('cell');
    for (let k=0; k<cells.length; k++) {
        cells[k].addEventListener("click", function(event) {
            let selectedCell = event.target;
            selectedCell.style.backgroundColor = colorPicker.value
        });
    }
}

var colorPicker = document.getElementById('colorPicker')