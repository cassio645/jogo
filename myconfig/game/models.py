from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=20, help_text="Nome do tema")
    slug = models.SlugField(max_length=22, unique=True, help_text="NÃO MEXE AQUI")
    img = models.ImageField()

    def __str__(self):
        return self.nome


class Palavra(models.Model):
    imagem = models.ImageField()
    resposta = models.CharField(max_length=40, help_text="Insira a resposta")
    wiki = models.CharField(max_length=200, null=True, blank=True, help_text="Link dessa página do Wikipédia")
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, help_text="Qual tema essa palavra faz parte?")

    def __str__(self):
        return self.resposta