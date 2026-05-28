from django.test import TestCase
from rest_framework.test import APITestCase
from edu.models import Autor
from django.urls import reverse
from edu.serializers import AutorSerializer
from django.utils import timezone
from datetime import timedelta
from edu.forms import LivroForm
from edu.models import Editora
from rest_framework import status

class AutorModelTest(TestCase):

    def test_str_retorna_nome(self):
        autor = Autor.objects.create(nome='Machado de Assis')

        self.assertEqual(str(autor), 'Machado de Assis')


class ListarAutoresViewTest(TestCase):

    def test_listar_autores(self):
        Autor.objects.create(nome='Clarice Lispector')

        response = self.client.get(
            reverse('listar_autores')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Clarice Lispector')

class LivroFormTest(TestCase):

    def test_data_futura_invalida(self):
        editora = Editora.objects.create(nome='Editora Abril')

        data_futura = timezone.now() + timedelta(days=1)

        form = LivroForm(data={
            'isbn': '1234567890123',
            'titulo': 'Livro Teste',
            'publicacao': data_futura,
            'preco': 50.00,
            'estoque': 10,
            'editora': editora.id
        })

        self.assertFalse(form.is_valid())

class AutorSerializerTest(TestCase):

    def test_serializer_autor(self):
        autor = Autor.objects.create(nome='Paulo Coelho')

        serializer = AutorSerializer(autor)

        self.assertEqual(
            serializer.data['nome'],
            'Paulo Coelho'
        )

class AutorAPITest(APITestCase):

    def test_api_lista_autores(self):
        Autor.objects.create(nome='George Orwell')

        url = reverse('autor-list')

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data[0]['nome'],
            'George Orwell'
        )