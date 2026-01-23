from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Receita(models.Model):  # Use singular and PascalCase for class names
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    tempo_preparo = models.IntegerField(help_text="Tempo em minutos")
    tempo_preparo_unidade = models.CharField(max_length=65)
    porcoes = models.IntegerField()
    porcoes_unidade = models.CharField(max_length=65)
    modo_preparo = models.TextField()
    modo_preparo_is_html = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='receitas/covers/%Y/%m/%d/', 
        blank=True, null=True
    )
    categoria = models.ForeignKey(  # lowercase field name
        Categoria, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='receitas'
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, 
        related_name='receitas'
    )
    ingredientes = models.TextField()
    rendimento = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
