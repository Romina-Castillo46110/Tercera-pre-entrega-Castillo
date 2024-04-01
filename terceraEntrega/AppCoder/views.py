from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from AppCoder.forms import Alumno_formulario, Curso_formulario, Profesor_formulario

def inicio(request):
    return render(request, "base.html")

def alta_curso(request, nombre, camada):
    curso = Curso(nombre=nombre , camada=camada)
    curso.save()
    mensaje_cursos = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(mensaje_cursos)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla_cursos = loader.get_template("cursos.html")
    documento_cursos = plantilla_cursos.render(dicc)
    return HttpResponse(documento_cursos)


def alumnos(request):
    return render(request , "alumnos.html")

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    lista_alumnos = {"Alumnos": alumnos}
    plantilla_alumnos = loader.get_template("alumnos.html")
    documento_alumnos = plantilla_alumnos.render(lista_alumnos)
    return HttpResponse(documento_alumnos)

def alta_alumno(request, nombre, legajo):
    alumno = Alumno(nombre=nombre , legajo=legajo)
    alumno.save()
    mensaje_alum = f"Se guardó en la base de datos el alumno: {alumno.nombre} {alumno.legajo}"
    return HttpResponse(mensaje_alum)

def ver_profesores(request):
    profesores = Profesor.objects.all()
    lista_profesores = {"Profesores": profesores}
    plantilla_prof = loader.get_template("profesores.html")
    documento_profesores =plantilla_prof.render(lista_profesores)
    return HttpResponse(documento_profesores)

def alta_profesor(request, nombre, legajo):
    profesor = Profesor(nombre=nombre, legajo=legajo)
    profesor.save()
    mensaje_prof = f"Se guardó en la BD el profesor: {profesor.nombre} {profesor.legajo}"
    return HttpResponse(mensaje_prof)

def curso_formulario(request):
    if request.method == "POST":
        curso_form = Curso_formulario( request.POST )
        if curso_form.is_valid():
            datos_curso = curso_form.cleaned_data
            curso = Curso( nombre=datos_curso["nombre"], camada=datos_curso["camada"])
            curso.save()
            return render(request, "formularioCurso.html")
    return render(request, "formularioCurso.html")

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscarCurso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request ,  "resultado_busquedaCurso.html", {"cursos": cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
def alumno_formulario(request):
    if request.method == "POST":
        alumno_form = Alumno_formulario( request.POST )
        if alumno_form.is_valid():
            datos_alumno = alumno_form.cleaned_data
            alumno = Alumno( nombre=datos_alumno["nombre"], legajo=datos_alumno["legajo"])
            alumno.save()
            return render(request, "formularioAlumno.html")
    return render(request, "formularioAlumno.html")

def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscarAlumno(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request ,  "resultado_busquedaAlumno.html", {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")

def profesor_formulario(request):
    if request.method == "POST":
        profesor_form = Profesor_formulario( request.POST )
        if profesor_form.is_valid():
            datos_profesor = profesor_form.cleaned_data
            profesor = Profesor( nombre=datos_profesor["nombre"], legajo=datos_profesor["legajo"])
            profesor.save()
            return render(request, "formularioProfesor.html")
    return render(request, "formularioProfesor.html")

def buscar_profesor(request):
    return render(request, "buscar_profesor.html")

def buscarProfesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render( request ,  "resultado_busquedaProfesor.html", {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")
    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    
    return render(request, "cursos.html", {"cursos":curso})

def editar(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso_form = Curso_formulario(request.POST)
        if curso_form.is_valid():
            datos_curso = curso_form.cleaned_data
            curso.nombre = datos_curso["nombre"]
            curso.camada = datos_curso["camada"]
            curso.save()
            curso = Curso.objects.all()
            return render(request,"cursos.html",{"cursos":curso})
    else:
        curso_form = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})
    return render(request,"editar_curso.html",{"curso_form": curso_form, "curso":curso})

