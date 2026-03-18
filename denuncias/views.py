# denuncias/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Denuncia
from .forms import DenunciaForm, LoginForm
from django.contrib.auth.models import User # Adicione este import no topo do arquivo

# =================================================================
# 1. HOMEPAGE (Feed de Denúncias)
# =================================================================
def homepage(request):
    # Procura as 6 denúncias mais recentes para mostrar no feed
    denuncias_recentes = Denuncia.objects.all().order_by('-data_registro')[:6]
    
    context = {
        'denuncias': denuncias_recentes
    }
    return render(request, 'home/homepage.html', context)

# =================================================================
# 2. FAZER DENÚNCIA (Criação)
# =================================================================
def fazerdenuncias(request):
    if request.method == 'POST':
        # Carrega o formulário com os dados do POST e os arquivos (fotos/vídeos)
        form = DenunciaForm(request.POST, request.FILES)
        
        if form.is_valid():
            denuncia = form.save(commit=False) # Cria o objeto mas não salva no banco ainda
            
            # Verifica se o usuário quer anonimato ou se não está logado
            anonima = form.cleaned_data.get('anonima')
            
            if request.user.is_authenticated and not anonima:
                denuncia.usuario = request.user # Associa a denúncia ao utilizador logado
            
            denuncia.save() # Salva definitivamente no banco de dados
            
            messages.success(request, 'A sua denúncia foi enviada com sucesso! Obrigado por ajudar o meio ambiente.')
            return redirect('homepage')
        else:
            messages.error(request, 'Houve um erro no formulário. Por favor, verifique os dados.')
    else:
        form = DenunciaForm()

    return render(request, 'usuario/fazerdenuncias.html', {'form': form})

# =================================================================
# 3. LOGIN E LOGOUT
# =================================================================

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_digitado = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # 1. Tentamos descobrir quem é o dono desse e-mail
            try:
                user_obj = User.objects.get(email=email_digitado)
                # Se achamos, usamos o username real dele para autenticar
                username_para_auth = user_obj.username
            except User.DoesNotExist:
                # Se não achar o e-mail, usamos o que foi digitado (pode ser um username)
                username_para_auth = email_digitado

            # 2. Agora o authenticate vai funcionar porque passamos o username correto
            user = authenticate(request, username=username_para_auth, password=password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo de volta, {user.username}!')
                return redirect('homepage')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha o formulário corretamente.')
    else:
        form = LoginForm()
        
    return render(request, 'usuario/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "Sessão encerrada com sucesso.")
    return redirect('homepage')

# Views básicas para renderização (caso precise)
def base(request):
    return render(request, 'base/base.html')

def navbar(request):
    return render(request, 'base/navbar.html')

# =================================================================
# 4. REGISTRO DE USUÁRIO    
from .forms import DenunciaForm, LoginForm, UserRegisterForm # Adicione UserRegisterForm aqui

def register_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco
            auth_login(request, user) # Loga automaticamente
            messages.success(request, f'Conta criada com sucesso! Bem-vindo(a), {user.username}!')
            return redirect('homepage')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados e tente novamente.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'usuario/register.html', {'form': form})