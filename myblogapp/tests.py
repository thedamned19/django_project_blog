from django.test import TestCase
from .models import Articulo

# Create your tests here.
class ArticuloTests(TestCase):

    def test_creacion_de_articulo_autor(self):
        """
        Prueba crear articulo con un autor que no existe.
        """
        articulo_con_autor_invalido = Articulo.objects.create(
            titulo="titulo_A", subtitulo="subtitulo_A", cuerpo="cuerpo_A", autor_id=200
        )
        # Compruebo que el articulo fue creado
        self.assertEqual(Articulo.objects.all().count(), 1)
        self.assertIsNotNone(articulo_con_autor_invalido)

    def test_creacion_de_articulo_titulo(self):
        """
        Prueba crear articulo sin titulo.
        """
        articulo_sin_titulo = Articulo.objects.create(
            titulo="", subtitulo="subtitulo_A", cuerpo="cuerpo_A", autor_id=1
        )
        # Compruebo que el articulo fue creado
        self.assertEqual(Articulo.objects.all().count(), 1)
        self.assertIsNotNone(articulo_sin_titulo)

        
