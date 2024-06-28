from main.models import Estudiante, Direccion, Profesor, Curso

def crear_curso(codigo:str, nombre:str, version:int):
    curso = Curso(
        codigo = codigo,
        nombre = nombre,
        version = version
    )
    curso.save()
    return curso

def crear_profesor(rut:str, nombre:str, apellido:str):
    profesor = Profesor(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
    )
    profesor.save()
    return profesor




#crear_estudiante
#crear_direccion
#obtiene_estudiante
#obtiene_profesor
#obtiene_curso
#agrega_profesor_a_curso
#agrega_cursos_a_estudiante
#imprime_estudiante_cursos