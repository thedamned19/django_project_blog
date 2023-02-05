from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('pages/', views.articulos, name="articulos"),
    path('create_articulo/', views.create_articulo, name="create_articulo"),
    path('eliminar_articulo/<int:id>/', views.eliminar_articulo, name="eliminar_articulo"),
    path('ver_articulo/<int:id>/', views.ver_articulo, name="ver_articulo"),
    path('editar_articulo/<int:id>/', views.editar_articulo, name="editar_articulo"),
    path('accounts/signup/', views.registro, name="registro"),
    path('accounts/login/', views.login_view, name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('accounts/profile/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar_avatar/', views.agregar_avatar, name="agregar_avatar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)