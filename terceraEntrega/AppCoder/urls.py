from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_curso", views.curso_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscarCurso", views.buscarCurso),
    path("buscar_alumno", views.buscar_alumno),
    path("buscarAlumno", views.buscarAlumno),
    path("buscar_profesor", views.buscar_profesor),
    path("buscarProfesor", views.buscarProfesor),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso")
]