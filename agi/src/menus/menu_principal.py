from agi.base_agi import BaseAgi
from services.base_service import BaseApiClienteService


class MenuPrincipal:

    def __init__(self, api_service: BaseApiClienteService, agi: BaseAgi):
        self._api_service = api_service
        self._agi = agi
    