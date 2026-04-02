from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()

    # Esta função faz com que o artigo apareça com o seu título no painel de administração, em vez de "Artigo object (1)"
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    # A ForeignKey cria a relação: 1 Artigo tem Vários Comentários.
    # on_delete=models.CASCADE garante que, se apagares o artigo, os comentários vão atrás.
    # related_name='comentarios' vai dar-nos muito jeito mais à frente nas views!
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()

    def __str__(self):
        return f"Comentário em: {self.artigo.titulo}"