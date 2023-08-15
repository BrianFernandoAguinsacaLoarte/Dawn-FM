from django import forms


from dawnbem.models import Registro, Jugador, Inscripcion, Equipo, Partido, Marcador, Temporada, Reglamento, Regla, \
    Sorteo, Grupo


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'edad', 'EscogerDeporte', 'EleccionDeRol']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su edad'
                }

            ),
            'EscogerDeporte': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su deporte'
                }
            ),
            'EleccionDeRol': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rol'
                }
            ),

        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'EscogerDeporte': 'Deporte',
            'EleccionDeRol': 'Rol',
        }
class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['registro', 'numero_Camiseta', 'posicion', ]
        widgets = {
            'registro': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su registro'
                }
            ),
            'numero_Camiseta': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de camiseta'
                }
            ),
            'posicion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su posición'
                }
            ),

        }
        labels = {
           'registro': 'Registro',
           'numero_Camiseta': 'Número de camiseta',
           'posicion': 'Posición',

        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['fecha_solicitud', 'jugador','EstadoInscripcion']
        widgets = {
            'fecha_solicitud': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha de solicitud'
                }
            ),
            'jugador': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su jugador'
                }
            ),
            'EstadoInscripcion': forms.HiddenInput(),

        }
        labels = {
            'fecha_solicitud': 'Fecha de solicitud',
            'jugador': 'Jugador',
            'EstadoInscripcion': 'Estado de inscripción',
        }


class EquipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las inscripciones registradas y establecer el queryset del campo 'inscripcion'
        self.fields['inscripcion'].queryset = Inscripcion.objects.filter(EstadoInscripcion='Registrado')

    class Meta:
        model = Equipo
        fields = ['nombre', 'numero_Jugadores', 'categoria', 'inscripcion']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del Equipo'
                }
            ),
            'numero_Jugadores': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de jugadores'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su categoría'
                }
            ),
            'inscripcion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su inscripción'
                }
            ),
        }
        labels = {
            'nombre': 'Nombre',
            'numero_Jugadores': 'Número de jugadores',
            'categoria': 'Categoría',
            'inscripcion': 'Inscripciones Registradas',
        }


class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['fecha','hora','numero_encuentro','equipo_local','equipo_visitante','estado']
        widgets = {
            'fecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su hora'
                }
            ),
            'numero_encuentro': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de encuentro'
                }
            ),
            'equipo_local': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su equipo local'
                }
            ),
            'equipo_visitante': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su equipo Visitante'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su estado'
                }
            ),
        }
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'numero_encuentro': 'Número de encuentro',
            'estado': 'Estado',

        }

class MarcadorForm(forms.ModelForm):
    class Meta:
        model = Marcador
        fields = ['nombre_equipo_local', 'nombre_equipo_visitante', 'punto_marcador_local', 'punto_marcador_visitante']
        widgets = {
            'nombre_equipo_local': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de equipo local'
                }
            ),
            'nombre_equipo_visitante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de equipo visitante'
                }
            ),
            'punto_marcador_local': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su punto de marcador local'
                }
            ),
            'punto_marcador_visitante': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su punto de marcador visitante'
                }
            ),
        }

        labels = {
            'nombre_equipo_local': 'Nombre de equipo local',
            'nombre_equipo_visitante': 'Nombre de equipo visitante',
            'punto_marcador_local': 'Punto de marcador local',
            'punto_marcador_visitante': 'Punto de marcador visitante',
        }

class TemporadaForm(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'ModoJuego', 'EquipoList']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'fecha_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha de inicio'
                }
            ),
            'fecha_fin': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha de fin'
                }
            ),
            'ModoJuego': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su modo de juego'
                }
            ),
            'EquipoList': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su lista de equipos'
                }
            ),
        }
        labels = {
            'nombre': 'Nombre',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de fin',
            'ModoJuego': 'Modo de juego',
            'EquipoList': 'Lista de equipos',
        }

class ReglamentoForm(forms.ModelForm):
    class Meta:
        model = Reglamento
        fields = ['nombre','descripcion', 'fecha', 'regla_list']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su descripción'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha'
                }
            ),
            'regla_list': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su lista de reglas'
                }
            ),
        }
        labels = {
            'nombre': 'Nombre',
            'fecha': 'Fecha',
            'descripcion': 'Descripción',
            'regla_list': 'Lista de reglas',
        }

class ReglaForm(forms.ModelForm):
    class Meta:
        model = Regla
        fields = ['nombre_regla','descripcion']
        widgets = {
            'nombre_regla': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de regla'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su descripción'
                }
            ),
        }
        labels = {
            'nombre_regla': 'Nombre de regla',
            'descripcion': 'Descripción',
        }

class SorteoForm(forms.ModelForm):
    
    class Meta:
        model= Sorteo
        fields = ['fecha', 'hora', 'Equipo_list','equipos_locales', 'equipos_visitantes']
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dd/mm/aaaa'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm:ss'
                }
            ),
            'Equipo_list': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su equipo'
                }
            ),
            'equipos_locales': forms.HiddenInput(),

            'equipos_visitantes': forms.HiddenInput(),
        }
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'Equipo_list': 'Equipo',
            'equipos_locales': 'Equipo local',
            'equipos_visitantes': 'Equipo visitante',
        }

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'capacidad_maxima_equipos', 'EquipoList']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'capacidad_maxima_equipos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su capacidad máxima de equipos'
                }
            ),

            'EquipoList': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su equipo'
                }
            ),
        }
        labels = {
            'nombre': 'Nombre',
            'capacidad_maxima_equipos': 'Capacidad máxima de equipos',
            'EquipoList': 'Equipo',
        }