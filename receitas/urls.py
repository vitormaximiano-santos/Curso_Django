from django.urls import path
from . import views


app_name = 'receita'

urlpatterns = [
    path('', views.Home, name='home'),
    path('receitas/<int:id>/', views.Receita, name='receita')
]