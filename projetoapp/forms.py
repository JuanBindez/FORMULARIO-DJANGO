from django import forms
from .models import Cliente


SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino')
)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"