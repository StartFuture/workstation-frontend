var cards = document.getElementsByClassName('card-blog');
var datas = document.getElementsByClassName('p-data-card');

var dateNow = new Date();

function getMonth() {
    for (let i = 0; i < cards.length; i++) {
        var data = datas[i].outerText.split('/')

        if (!(parseInt(data[1]) == dateNow.getMonth() + 1 && parseInt(data[2]) == dateNow.getFullYear())) {
            cards[i].classList.add("invisible")
            cards[i].classList.remove("visible")

        } else {
            cards[i].classList.add("visible")
            cards[i].classList.remove("invisible")
        }
    }
}

function getToday() {
    for (let i = 0; i < cards.length; i++) {
        var data = datas[i].outerText.split('/')

        if (!(parseInt(data[0]) == dateNow.getDate() && parseInt(data[1]) == dateNow.getMonth() + 1 && parseInt(data[2]) == dateNow.getFullYear())) {
            cards[i].classList.add("invisible")
            cards[i].classList.remove("visible")
        } else {
            cards[i].classList.add("visible")
            cards[i].classList.remove("invisible")
        }
    }
}

function getAll() {
    for (let i = 0; i < cards.length; i++) {
        cards[i].classList.add("visible")
        cards[i].classList.remove("invisible")
    }
}