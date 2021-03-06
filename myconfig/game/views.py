from random import randint
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Tema, Palavra
from .forms import Formulario
from .game import jogar



def index(request):
    # Criando sessions para o placar e resposta do usuário
    request.session["vidas"] = 3
    request.session["pontos"] = 0
    request.session["user"] = ""

    # listando todos os temas 
    temas = Tema.objects.all().order_by('nome')
    return render(request, 'game/index.html', {"temas":temas})


def jogo(request, slug):
    form = Formulario()

    if request.method == "GET":

        # SE a session de respostas estiver vazia, reset as vidas e os pontos
        # sempre vem vazia do index, e não permite que o usuario fique atualizando a página, para trocar a imagem
        # sem perder vidas
        if request.session["user"] == "":
            request.session["vidas"] = 3
            request.session["pontos"] = 0
        
        # resetando a session
        request.session["user"] = ""

        # pegando as palavras daquele tema específico
        lista_palavras = Palavra.objects.filter(tema__slug=slug)

        # pegando o nome do tema a partir do slug (para aparecer acima do input onde o usuário responde)
        nome = Tema.objects.get(slug=slug)

        # pegando a quantidade de palavras daquele tema
        total = lista_palavras.count()

        # sorteando uma palavra aleatoria na lista de palavras(usando o total)
        palavra = lista_palavras[randint(0, total-1)]

        # salvando a resposta ATUAL em session, pois ao atualizar ela mudaria antes de verificar se o usuario acertou
        request.session ['resposta_atual'] = palavra.resposta
        resp = request.session['resposta_atual']

        # pegando a imagem referente a palavra sorteada
        imagem = palavra.imagem

        # Se acabar as vidas vai para página gameover
        if request.session["vidas"] < 1:
            return redirect('game:gameover')

        context = {
                    "imagem":imagem,
                    "resp":resp, "form":form,
                    "pontos":request.session["pontos"],
                    "vidas":request.session["vidas"],
                    "tema":nome
            }
        return render(request, "game/jogo.html", context)
    else:

        # no form está o input onde o usuário irá responder
        form = Formulario(request.POST)
        if form.is_valid():

            # pegando a resposta do usuário
            usuario = request.POST.get('resposta')

            # atribuindo valor a session de resposta
            request.session["user"] = usuario

            # função jogar faz a validação e verifica se acertou ou não, retornando uma mensagem
            msg = jogar(usuario, request.session['resposta_atual'])
            messages.info(request, msg)

            # caso ele tenha acertado ele recebe 1 ponto E a vida devolta que ele havia perdido no GET
            if "Acertou" in msg:
                request.session["pontos"] += 1
            else:
                request.session["vidas"] -= 1
            return redirect('game:jogo', slug=slug)


def gameover(request):
    # Pegando a pontuacao feita, e criando uma mensa
    if request.session["pontos"] != 1:
        msg = f'Você fez {request.session["pontos"]} pontos'
    else:
        msg = f'Você fez {request.session["pontos"]} ponto'
    messages.info(request, msg)
    
    # zerando a pontuacao, apos exibir a msg
    request.session["pontos"] = 0
    return render(request, "game/gameover.html")


def aprenda(request, slug):
    # pegando todas as palavras daquele tema, e listando por ordem alfabética das respostas
    lista_palavras = Palavra.objects.filter(tema__slug=slug).order_by('resposta')
    return render(request, "game/aprenda.html", {"lista":lista_palavras})

def sobre(request):
    return render(request, "game/sobre.html")