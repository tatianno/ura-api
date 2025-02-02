from unittest import TestCase
from entities.boleto import Boleto


class BoletoTestCase(TestCase):

    def test_instanciando_boleto(self):
        dados_recebidos = {
            "id": 1,
            "codigo_barras": "123123123123123"
        }
        boleto = Boleto(**dados_recebidos)
        self.assertEqual(boleto.id, 1)
        self.assertEqual(boleto.codigo_barras, "123123123123123")