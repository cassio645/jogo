// pegando o timer setando o tempo inicial
const starting = 0.15;
let time = starting * 60;
const cont = document.querySelector("#timer");

// intervalo de tempo ser a cada 1 segundos
setInterval(updateCont, 1000);


function updateCont(){
    var txt = "Tempo: ";
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    // mostrando na tela o tempo
    cont.innerHTML = `${txt.bold()} ${seconds}`;
    time--;

    // SE os segundos chegarem em 0 redirecione à página gameover
    // SE os segundos forem menor que 10 mude o texto para vermelho e negrito
    if(seconds == 0){
        window.location.assign("/gameover")
    } else if(seconds < 5){
        cont.style.color = "red";
        cont.style.fontWeight = "700";
    }
}