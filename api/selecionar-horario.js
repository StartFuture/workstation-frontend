const y = document.getElementsByClassName("input-horario");

for (var i = 0; i < y.length; i++) {
    y[i].addEventListener('click', function(i) {
        if (y[i].style.backgroundColor == 'white') {
            y[i].style.backgroundColor = 'salmon'
        } else {
            y[i].style.backgroundColor = 'white'
        }
    }.bind(null, i));
}