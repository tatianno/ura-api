from unittest import TestCase
from entities.protocolo import Protocolo


class ProtocoloTestCase(TestCase):

    def test_instanciando_protocolo(self):
        dados_recebidos = {
            "id": 2,
            "data": "2025-02-02T11:27:49.216329-03:00",
            "cliente": 2,
            "telefone": "1133223322",
            "numero": "202502022"
        }
        protocolo = Protocolo(**dados_recebidos)
        self.assertEqual(protocolo.id, 2)
        self.assertEqual(protocolo.data, "2025-02-02T11:27:49.216329-03:00")
        self.assertEqual(protocolo.cliente, 2)
        self.assertEqual(protocolo.telefone, "1133223322")
        self.assertEqual(protocolo.numero, "202502022")