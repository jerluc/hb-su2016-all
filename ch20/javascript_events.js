var mybutton = document.getElementById('mybutton');

function alertClick() {
    alert('Stop clicking me!');
}

mybutton.addEventListener('click', alertClick);

function changeColorsOn() {
    this.style.color = 'red';
}

function changeColorsOff() {
    this.style.color = 'black';
}

mybutton.addEventListener('mouseover', changeColorsOn);
mybutton.addEventListener('mouseout', changeColorsOff);
