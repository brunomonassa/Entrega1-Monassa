from django import forms

class Villa_olimpica_form(forms.Form):

    nombre=forms.CharField(max_length=40)
    ubicacion=forms.CharField(max_length=40)
    numero=forms.IntegerField()
    fundacion=forms.DateField()

class Disciplina_form(forms.Form):

    nombre= forms.CharField(max_length=40)
    se_juega_con_balon=forms.BooleanField()

class Deportista_form(forms.Form):

    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email=forms.EmailField()
