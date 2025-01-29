import sys, os, django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()


from scripts.configuracoes_iniciais.configuracoes_usuario import criar_usuario_admin
from scripts.configuracoes_iniciais.configuracoes_clientes import criar_clientes


criar_usuario_admin()
criar_clientes()