var modalAlterarCartaoConfirmacao = document.getElementById("my-modal-alterar-cartao-confirmacao");
var btnAlterarCartaoConfirmacao = document.getElementById("my-btn-alterar-cartao-confirmacao");
var spanAlterarCartaoConfirmacao = document.getElementById("close-alterar-cartao-confirmacao");
btnAlterarCartaoConfirmacao.onclick = function() {
    modalAlterarCartaoConfirmacao.style.display = "block";
}
spanAlterarCartaoConfirmacao.onclick = function() {
    modalAlterarCartaoConfirmacao.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modalAlterarCartaoConfirmacao) {
        modalAlterarCartaoConfirmacao.style.display = "none";
    }
}