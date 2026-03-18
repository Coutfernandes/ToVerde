# denuncias/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    # CORREÇÃO: Adicionei 'status' aqui para o 'list_editable' funcionar
    list_display = ('ver_foto', 'tipo_ocorrencia', 'localizacao', 'data_ocorrencia', 'status', 'status_colorido', 'anonima')
    
    list_filter = ('status', 'tipo_ocorrencia', 'data_ocorrencia', 'anonima')
    search_fields = ('descricao', 'localizacao')
    
    # Agora o Django aceita, pois 'status' está no list_display acima
    list_editable = ('status',)

    fieldsets = (
        ('Informações da Ocorrência', {
            'fields': ('tipo_ocorrencia', 'descricao', 'data_ocorrencia', 'localizacao', 'foto')
        }),
        ('Controle e Status', {
            'fields': ('usuario', 'anonima', 'status'),
        }),
    )

    # --- FUNÇÕES CUSTOMIZADAS ---

    def status_colorido(self, obj):
        cores = {
            'Em análise': 'orange',
            'Resolvida': 'green',
            'Não verificada': 'red'
        }
        cor = cores.get(obj.status, 'black')
        return format_html('<b style="color: {};">{}</b>', cor, obj.status)
    
    status_colorido.short_description = 'Legenda Visual'

    def ver_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px;" />', obj.foto.url)
        return "Sem foto"
    
    ver_foto.short_description = 'Miniatura'