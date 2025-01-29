from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def criar_usuario_admin():
    admin, _ = User.objects.get_or_create(username='admin')
    admin.is_staff = True
    admin.is_superuser = True
    admin.set_password('admin')
    admin.save()
    print(f'Usuario {admin} criado com sucesso!')
    token, _ = Token.objects.get_or_create(user=admin)
    print(f'Token {token} criado com sucesso!')