from django import forms
from .models import Publicacion, Seccion, Comentario

#choices = [('tecnologos', 'lifestyle', 'arte y cultura', 'viajes')]
choices = ['noticias', 'lifestyle', 'tecnologos', 'arte', 'cultura', 'tutoriales', 'entrevistas', 'experiencias']


class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = ('titulo', 'seccion', 'autor', 'publicacionImage', 'descripcion', 'contenido', 'snippet')

		widget = {
			'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe el titulo de tu historia'}),
			'seccion': forms.Select(choices=choices, attrs={'class': 'form-control'}),
			'autor': 'username',
			'publicacionImage': forms.FileInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'contenido': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = ('titulo', 'descripcion', 'contenido')

		widget = {
			'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe el titulo de tu historia'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'contenido': forms.Textarea(attrs={'class': 'form-control'}),
		}

class ComentarioForm(forms.ModelForm):
	class Meta: 
		model = Comentario
		fields = ('name', 'body')

		widget = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}
