$(document).ready(function(){
    $('.button_choice').click(function(e){
        $('.formCep').attr('style', 'display:block');
        window.scrollTo(0,2000);
    });
    $('.button_send').click(function(e){
        if($("input[name=cep]").val() == ''){
            alert('Preencha o campo de CEP');
        }
    });
})