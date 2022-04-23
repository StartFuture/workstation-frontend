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

var divPagamento = document.getElementById("coontainer-pagamento-confirmar-reserva");
var titleModalEditCard = document.getElementById("title-modal-confirmar-reserva-cartao");
if (true) {
    divPagamento.style.display = "none";
    btnAlterarCartaoConfirmacao.value = "Adicionar novo cartão";
    titleModalEditCard.textContent = "Adicionar novo cartão de crédito"
} else {
    divPagamento.style.display = "block";
    btnAlterarCartaoConfirmacao.value = "Editar cartão";
    titleModalEditCard.textContent = "Alterar cartão de crédito";
}