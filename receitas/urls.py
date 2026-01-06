from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('receitas/<int:id>/', views.Receitas),
]
 