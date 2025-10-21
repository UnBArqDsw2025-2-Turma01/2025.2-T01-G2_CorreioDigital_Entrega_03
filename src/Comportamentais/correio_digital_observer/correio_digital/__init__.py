# src/correio_digital/__init__.py

from .models import Mensagem
from .observer_pattern import Observer, Subject
from .sistema import SistemaDeMensagens
from .notificadores import NotificadorWeb, NotificadorEmail, NotificadorMobile

# Expondo as classes principais do pacote
__all__ = [
    'Mensagem',
    'Observer',
    'Subject',
    'SistemaDeMensagens',
    'NotificadorWeb',
    'NotificadorEmail',
    'NotificadorMobile'
]
