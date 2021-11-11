from django import forms

class Formulario(forms.Form):
    resposta = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={"placeholder":"Resposta"}))