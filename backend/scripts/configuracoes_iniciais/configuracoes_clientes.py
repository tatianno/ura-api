from cliente.models import Cliente
from boleto.models import Boleto


DADOS_CLIENTE = [
    {
        'nome': 'Letícia Sophia Lívia Almeida',
        'documento': '64810797058',
        'em_massiva': False,
        'boletos': []
    },
    {
        'nome': 'Laís Mariana Baptista',
        'documento': '65112947063',
        'em_massiva': False,
        'boletos': ['123123123123123']
    },
    {
        'nome': 'Calebe e Fátima Entulhos Ltda',
        'documento': '36272715000140',
        'em_massiva': True,
        'boletos': []
    }
]


def criar_clientes():
    print('Removendo registros anteriores')
    Cliente.objects.all().delete()

    for cliente_dict in DADOS_CLIENTE:
        cliente = Cliente.objects.create(
            nome=cliente_dict.get('nome'),
            documento=cliente_dict.get('documento'),
            em_massiva=cliente_dict.get('em_massiva'),
        )
        print(f'Cliente {cliente} criado com sucesso!')

        for codigo_barras in cliente_dict.get('boletos'):
            boleto = Boleto.objects.create(
                codigo_barras=codigo_barras,
                cliente=cliente
            )
            print(f'Boleto {boleto} criado com sucesso!')