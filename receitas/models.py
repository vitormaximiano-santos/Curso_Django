from django.db import models

class Receitas( models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug= models.SlugField(unique=True)
    tempo_preparo = models.IntegerField(help_text="Tempo em minutos")
    tempo_preparo_unidade = models.CharField(max_length=65)
    porcoes = models.IntegerField()
    porcoes_unidade = models.CharField(max_length=65)
    modo_preparo = models.TextField()
    modo_preparo_is_html = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receitas/covers/%Y/%m/%d/', blank=True, null=True)
    ingredientes = models.TextField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
   

    def __str__(self):
        return self.titulo
