var registerButton = document.getElementById('finalizar-cadastro')

registerButton.addEventListener(function() {
    var fields = document.getElementsByClassName('inputs-login');

    for (let i = 0; i < fields.length; i++) {
        if (fields[i].textContent == null || fields[i].textContent == '') {
            return;
        }
    }

    var span = document.getElementsByClassName("close")[0];

    btn.onclick = function() {
    modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }

    var closeBtn = document.getElementsByClassName("btn-continue-cadastro")[0];

    closeBtn.onclick = function() {
    modal.style.display = "none";
    }
});