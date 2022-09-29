$(document).ready(function(){
    $('.button_choice').click(function(e){
        if($("input[name=cep]").val() == ''){
            alert("Preencha o campo de CEP")
        } else {
            $("enviado").css('display', 'block');
            window.scrollTo(0,2000);
        }
    });
})