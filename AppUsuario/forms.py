from django import forms
import datetime
class PosteoForm(forms.Form):
    
    titulo = forms.CharField(max_length=90)
    texto = forms.CharField(max_length=90)

class PostearForm(forms.Form):

    titulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=400)  
    nombre = forms.CharField(max_length=40)
    fecha = forms.DateField(initial=datetime.date.today)


