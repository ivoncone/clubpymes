from django.contrib import admin
from .models import Seccion, Publicacion, Profile, Comentario

# Register your models here.
admin.site.register(Seccion)
admin.site.register(Publicacion)
admin.site.register(Profile)
admin.site.register(Comentario)