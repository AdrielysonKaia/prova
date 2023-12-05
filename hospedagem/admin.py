from django.contrib import admin
from .models import Hospedagem, Consumo, Cliente, Quarto

admin.site.register(Hospedagem)
admin.site.register(Consumo)
admin.site.register(Cliente)
admin.site.register(Quarto)
