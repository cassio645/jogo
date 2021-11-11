
// Pegando o número de vidas atual e transformando em número
var vidas = document.querySelector("#vidas");
var numero_vidas = Number(vidas.textContent);

// Fazendo aparecer no html o emoji de coração, usando a função repeat e o NÚMERO de vidas atual.
vidas.innerHTML = "&#128151;".repeat(numero_vidas);


// pegando a mensagem de feedback e alterando as cores para verde se acertou e vermelho se não acertou
var txt = document.querySelector("#message");
var msg = txt.textContent;

    if(msg.includes("Acertou")){
        txt.style.color = "rgb(0, 107, 0)";
    } else{
        txt.style.color = "rgb(138, 15, 15)";
    }

// Fazendo o input ter o foco após a primeira interação com o jogo
document.querySelector("#id_resposta").focus();

