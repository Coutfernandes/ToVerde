# denuncias/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Importação recomendada

urlpatterns = [
    path('', views.homepage, name='homepage'), # Homepage como página principal
    path('base/', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
    path('fazerdenuncias/', views.fazerdenuncias, name='fazerdenuncias'),
    
    # URLs de Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Recuperação de Senha
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuario/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuario/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="usuario/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuario/password_reset_done.html"), name="password_reset_complete"),
]
