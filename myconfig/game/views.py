from random import randint
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Tema, Palavra
from .forms import Formulario
from .game import jogar


def vidas_inicial():
    # função que seta o número de vidas inicial +1, pois sempre sera removida no GET
    return 4

def pontos_inicial():
    # configurando a pontuação inicial
    return 0


def index(request):
    # Zerando a pontuação e as vidas, sempre que voltar para a página inicial
    global pontuacao
    global vidasUser
    pontuacao = pontos_inicial()
    vidasUser = vidas_inicial()
    temas = Tema.objects.all().order_by('nome')
    return render(request, 'game/index.html', {"temas":temas})

# zerando a pontuação e as vidas fora do index
pontuacao = pontos_inicial()
vidasUser = vidas_inicial()


def jogo(request, slug):
    # Pegando a pontuação e as vidas iniciais
    global pontuacao
    global vidasUser
    form = Formulario()

    if request.method == "GET":
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

        '''
        vidasUser -=1 no GET foi feito para que o usuário não fique atualizando a página
         pois assim palavra/imagem mudariam sem que ele perdesse vidas. 
         Contudo isso faz o usuário SEMPRE perder uma vida independente de tudo.
        '''
        vidasUser -= 1

        # caso ele atualize a página 3x perderá todas as vidas e sera redirecionado ao gameover
        if vidasUser < 1:
            return redirect("game:gameover")
        return render(request, "game/jogo.html", {"imagem":imagem, "resp":resp, "form":form, "pontos":pontuacao, "vidas":vidasUser, "tema":nome})
    else:

        # verificando as vidas method POST
        if vidasUser < 1:
            return redirect("game:gameover")
        
        # no form está o input onde o usuário irá responder
        form = Formulario(request.POST)
        if form.is_valid():

            # pegando a resposta do usuário
            usuario = request.POST.get('resposta')

            # função jogar faz a validação e verifica se acertou ou não, retornando uma mensagem
            msg = jogar(usuario, request.session['resposta_atual'])
            messages.info(request, msg)

            # caso ele tenha acertado ele recebe 1 ponto E a vida devolta que ele havia perdido no GET
            if "Acertou" in msg:
                vidasUser += 1
                pontuacao += 1
            return redirect('game:jogo', slug=slug)


def gameover(request):
    messages.info(request, "")
    return render(request, "game/gameover.html", {"pontos":pontuacao})


def aprenda(request, slug):
    # pegando todas as palavras daquele tema, e listando por ordem alfabética das respostas
    lista_palavras = Palavra.objects.filter(tema__slug=slug).order_by('resposta')
    return render(request, "game/aprenda.html", {"lista":lista_palavras})

def sobre(request):
    return render(request, "game/sobre.html")