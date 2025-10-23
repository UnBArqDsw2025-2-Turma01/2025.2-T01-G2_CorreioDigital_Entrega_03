# src/correio_digital/models.py

import datetime
from dataclasses import dataclass

@dataclass
class Mensagem:
    """
    Classe de dados para representar uma mensagem no sistema.
    """
    remetente: str
    destinatario: str
    conteudo: str
    timestamp: datetime.datetime
