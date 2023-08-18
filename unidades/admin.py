from django.contrib import admin

from unidades.models import Unidade, Maquina, Impressao

# Register your models here.

admin.site.register(Unidade)
admin.site.register(Maquina)
admin.site.register(Impressao)