"""
URL configuration for DawnFM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from dawnbem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.mi_vista, name='mi_vista'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='Inicio'),
    path('pinpon/', views.pinpon, name='pinpon'),
    path('contacto1/', views.contacto1, name='contacto1'),
    path('contacto2/', views.contacto2, name='contacto2'),
    path('paginaFutbol/', views.pageFutbol, name='pageFutbol'),
    path('formulario/', views.formulario, name='formulario'),

    path('registro/<int:id>/', views.registro_detail, name='registroDetail'),
    path('nuevo_registro/', views.nuevo_Registro, name='registroNuevo'),
    path('editar_registro/<int:id>/', views.editar_Registro, name='editar_registro'),
    path('registro_eliminar/<int:id>/', views.eliminar_Registro, name='eliminar_registro'),

    path('jugador/<int:id>/', views.jugador_detail, name='jugadorDetail'),
    path('nuevo_jugador/', views.nuevo_jugador, name='jugadorNuevo'),
    path('editar_jugador/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('jugador_eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),

    path('inscripcion/<int:id>/', views.inscripcion_detail, name='inscripcionDetail'),
    path('nueva_inscripcion/', views.nueva_inscripcion, name='inscripcionNueva'),
    path('editar_inscripcion/<int:id>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('inscripcion_eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),

    path('equipo/<int:id>/', views.equipo_detail, name='equipoDetail'),
    path('nuevo_equipo/', views.nuevo_equipo, name='equipoNuevo'),
    path('editar_equipo/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipo_eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),

    path('grupo/<int:id>/', views.grupo_detail, name='grupoDetail'),
    path('nuevo_grupo/', views.nuevo_grupo, name='grupoNuevo'),
    path('editar_grupo/<int:id>/', views.editar_grupo, name='editar_grupo'),
    path('grupo_eliminar/<int:id>/', views.eliminar_grupo, name='eliminar_grupo'),

    path('sorteo/<int:id>/', views.sorteo_detail, name='sorteoDetail'),
    path('nuevo_sorteo/', views.nuevo_sorteo, name='sorteoNuevo'),
    path('editar_sorteo/<int:id>/', views.editar_sorteo, name='editar_sorteo'),
    path('sorteo_eliminar/<int:id>/', views.eliminar_sorteo, name='eliminar_sorteo'),

    path('partido/<int:id>/', views.partido_detail, name='partidoDetail'),
    path('nuevo_partido/', views.nuevo_partido, name='partidoNuevo'),
    path('editar_partido/<int:id>/', views.editar_partido, name='editar_partido'),
    path('partido_eliminar/<int:id>/', views.eliminar_partido, name='eliminar_partido'),

    path('marcador/<int:id>/', views.marcador_detail, name='marcadorDetail'),
    path('nuevo_marcador/', views.nuevo_marcador, name='marcadorNuevo'),
    path('editar_marcador/<int:id>/', views.editar_marcador, name='editar_marcador'),
    path('marcador_eliminar/<int:id>/', views.eliminar_marcador, name='eliminar_marcador'),

    path('reglamento/<int:id>/', views.reglamento_detail, name='reglamentoDetail'),
    path('nuevo_reglamento/', views.nuevo_reglamento, name='reglamentoNuevo'),
    path('reglamento_visualizar/', views.reglamento_visualizar, name='visualizar_reglamento'),
    path('editar_reglamento/<int:id>/', views.editar_reglamento, name='editar_reglamento'),
    path('reglamento_eliminar/<int:id>/', views.eliminar_reglamento, name='eliminar_reglamento'),

    path('regla/<int:id>/', views.regla_detail, name='reglaDetail'),
    path('nueva_regla/', views.nueva_regla, name='reglaNueva'),
    path('editar_regla/<int:id>/', views.editar_regla, name='editar_regla'),
    path('regla_visualizar/', views.regla_visualizar, name='visualizar_regla'),
    path('regla_eliminar/<int:id>/', views.eliminar_regla, name='eliminar_regla'),

    path('temporada/<int:id>/', views.temporada_detail, name='temporadaDetail'),
    path('nueva_temporada/', views.nueva_temporada, name='temporadaNueva'),
    path('editar_temporada/<int:id>/', views.editar_temporada, name='editar_temporada'),
    path('temporada_eliminar/<int:id>/', views.eliminar_temporada, name='eliminar_temporada'),

]
