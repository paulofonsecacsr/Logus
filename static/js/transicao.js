// Faz o conteúdo sumir antes de ir para a próxima página
document.querySelectorAll('nav a, .logo, .btn-cta').forEach(function (link) {
    link.addEventListener('click', function (e) {
        if (link.pathname === window.location.pathname) return;
        e.preventDefault();
        document.body.classList.add('saindo');
        setTimeout(function () { window.location.href = link.href; }, 300);
    });
});

// Ao voltar pelo botão "voltar" do navegador, limpa o estado de saída
window.addEventListener('pageshow', function () {
    document.body.classList.remove('saindo');
});