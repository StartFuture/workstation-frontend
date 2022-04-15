// Get the modal
var modal = document.getElementById("myModal");
var modalAlterarEmail = document.getElementById("my-modal-alterar-email");
var modalAlterarSenha = document.getElementById("my-modal-alterar-senha");
var modalAlterarCpf = document.getElementById("my-modal-alterar-cpf");
var modalAlterarTelefone = document.getElementById("my-modal-alterar-telefone");
var modalAlterarCartao = document.getElementById("my-modal-alterar-cartao");


// Get the button that opens the modal
var btn = document.getElementById("myBtn");
var btnAlterarEmail = document.getElementById("my-btn-alterar-email");
var btnAlterarSenha = document.getElementById("my-btn-alterar-senha");
var btnAlterarCpf = document.getElementById("my-btn-alterar-cpf");
var btnAlterarTelefone = document.getElementById("my-btn-alterar-telefone");
var btnAlterarCartao = document.getElementById("my-btn-alterar-cartao");


// Get the <span> element that closes the modal
var spanAlterarNome = document.getElementById("close-alterar-nome");
var spanAlterarEmail = document.getElementById("close-alterar-email");
var spanAlterarSenha = document.getElementById("close-alterar-senha");
var spanAlterarCpf = document.getElementById("close-alterar-cpf");
var spanAlterarTelefone = document.getElementById("close-alterar-telefone");
var spanAlterarCartao = document.getElementById("close-alterar-cartao");



// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}
btnAlterarEmail.onclick = function() {
    modalAlterarEmail.style.display = "block";
}
btnAlterarSenha.onclick = function() {
    modalAlterarSenha.style.display = "block";
}
btnAlterarCpf.onclick = function() {
    modalAlterarCpf.style.display = "block";
}
btnAlterarTelefone.onclick = function() {
    modalAlterarTelefone.style.display = "block";
}
btnAlterarCartao.onclick = function() {
    modalAlterarCartao.style.display = "block";
}




// When the user clicks on <span> (x), close the modal
spanAlterarNome.onclick = function() {
    modal.style.display = "none";
}
spanAlterarEmail.onclick = function() {
    modalAlterarEmail.style.display = "none";
}

spanAlterarSenha.onclick = function() {
    modalAlterarSenha.style.display = "none";
}
spanAlterarCpf.onclick = function() {
    modalAlterarCpf.style.display = "none";
}
spanAlterarTelefone.onclick = function() {
    modalAlterarTelefone.style.display = "none";
}
spanAlterarCartao.onclick = function() {
    modalAlterarCartao.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}