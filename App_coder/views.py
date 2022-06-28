from django.shortcuts import render
from App_coder.models import Villa_olimpica, Deportista, Disciplina
from App_coder.forms import Villa_olimpica_form, Disciplina_form, Deportista_form

# Create your views here.

def inicio(request):
    return render(request, "App_coder/inicio.html")

def villa_olimpica(request):
    
    if request.method == 'POST':

        mi_formulario= Villa_olimpica_form(request.POST)

        if mi_formulario.is_valid():

            informacion= mi_formulario.cleaned_data

            villa= Villa_olimpica (nombre=informacion['nombre'], ubicacion=informacion['ubicacion'], numero=informacion['numero'], fundacion=informacion['fundacion'])

            villa.save()

            return render(request, "App_coder/inicio.html")

    else:

        mi_formulario= Villa_olimpica_form()

    return render(request, "App_coder/villaolimpica.html", {"mi_formulario":mi_formulario})

def disciplina(request):

    if request.method == 'POST':

        mi_formulario= Disciplina_form(request.POST)

        if mi_formulario.is_valid():

            informacion= mi_formulario.cleaned_data

            disciplina= Disciplina (nombre=informacion['nombre'], se_juega_con_balon=informacion['se_juega_con_balon'])

            disciplina.save()

            return render(request, "App_coder/inicio.html")

    else:

        mi_formulario= Disciplina_form()

    return render(request, "App_coder/disciplina.html", {"mi_formulario":mi_formulario})

def deportista(request):

    if request.method == 'POST':

        mi_formulario= Deportista_form(request.POST)

        if mi_formulario.is_valid():

            informacion= mi_formulario.cleaned_data

            deportista= Deportista (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

            deportista.save()

            return render(request, "App_coder/inicio.html")

    else:

        mi_formulario= Deportista_form()


    return render(request, "App_coder/deportista.html", {"mi_formulario":mi_formulario})

def busqueda(request):

    if request.GET['ubicacion']:

        ubicacion = request.GET['ubicacion']
        villas = Villa_olimpica.objects.filter(ubicacion__icontains=ubicacion)

        return render(request, "App_coder/inicio.html", {"villas":villas, "ubicacion":ubicacion})

    else:

        respuesta = "No enviaste datos"

    return render(request,"App_coder/inicio.html", {"respuesta":respuesta})

