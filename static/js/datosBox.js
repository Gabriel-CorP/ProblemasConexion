const $departamento = $('#listaD');
const $municipio = $('#listaM');
    
$departamento.change(function() {
    $municipio.val('');
    
    $municipio.prop('disabled', !Boolean($departamento.val()));
    $municipio.find('option[data-departamento]').hide();
    $municipio.find('option[data-departamento="' + $departamento.val() + '"]').show();
});