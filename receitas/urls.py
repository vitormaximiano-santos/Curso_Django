from django.urls import path
from . import views


app_name = 'receitas'

urlpatterns = [
    path('', views.Home, name='home'),
    path('receitas/<int:id>/', views.Receita, name='receita'),
    path('search/', views.search, name='search'), # rota de busca
]
