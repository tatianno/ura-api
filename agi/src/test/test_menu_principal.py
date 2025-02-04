from unittest import TestCase
from unittest.mock import MagicMock
from agi.base_agi import BaseAgi
from entities.cliente import Cliente
from menus.menu_principal import MenuPrincipal, ExcedidoLimiteTentativasException


class MenuPrincipalTestCase(TestCase):

    def test_reproduzir_prompt_informe_documento_invalido(self):
        api_service = MagicMock()
        agi: BaseAgi = MagicMock()
        agi.reproduzir_prompt.return_value = '123456789'
        menu_principal = MenuPrincipal(api_service, agi)
        self.assertRaises(
            ExcedidoLimiteTentativasException,
            menu_principal._reproduzir_prompt_informe_documento
        )
    
    def test_reproduzir_prompt_informe_documento_invalido(self):
        dados_cliente = dados_recebidos = {
            "id": 3,
            "nome": "Calebe e Fátima Entulhos Ltda",
            "em_massiva": True
        }
        cliente = Cliente(**dados_recebidos)
        api_service = MagicMock()
        api_service.consultar_cliente.return_value = cliente
        agi: BaseAgi = MagicMock()
        agi.reproduzir_prompt.return_value = '90879834099'
        menu_principal = MenuPrincipal(api_service, agi)
        cliente_consulta = menu_principal._reproduzir_prompt_informe_documento()
        self.assertEqual(cliente, cliente_consulta)