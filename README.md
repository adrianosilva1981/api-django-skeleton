### Instalação:
```python
# =============== a partir do zero ===============
# instalar o último django LTS:
$ pip install django==2.2.9

# criar projeto:
$ django-admin startproject nome-do-projeto .

# criar aplicação:
$ django-admin startapp nome-do-app

# instalar o django rest framework e o filter
$ pip install djangorestframework markdown django-filter

# fazer a migração:
$ python manage.py makemigrations
$ python manage.py migrate

# =============== a partir deste clone ===============
# criar user para acesso a api:
$ python manage.py createsuperuser

# rodar aplicação:
$ python manage.py runserver
```

### Referências:
[https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
