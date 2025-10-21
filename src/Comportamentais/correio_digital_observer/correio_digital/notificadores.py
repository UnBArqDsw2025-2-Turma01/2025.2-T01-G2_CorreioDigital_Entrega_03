# src/correio_digital/notificadores.py

from .observer_pattern import Observer
from .models import Mensagem

class NotificadorWeb(Observer):
    """
    Um observador concreto que simula o envio de uma notificação
    para a interface web.
    """
    def update(self, mensagem: Mensagem) -> None:
        print(f"  [WEB] Notificação Push: 'Nova mensagem de {mensagem.remetente}: {mensagem.conteudo[:20]}...'")

class NotificadorEmail(Observer):
    """
    Um observador concreto que simula o envio de um e-mail.
    """
    def update(self, mensagem: Mensagem) -> None:
        print(f"  [EMAIL] Enviando e-mail para {mensagem.destinatario}: 'Assunto: Nova mensagem de {mensagem.remetente}'")

class NotificadorMobile(Observer):
    """
    Um observador concreto que simula o envio de uma notificação
    para um dispositivo móvel.
    """
    def update(self, mensagem: Mensagem) -> None:
        print(f"  [MOBILE] Notificação (Pling!): '{mensagem.remetente} disse: {mensagem.conteudo[:15]}...'")
