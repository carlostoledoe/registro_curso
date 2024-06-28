from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # dirección: Dirección
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Direccion(models.Model):
    regiones = (
        ('i', 'Tarapacá'),
        ('ii', 'Antofagasta'),
        ('iii', 'Atacama'),
        ('iv', 'Coquimbo'),
        ('v', 'Valparaíso'),
        ('vi', "O'Higgins"),
        ('vii', 'Maule'),
        ('viii', 'Ñuble'),
        ('ix', 'Biobío'),
        ('x', 'La Araucanía'),
        ('xi', 'Los Ríos'),
        ('xii', 'Los Lagos'),
        ('xiv', 'Los Ríos'),
        ('xv', 'Aysén'),
        ('xvi', 'Magallanes y de la Antártica Chilena'),
        ('rm', 'Región Metropolitana de Santiago')
    )
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=regiones)
    estudiante = models.OneToOneField(Estudiante, related_name='direccion', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.calle} {self.comuna}'

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ForeignKey(Profesor, related_name='cursos', on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
    def __str__(self) -> str:
        return f'{self.codigo} {self.nombre}'


'''
relaciones:
    Estudiante - Dirección (Uno a Uno)
    Profesor - Curso (Uno a Muchos)
    Estudiante - Curso (Muchos a Muchos)
'''