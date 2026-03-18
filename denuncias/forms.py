# denuncias/forms.py
from django import forms
from .models import Denuncia
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#1. Formulário para o Model Denuncia
class DenunciaForm(forms.ModelForm):
# O widget DateInput garante que o campo 'data_ocorrencia' seja 
# renderizado como um input type="date", como você tinha no seu HTML
    data_ocorrencia = forms.DateField(
        label='Data da Ocorrência',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    class Meta:
        model = Denuncia
# Define quais campos do Model estarão no formulário
        fields = ['tipo_ocorrencia', 'descricao', 'data_ocorrencia', 'localizacao', 'foto', 'anonima']
# Opcional: Customiza os labels exibidos no formulário
        labels = {
            'tipo_ocorrencia': 'Tipo de Ocorrência',
            'descricao': 'Descrição da ocorrência',
            'localizacao': 'Localização',
            'foto': 'Anexo (foto ou vídeo)',
            'anonima': 'Enviar de forma Anônima',
        }
# Opcional: Adiciona classes CSS ou placeholders aos widgets

        widgets ={
            'tipo_ocorrencia': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Descreva o que está ocorrendo: local, horario, pessoas envolvidas...'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Digite o endereço ou local'}),
        }
# 2. Formulário para Login
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail do usuário',
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'nome@email.com', 'class': 'form-input'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class': 'form-input'})
    )

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# 3. Formulário para Registro de Usuário

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail do usuário',
        widget=forms.EmailInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'email'] # Define os campos que aparecerão
        
    # Opcional: Adicionar classes CSS para ficar bonito
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input'})