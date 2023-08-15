import enum

from django.db import models

class EleccionDeRol(enum.Enum):
    Jugador = 'Jugador'
    Director_Tecnico = 'Director Tecnico'
    Arbitro = 'Arbitro'

class EstadoInscripcion(enum.Enum):
    REGISTRADO = 'Registrado'
    EN_PROCESO = 'En Proceso'
    ANULADA = 'Anulada'

class EscogerDeporte(enum.Enum):
    FUTBOL = 'Futbol'
    PING_PONG = 'Ping Pong'

class Categoria(enum.Enum):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'

class EstadoPartido(enum.Enum):
    FINALIZADO = 'Finalizado'
    APLAZADO = 'Aplazado'
    SUSPENDIDO = 'Suspendido'
    INICIADO = 'Iniciado'
    ENTRETIEMPO = 'Entretiempo'
    NO_INICIADO = 'No Iniciado'

class ModoJuego(enum.Enum):
    Eliminacion_Simple = 'Eliminacion simple'
    Rondas_de_Clasificacion = 'Rondas de Clasificacion'
    Puntuacion_Acumulativa = 'Puntuacion Acumulativa'
    Uno_contra_Uno = 'Uno contra Uno'
    Ligas = 'Ligas'
    Fase_Grupos = 'Fase de Grupos'
    Eliminatorias = 'Eliminatorias'

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    EscogerDeporte = models.CharField(max_length=10, choices=[(tag.value, tag.value) for tag in EscogerDeporte], blank=True, null=True)
    EleccionDeRol = models.CharField(max_length=20, choices=[(tag.value, tag.value) for tag in EleccionDeRol], blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Jugador(models.Model):
    numero_Camiseta = models.PositiveIntegerField()
    posicion = models.CharField(max_length=50,default=None)
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='RegistroList', default=None)  # relacion de uno a muchos

    def __str__(self):
        return f"{self.registro.nombre} {self.registro.apellido}"

class Inscripcion(models.Model):
    fecha_solicitud = models.DateField(blank=True,null=True)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='jugadorList', default=None)  # relacion de uno a muchos
    EstadoInscripcion = models.CharField(max_length=10, choices=[(tag.value, tag.value) for tag in EstadoInscripcion], default='En Proceso')
    def __str__(self):
        return f"{self.jugador.registro.nombre} {self.jugador.registro.apellido}"


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    numero_Jugadores = models.PositiveIntegerField()
    categoria = models.CharField(max_length=10, choices=[(tag.value, tag.value) for tag in Categoria], blank=True, null=True)
    inscripcion = models.ManyToManyField(Inscripcion, related_name='equipos', blank=True)

    #Relaciones
    def __str__(self):
        return self.nombre

class Sorteo(models.Model):
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    Equipo_list = models.ManyToManyField(Equipo, related_name='sorteos', blank=True)
    equipos_locales = models.ManyToManyField(Equipo, related_name='sorteos_locales', blank=True)
    equipos_visitantes = models.ManyToManyField(Equipo, related_name='sorteos_visitantes', blank=True)
    def __str__(self):
        return f"{self.fecha} {self.hora}"

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad_maxima_equipos = models.PositiveIntegerField()


    #Relaciones
    EquipoList = models.ManyToManyField(Equipo, related_name='grupos', blank=True)
    equipos = models.ManyToManyField(Equipo)
    def __str__(self):
        return self.nombre




class Partido(models.Model):
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    numero_encuentro = models.PositiveIntegerField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    estado = models.CharField(max_length=20, choices=[(tag.value, tag.value) for tag in EstadoPartido], blank=True, null=True, default='No Iniciado')

    #Relaciones
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

class Marcador(models.Model):
    nombre_equipo_local = models.CharField(max_length=50)
    nombre_equipo_visitante = models.CharField(max_length=50)
    punto_marcador_local = models.PositiveIntegerField()
    punto_marcador_visitante = models.PositiveIntegerField()

    def __str__(self):
        return f"Resultado = {self.nombre_equipo_local}: {self.punto_marcador_local} - {self.nombre_equipo_visitante}: {self.punto_marcador_visitante}"


class Temporada(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    ModoJuego = models.CharField(max_length=50, choices=[(tag.value, tag.value) for tag in ModoJuego], blank=True, null=True)

    #Relaciones
    EquipoList = models.ManyToManyField(Equipo, related_name='temporadas', blank=True, default=None)

    def __str__(self):
        return self.nombre

class Reglamento(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField(blank=True, null=True)

    regla_list = models.ManyToManyField('Regla', related_name='reglamentos', blank=True, default=None)
    def __str__(self):
        return self.nombre

class Regla(models.Model):
    nombre_regla = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre_regla

class TipoCalendario(models.Model):
    nombre = models.CharField(max_length=100)

class Calendario(models.Model):
    nombre = models.CharField(max_length=100, default=None)
    tipo_calendario = models.ForeignKey(TipoCalendario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
