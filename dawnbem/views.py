from datetime import date, time
from math import ceil
from random import sample

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from dawnbem.forms import RegistroForm, JugadorForm, InscripcionForm, EquipoForm, PartidoForm, MarcadorForm, TemporadaForm, ReglamentoForm, ReglaForm, SorteoForm, GrupoForm
from dawnbem.models import Registro, Jugador, Inscripcion, Equipo, Partido, Marcador, Temporada, Reglamento, Regla, \
    Sorteo, Grupo


# Create your views here.
def mi_vista(request):
    contexto = {
        'titulo': 'Ejemplo de página HTML en Django',
        'contenido': '¡Hola! Esta es una página HTML generada con Django.',
        'contenido2': 'Enlazado exitosamente Html y DJango'
    }
    return render(request, 'formulario.html', contexto)

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def registro_detail(request,id):
    registro = Registro.objects.get(id=id)
    context = {'registro': registro}
    return render(request, 'registroDetail.html', context)

def nuevo_Registro(request):
    registro = Registro.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroNuevo')

    form = RegistroForm()
    registro_list = Registro.objects.all()
    context = {'form': form,
               'registro_list': registro_list,
               'registro': registro
               }
    return render(request, 'registroNuevo.html', context)

def editar_Registro(request, id):
    registro = Registro.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('registroNuevo')

    form = RegistroForm(instance=registro)
    registro_list = Registro.objects.all()
    context = {'form': form,
               'registro_list': registro_list,
               'registro': registro
               }
    return render(request, 'registroEditar.html', context)
def eliminar_Registro(request, id):
    registro = Registro.objects.get(id=id)
    registro.delete()
    return redirect('registroNuevo')


def jugador_detail(request,id):
    jugador = Jugador.objects.get(id=id)
    context = {'jugador': jugador}
    return render(request, 'jugadorDetail.html', context)

def nuevo_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadorNuevo')

    form = JugadorForm()
    jugador_list = Jugador.objects.all()
    context = {'form': form,
               'jugador_list': jugador_list
               }
    return render(request, 'jugadorNuevo.html', context)
def editar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugadorNuevo')

    form = JugadorForm(instance=jugador)
    jugador_list = Jugador.objects.all()
    context = {'form': form,
               'jugador_list': jugador_list,
               'jugador': jugador
               }
    return render(request, 'jugadorEditar.html', context)

def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    return redirect('jugadorNuevo')

def inscripcion_detail(request,id):
    inscripcion = Inscripcion.objects.get(id=id)
    context = {'inscripcion': inscripcion,
            }
    return render(request, 'inscripcionDetail.html', context)

def nueva_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcionNueva')

    form = InscripcionForm()
    inscripcion_list = Inscripcion.objects.all()
    context = {'form': form,
               'inscripcion_list': inscripcion_list
               }
    return render(request, 'inscripcionNueva.html', context)
def editar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('inscripcionNueva')

    form = InscripcionForm(instance=inscripcion)
    inscripcion_list = Inscripcion.objects.all()
    context = {'form': form,
               'inscripcion_list': inscripcion_list,
               'inscripcion': inscripcion,
               }
    return render(request, 'inscripcionEditar.html', context)

def eliminar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()
    return redirect('inscripcionNueva')

def equipo_detail(request,id):
    equipo = Equipo.objects.get(id=id)
    context = {'equipo': equipo}
    return render(request, 'equipoDetail.html', context)

def nuevo_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipoNuevo')

    form = EquipoForm()
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'equipo_list': equipo_list
               }
    return render(request, 'equipoNuevo.html', context)

def editar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipoNuevo')

    form = EquipoForm(instance=equipo)
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'equipo_list': equipo_list,
               'equipo': equipo
               }
    return render(request, 'equipoEditar.html', context)

def eliminar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('equipoNuevo')

def sorteo_detail(request,id):
    sorteo = Sorteo.objects.get(id=id)
    sorteo_list = Sorteo.objects.all()
    context = {'sorteo_list': sorteo_list}
    return render(request, 'sorteoDetail.html', context)
def nuevo_sorteo(request):
    global grupo
    grupos = []
    partidos = []
    if request.method == 'POST':
        form = SorteoForm(request.POST)
        if form.is_valid():

            sorteo = form.save()

            equipos_participantes = list(sorteo.Equipo_list.all())
            cantidad_equipos = len(equipos_participantes)

            if cantidad_equipos >= 2:

                equipos_aleatorios = sample(equipos_participantes, cantidad_equipos)
                mitad_equipos = cantidad_equipos // 2

                equipos_locales = equipos_aleatorios[:mitad_equipos]
                equipos_visitantes = equipos_aleatorios[mitad_equipos:]

                sorteo.equipos_locales.set(equipos_locales)
                sorteo.equipos_visitantes.set(equipos_visitantes)
                sorteo.save()

                cantidad_grupos = 2
                equipos_por_grupo = ceil(cantidad_equipos / cantidad_grupos)

                grupos = []
                for i in range(cantidad_grupos):

                    inicio = i * equipos_por_grupo
                    fin = (i + 1) * equipos_por_grupo
                    grupo = Grupo.objects.create(nombre=f'Grupo {i + 1}',capacidad_maxima_equipos=equipos_por_grupo)
                    for equipo in equipos_aleatorios[inicio:fin]:

                        grupo.equipos.add(equipo)
                    grupos.append(grupo)

                numero_encuentro = 1  # Inicializar el contador
                for grupo in grupos:

                    for i in range(len(grupo.equipos.all())):

                        for j in range(i + 1, len(grupo.equipos.all())):

                            partido = Partido.objects.create(
                                numero_encuentro=numero_encuentro,
                                fecha=date.today(),
                                hora=time(12, 0),
                                equipo_local=grupo.equipos.all()[i],
                                equipo_visitante=grupo.equipos.all()[j],

                            )
                            numero_encuentro += 1  # Incrementar el contador
                            partidos.append(partido)  # Agregar el partido a la lista de partidos

        return redirect('sorteoNuevo')
    form = SorteoForm()
    sorteo_list = Sorteo.objects.all()
    context = {'form': form, 'sorteo_list': sorteo_list, 'grupos': grupos,
               'partidos': partidos}
    return render(request, 'sorteoNuevo.html', context)

def editar_sorteo(request, id):
    sorteo = Sorteo.objects.get(id=id)
    if request.method == 'POST':
        form = SorteoForm(request.POST, instance=sorteo)
        if form.is_valid():
            form.save()
            return redirect('sorteoNuevo')

    form = SorteoForm(instance=sorteo)
    sorteo_list = Sorteo.objects.all()
    context = {'form': form,
               'sorteo_list': sorteo_list,
               'sorteo': sorteo
               }
    return render(request, 'sorteoEditar.html', context)

def eliminar_sorteo(request, id):
    sorteo = Sorteo.objects.get(id=id)
    sorteo.delete()
    return redirect('sorteoNuevo')

def grupo_detail(request,id):
    grupo = Grupo.objects.get(id=id)
    context = {'grupo': grupo}
    return render(request, 'grupoDetail.html', context)

def nuevo_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupoNuevo')

    form = GrupoForm()
    grupo_list = Grupo.objects.all()
    context = {'form': form,
               'grupo_list': grupo_list
               }
    return render(request, 'grupoNuevo.html', context)

def editar_grupo(request, id):
    grupo = Grupo.objects.get(id=id)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('grupoNuevo')

    form = GrupoForm(instance=grupo)
    grupo_list = Grupo.objects.all()
    context = {'form': form,
               'grupo_list': grupo_list,
               'grupo': grupo
               }
    return render(request, 'grupoEditar.html', context)

def eliminar_grupo(request, id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    return redirect('grupoNuevo')

def partido_detail(request,id):
    partido = Partido.objects.get(id=id)
    context = {'partido': partido,
               }
    return render(request, 'partidoDetail.html', context)
def nuevo_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidoNuevo')

    form = PartidoForm()
    partido_list = Partido.objects.all()
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'partido_list': partido_list,
               'equipo_list': equipo_list
               }
    return render(request, 'partidoNuevo.html', context)

def editar_partido(request, id):
    partido = Partido.objects.get(id=id)
    if request.method == 'POST':
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('partidoNuevo')

    form = PartidoForm(instance=partido)
    partido_list = Partido.objects.all()
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'partido_list': partido_list,
               'equipo_list': equipo_list,
               'partido': partido
               }
    return render(request, 'partidoEditar.html', context)

def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    partido.delete()
    return redirect('partidoNuevo')

def marcador_detail(request,id):
    marcador = Marcador.objects.get(id=id)
    context = {'marcador': marcador,
               }
    return render(request, 'marcadorDetail.html', context)

def nuevo_marcador(request):
    if request.method == 'POST':
        form = MarcadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcadorNuevo')

    form = MarcadorForm()
    marcador_list = Marcador.objects.all()
    context = {'form': form,
               'marcador_list': marcador_list
               }
    return render(request, 'marcadorNuevo.html', context)

def editar_marcador(request, id):
    marcador = Marcador.objects.get(id=id)
    if request.method == 'POST':
        form = MarcadorForm(request.POST, instance=marcador)
        if form.is_valid():
            form.save()
            return redirect('marcadorNuevo')

    form = MarcadorForm(instance=marcador)
    marcador_list = Marcador.objects.all()
    context = {'form': form,
               'marcador_list': marcador_list,
               'marcador': marcador
               }
    return render(request, 'marcadorEditar.html', context)

def eliminar_marcador(request, id):
    marcador = Marcador.objects.get(id=id)
    marcador.delete()
    return redirect('marcadorNuevo')

def temporada_detail(request,id):
    temporada = Temporada.objects.get(id=id)
    context = {'temporada': temporada}
    return render(request, 'temporadaDetail.html', context)

def nueva_temporada(request):
    if request.method == 'POST':
        form = TemporadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('temporadaNueva')

    form = TemporadaForm()
    temporada_list = Temporada.objects.all()
    context = {'form': form,
               'temporada_list': temporada_list
               }
    return render(request, 'temporadaNueva.html', context)

def editar_temporada(request, id):
    temporada = Temporada.objects.get(id=id)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect('temporadaNueva')

    form = TemporadaForm(instance=temporada)
    temporada_list = Temporada.objects.all()
    context = {'form': form,
               'temporada_list': temporada_list,
               'temporada': temporada
               }
    return render(request, 'temporadaEditar.html', context)

def eliminar_temporada(request, id):
    temporada = Temporada.objects.get(id=id)
    temporada.delete()
    return redirect('temporadaNueva')

def reglamento_detail(request,id):
    reglamento = Reglamento.objects.get(id=id)
    context = {'reglamento': reglamento}
    return render(request, 'reglamentoDetail.html', context)

def reglamento_visualizar(request):
    reglamento_list = Reglamento.objects.all()
    context = {'reglamento_list': reglamento_list,
               }
    return render(request, 'reglamentoVisualizar.html', context)
def nuevo_reglamento(request):
    if request.method == 'POST':
        form = ReglamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reglamentoNuevo')

    form = ReglamentoForm()
    reglamento_list = Reglamento.objects.all()
    context = {'form': form,
               'reglamento_list': reglamento_list
               }
    return render(request, 'reglamentoNuevo.html', context)

def editar_reglamento(request, id):
    reglamento = Reglamento.objects.get(id=id)
    if request.method == 'POST':
        form = ReglamentoForm(request.POST, instance=reglamento)
        if form.is_valid():
            form.save()
            return redirect('reglamentoNuevo')

    form = ReglamentoForm(instance=reglamento)
    reglamento_list = Reglamento.objects.all()
    context = {'form': form,
               'reglamento_list': reglamento_list,
               'reglamento': reglamento
               }
    return render(request, 'reglamentoEditar.html', context)
def eliminar_reglamento(request, id):
    reglamento = Reglamento.objects.get(id=id)
    reglamento.delete()
    return redirect('reglamentoNuevo')

def regla_detail(request,id):
    regla = Regla.objects.get(id=id)
    context = {'regla': regla,}
    return render(request, 'reglaDetail.html', context)

def regla_visualizar(request):
    regla_list = Regla.objects.all()
    context = {'regla_list': regla_list}
    return render(request, 'reglaVisualizar.html', context)

def nueva_regla(request):
    if request.method == 'POST':
        form = ReglaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reglaNueva')

    form = ReglaForm()
    regla_list = Regla.objects.all()
    context = {'form': form,
               'regla_list': regla_list
               }
    return render(request, 'reglaNueva.html', context)

def editar_regla(request, id):
    regla = Regla.objects.get(id=id)
    if request.method == 'POST':
        form = ReglaForm(request.POST, instance=regla)
        if form.is_valid():
            form.save()
            return redirect('reglaNueva')

    form = ReglaForm(instance=regla)
    regla_list = Regla.objects.all()
    context = {'form': form,
               'regla_list': regla_list,
               'regla': regla
               }
    return render(request, 'reglaEditar.html', context)

def eliminar_regla(request, id):
    regla = Regla.objects.get(id=id)
    regla.delete()
    return redirect('reglaNueva')

def inicio(request):
    return render(request, 'Inicio.html')



def formulario(request):
    return render(request, 'formulario.html')

def pinpon(request):
    return  render(request, 'pinpon.html')

def contacto1(request):
    return render(request, 'Contacto1.html')

def contacto2(request):
    return render(request, 'Contacto2.html')

def pageFutbol(request):
    return render(request, 'PageFutbol.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia 'inicio' al nombre de la vista que quieres redirigir después de iniciar sesión
        else:
            error_message = 'Credenciales inválidas'
            return render(request, 'registro/login.html', {'error_message': error_message})

    return render(request, 'registro/login.html')




