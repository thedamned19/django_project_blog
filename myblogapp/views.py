from django.http import HttpResponse
from .models import Usuario, Articulo, Avatar
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import CreateArticulo, UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello world!!!</h1>")

def index(request):
    return render(request, "index.html")

def about(request):
    creador = "Ernesto Leimsieder"
    texto_uno = "Mi nombre es Ernesto, soy Analista Programador recibido en la Universidad ORT de Montevideo en Noviembre de 2022."
    texto_dos = "Actualmente estoy aprendiendo el lenguaje de programación Python y el Framework Django. Seguiré actualizandome en tecnologías haciendo el curso de Data Science a través de Coderhouse ya que el camino que he elejido es de aprendizaje constante."
    return render(request, "about.html",
    {"creador":creador, "texto_uno":texto_uno, "texto_dos":texto_dos})

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html",
            {"usuarios":usuarios})

def articulos(request):
    articulos = Articulo.objects.all()
    paginator = Paginator(articulos,3)
    num_pagina = request.GET.get("page")
    pagina_actual = paginator.get_page(num_pagina)
    cant_articulos = articulos.__len__
    return render(request, "articulos.html",
            {"articulos":pagina_actual, "cant_articulos":cant_articulos})

@login_required
def create_articulo(request):
    if request.method == "GET":
        return render(request, "create_articulo.html",
                      {"form": CreateArticulo()})
    else:
        Articulo.objects.create(titulo = request.POST["titulo"],
            subtitulo = request.POST["subtitulo"],
            cuerpo = request.POST["cuerpo"], 
            autor_id = request.user.id,
            imagen = request.FILES["imagen"])
    return redirect("articulos")

@login_required
def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id = id)
    articulo.delete()
    articulos = Articulo.objects.all()
    contexto = {"articulos":articulos}
    return render(request, "articulos.html", contexto)

def ver_articulo(request, id):
    articulo = Articulo.objects.get(id = id)
    contexto = {
        "articulo":articulo
    }
    return render(
        request=request,
        template_name="detalle_articulo.html",
        context=contexto
    )

@login_required
def editar_articulo(request, id):
    articulo = Articulo.objects.get(id = id)
    if request.method == "POST":
        formulario = CreateArticulo(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data["titulo"]
            articulo.subtitulo = data["subtitulo"]
            articulo.cuerpo = data["cuerpo"]
            articulo.save()
            articulos = Articulo.objects.all()
            cant_articulos = articulos.__len__
            return render(request, "articulos.html", {"articulos":articulos, "cant_articulos":cant_articulos})
    else:
        inicial = {
                    'titulo':articulo.titulo,
                    'subtitulo':articulo.subtitulo,
                    'cuerpo':articulo.cuerpo,
        }
        formulario = CreateArticulo(initial=inicial)
        return render(
                request=request,
                template_name='edit_articulo.html',
                context={'form':formulario, 'articulo':articulo})
    
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name="registro.html",
        context={"form":formulario}
    )
    
def login_view(request):
    next_url = request.GET.get("next")
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data.get("username")
            contrasenia = data.get("password")
            user = authenticate(username=usuario, password=contrasenia)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)    
                url_exitosa = reverse("index")
                return redirect(url_exitosa) 
    else:
        formulario = AuthenticationForm()
        return render(
            request=request,
            template_name="login.html",
            context={"form":formulario}
        )

class CustomLogoutView(LogoutView):
    template_name = "logout.html"
    next_page = reverse_lazy("logout")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("index")
    template_name = "formulario_perfil.html"

    def get_object(self, queryset=None):
        return self.request.user
    
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name="formulario_avatar.html",
        context={"form":formulario}
    )

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy("articulos")
    template_name = "layouts/confirmar_eliminacion_articulo.html"