"""
Pacote de implementação do padrão Adapter no domínio CorreioDigital.
Fornece adaptadores para serviços externos de tradução.
"""

from .models import Mensagem
from .adapter_pattern import ITradutor, TraducaoError
from .adaptadores import (
    GoogleTranslateAPI,
    DeepLAPI,
    GoogleAdapter,
    DeepLAdapter
)
from .servico import ServicoTraducao

__all__ = [
    'Mensagem',
    'ITradutor',
    'TraducaoError',
    'GoogleTranslateAPI',
    'DeepLAPI',
    'GoogleAdapter',
    'DeepLAdapter',
    'ServicoTraducao'
]
