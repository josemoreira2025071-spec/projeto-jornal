from django.contrib import admin
from .models import Artigo, Comentario

# Isto faz com que os modelos apareçam no painel
admin.site.register(Artigo)
admin.site.register(Comentario)