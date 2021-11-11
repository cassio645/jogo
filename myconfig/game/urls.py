from django.urls import path
from . import views

app_name = "game"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("jogo/<slug:slug>", views.jogo, name="jogo"),
    path("gameover/",views.gameover, name="gameover"),
    path("<slug:slug>/aprenda/", views.aprenda, name="aprenda"),
    path("sobre/", views.sobre, name="sobre"),
]