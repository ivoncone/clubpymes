from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

def upload_load(instance, filename):
	return f'photos_members{instance.first_name}/{filename}'

# Create your models here.
class Seccion(models.Model):
	name = models.CharField(max_length=200, default="noticias")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	profileImage = models.ImageField(upload_to=upload_load, default='default.jpg', null=True, )
	bio = models.TextField(max_length=200, null=True)
	ciudad = models.CharField(max_length=200, null=True)
	redes = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')

class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	seccion = models.CharField(max_length=200)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	publicacionImage = models.ImageField(null=True)
	descripcion = models.CharField(max_length=200)
	contenido = RichTextField(blank=True, null=True)
	fecha = models.DateField(auto_now_add=True)
	snippet = models.CharField(max_length=255, default='Da click en el enlace para leer la historia completa')
	likes = models.ManyToManyField(User, related_name="pub")

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.titulo 

	def get_absolute_url(self):
		return reverse('home')

class Comentario(models.Model):
	publicacion = models.ForeignKey(Publicacion, related_name="comentarios", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	fecha_coment = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.publicacion.titulo, self.name)


