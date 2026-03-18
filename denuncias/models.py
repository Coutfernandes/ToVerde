# denuncias/models.py
from django.db import models
from django.contrib.auth.models import User # Importamos o modelo de Usuário do Django

class Denuncia(models.Model):
    # Tipos de Ocorrência
    TIPO_OCORRENCIA_CHOICES = [
        ('desmatamento', 'Desmatamento'),
        ('queimada', 'Queimada'), # <--- CORRIGIDO
        ('poluicao', 'Poluição'),
        ('caca', 'Caça Ilegal'),
        ('outro', 'Outro'),
    ]

    # Relacionamento com o usuário que fez a denúncia (pode ser nulo/em branco se for anônima)
    usuario = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Denunciante"
    )
    
    # Campos do Formulário
    tipo_ocorrencia = models.CharField(max_length=50, choices=TIPO_OCORRENCIA_CHOICES)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=255) 
    data_ocorrencia = models.DateField()
    
    # Campo para o anexo
    foto = models.FileField(upload_to='denuncias/anexos/', blank=True, null=True) 
    
    # Campo para anonimato
    anonima = models.BooleanField(default=False)
    
    # Campos de controle
    STATUS_CHOICES = [
        ('Em análise', 'Em análise'),
        ('Resolvida', 'Resolvida'),
        ('Não verificada', 'Não verificada'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Em análise')
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipo_ocorrencia_display()} em {self.localizacao}'

    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"
        ordering = ['-data_registro'] # Ordem padrão, da mais nova para a mais antiga