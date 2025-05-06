from django.test import TestCase
from cadastro.models import usuario
from django.db import IntegrityError
import factory


class PessoaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = usuario

    nome = "Joao da Silva"
    email = "orlando@teste.com"



class UsuarioModelTest(TestCase):

      def test_criacao_de_pessoa1(self):
            pessoa = PessoaFactory()  

            self.assertEqual(pessoa.email, 'orlando@teste.com')
            self.assertEqual(pessoa.nome, 'Joao da Silva')

      def test_create_usuario2(self):
            user = usuario.objects.create(
                  email = 'teste@teste.com',
                  nome = 'teste',
                  sobrenome = 'testando',
                  is_active = True,
                  is_staff = False,
                  tipo = 'locatario'
            )
            
            self.assertEqual(user.email, 'teste@teste.com')
            self.assertEqual(user.nome, 'teste')
            self.assertEqual(user.sobrenome, 'testando')
            self.assertEqual(user.is_active, True)
            self.assertEqual(user.is_staff, False)
            self.assertEqual(user.tipo, 'locatario')

      
      def test_email_unico(self):
            
            usuario.objects.create(
                  email = 'teste@teste.com',
                  nome = 'teste',
                  sobrenome = 'testando',
                  is_active = True,
                  is_staff = False,
                  tipo = 'locatario'
                  )
            
            with self.assertRaises(IntegrityError):
                  user2 = usuario.objects.create(
                  email = 'teste@teste.com',
                  nome = 'teste2',
                  sobrenome = 'testando2',
                  is_active = True,
                  is_staff = False,
                  tipo = 'locatario'
                  )
            