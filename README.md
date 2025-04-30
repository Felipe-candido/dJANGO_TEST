
# 🧪 Testes e Qualidade de Software com Django REST Framework (DRF)

Este repositório demonstra a aplicação de **testes automatizados** em uma API desenvolvida com **Django** e **Django REST Framework (DRF)**, com foco em **qualidade de software**, manutenção e confiabilidade do sistema.

---

## 🎯 Objetivos

- Demonstrar como testar endpoints de APIs REST com Django e DRF
- Garantir que regras de negócio funcionem como esperado
- Proteger endpoints contra regressões futuras
- Aumentar a confiabilidade com cobertura de testes

---

## 🧰 Ferramentas de Teste Utilizadas

### 1. **`unittest` (TestCase) - Nativo do Django**
- Baseado na biblioteca padrão do Python.
- Permite testar modelos, views, serializers, comandos customizados, etc.
- Classes: `TestCase`, `TransactionTestCase`, `SimpleTestCase`.

### 2. **`APIClient` (DRF)**
- Cliente HTTP para testes de APIs RESTful.
- Permite simular requisições `GET`, `POST`, `PUT`, `PATCH`, `DELETE` com ou sem autenticação.
  
```python
from rest_framework.test import APITestCase, APIClient

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        response = self.client.post('/api/users/', {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 201)
```

### 3. **`pytest` (opcional)**
- Framework de testes mais moderno e legível.
- Suporte a fixtures reutilizáveis, parametrização e plugins.
- Pode ser usado junto com Django com `pytest-django`.

```bash
pip install pytest pytest-django
pytest
```

### 4. **`coverage`**
- Ferramenta para medir o quanto do seu código está coberto por testes.
- Gera relatórios simples ou em HTML.

```bash
coverage run manage.py test
coverage report
coverage html  # Acesse htmlcov/index.html
```

### 5. **Factory Boy (mock de dados)**
- Gera objetos de teste (usuários, produtos, etc.) com facilidade.
- Ideal para criar fixtures dinâmicas para testes.

```python
import factory
from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', '123456')
```

---

## 📁 Estrutura dos Testes

```bash
project/
│
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── tests/
│       ├── test_models.py
│       ├── test_views.py
│       ├── test_serializers.py
│       ├── test_urls.py
│       └── test_api.py
```

---

## 🧪 Exemplos de Testes

### Testando um endpoint de criação (POST)

```python
def test_create_project(self):
    data = {"name": "Projeto X", "budget": 10000}
    response = self.client.post('/api/projects/', data)
    self.assertEqual(response.status_code, 201)
```

### Testando autenticação JWT

```python
def test_authenticated_access(self):
    user = UserFactory()
    self.client.force_authenticate(user=user)
    response = self.client.get('/api/secure-data/')
    self.assertEqual(response.status_code, 200)
```

---

## 🚀 Executando os Testes

```bash
# Com unittest (Django)
python manage.py test

# Com pytest (se configurado)
pytest

# Com cobertura
coverage run manage.py test
coverage report -m
```

---

## 📌 Boas Práticas

- Crie dados de teste com `Factory Boy`, evitando duplicações
- Teste cenários de erro (validações, autenticação, permissão)
- Use `reverse()` para resolver URLs dinamicamente
- Mantenha os testes organizados por tipo: models, serializers, views, etc.
- Almeje pelo menos 90% de cobertura nos arquivos críticos

---

## 📚 Referências

- [Documentação Django Testing](https://docs.djangoproject.com/pt-br/stable/topics/testing/)
- [DRF Testing](https://www.django-rest-framework.org/api-guide/testing/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Pytest Django](https://pytest-django.readthedocs.io/)
- [Factory Boy](https://factoryboy.readthedocs.io/)

---


