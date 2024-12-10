console.log('teste de script');

function control_under_age() {
    document.querySelector('#txtParents').disabled = !document.querySelector('#txtUnderAge').checked;
}

function numbers_only(pElemento) {
    pElemento.addEventListener('keydown', function (e) {
        if (!/[0-9]/.test(e.key) && e.key !== 'Backspace' && e.key !== 'Tab') {
            e.preventDefault();
        }
    });

    pElemento.addEventListener('input', function () {
        this.value = this.value.replace(/\D/g, '');
    });
}