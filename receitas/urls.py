from django.urls import path
from django.http import HttpResponse
from receitas.views import Home, Contatos, Sobre, conteudo


urlpatterns = [
    path('', Home),
    path('contatos/', Contatos),
    path('sobre/', Sobre),
    path('conteudo/', conteudo),
]
