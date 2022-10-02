$(document).ready(function(){
    $('.button_choice').click(function getNomeProduto(e){
        $('.formCep').attr('style', 'display:block');
        window.scrollTo(0,2000);
        var nome_produto = $(this).val();
        $('.button_send').click(function(e){
            if($("input[name=cep]").val() == ''){
                alert('Preencha o campo de CEP');
            } else if ($("input[name=numero]").val() == ''){
                alert('Preencha o campo de Número');
            } else {
                var logradouro = $("input[name=rua]").val();
                var bairro = $("input[name=bairro]").val();
                var numero = $("input[name=numero]").val();
                var complemento = $("input[name=complemento]").val();
                if (complemento != "") {
                    $('.endereco_enviado').text(logradouro + ", " + numero + ", " + complemento + ", "  +  bairro);
                } else {
                    $('.endereco_enviado').text(logradouro + ", " + numero + ", " +  bairro);
                }
                $('.enviado').text("Ótimo! Estamos enviando " + nome_produto + " para o endereço");

                $('.truck_gif').attr('style', 'display:block; margin: 10px 35%;');
                window.scrollTo(0,4000);
            }
        });
    });
})