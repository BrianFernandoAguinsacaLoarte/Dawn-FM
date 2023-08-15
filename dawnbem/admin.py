from django.contrib import admin
from dawnbem.models import Registro, Jugador, Inscripcion, Equipo, Grupo, Partido, Marcador, Temporada, Reglamento, \
    Regla, Sorteo


class RegistroAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    list_display = ('nombre', 'apellido')
    list_filter = ('nombre',)
    list_per_page = 10
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['jugador', 'EstadoInscripcion']  # Mostrar estado en la lista
    list_filter = ['EstadoInscripcion']  # Agregar filtro por estado

class ReglaAdmin(admin.ModelAdmin):
    ordering = ['id']

class PartidoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_filter = ['estado']


admin.site.register(Registro, RegistroAdmin)
admin.site.register(Jugador)
admin.site.register(Inscripcion, InscripcionAdmin)

admin.site.register(Equipo)
admin.site.register(Grupo)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Marcador)
admin.site.register(Temporada)
admin.site.register(Reglamento)
admin.site.register(Regla, ReglaAdmin)
admin.site.register(Sorteo)

