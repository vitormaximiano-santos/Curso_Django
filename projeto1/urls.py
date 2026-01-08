from django.contrib import admin
from django.urls import path, include    

urlpatterns = [
    path('admin/', admin.site.urls),       # ativa o painel administrativo padrão
    path('', include('receitas.urls'))     # delega todas as rotas da raiz para o app receitas
]
