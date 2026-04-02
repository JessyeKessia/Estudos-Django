from django.contrib import admin

# Register your models here.
from .models import Autor, Editora, Livro, Publica

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Publica)