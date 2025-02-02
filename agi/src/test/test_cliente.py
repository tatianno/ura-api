from unittest import TestCase
from entities.cliente import Cliente


class ClienteTestCase(TestCase):

    def test_instanciando_cliente(self):
        dados_recebidos = {
            "id": 3,
            "nome": "Calebe e Fátima Entulhos Ltda",
            "em_massiva": True
        }
        cliente = Cliente(**dados_recebidos)
        self.assertEqual(cliente.id, 3)
        self.assertEqual(cliente.nome, "Calebe e Fátima Entulhos Ltda")
        self.assertEqual(cliente.em_massiva, True)