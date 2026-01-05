from django.urls import path
from receitas.views import Home


urlpatterns = [
    path('', Home)
]
