from django import forms

class formArticulo(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField(widget = forms.Textarea)
    publico = forms.BooleanField(required= False)
    imagen = forms.ImageField(required= False)

