var textoVidas = document.querySelector("#num-vidas")
var numeroVidas = Number(textoVidas.textContent)

textoVidas.innerHTML = '<i class="bi bi-heart-fill"></i> '.repeat(numeroVidas);


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

