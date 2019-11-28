from django.contrib import admin

# Register your models here.
from .models import Residente, Familiar, Informe, ParteInforme

admin.site.register(Residente)
admin.site.register(Familiar)
admin.site.register(Informe)
admin.site.register(ParteInforme)
