# src/correio_digital/sistema.py

import datetime
from typing import List
from .models import Mensagem
from .observer_pattern import Subject, Observer

class SistemaDeMensagens(Subject):
    """
    O Subject Concreto. Mantém o estado (mensagens) e notifica
    os observadores quando uma nova mensagem chega.
    """
    def __init__(self):
        self._observers: List[Observer] = []
        self._mensagens: List[Mensagem] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            print(f"[Sistema] {observer.__class__.__name__} foi anexado.")
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
            print(f"[Sistema] {observer.__class__.__name__} foi desanexado.")
        except ValueError:
            print(f"[Sistema] {observer.__class__.__name__} não está na lista.")

    def notify(self) -> None:
        """
        Dispara a atualização para todos os observadores,
        enviando a última mensagem (modelo Push).
        """
        if not self._mensagens:
            return

        ultima_mensagem = self._mensagens[-1]
        
        print(f"\n[Sistema] Notificando {len(self._observers)} observadores...")
        for observer in self._observers:
            observer.update(ultima_mensagem)

    def novaMensagem(self, remetente: str, destinatario: str, conteudo: str) -> None:
        """
        Método de negócio principal. Cria uma nova mensagem,
        armazena e notifica os observadores.
        """
        print(f"\n[Sistema] Nova mensagem recebida de {remetente}.")
        
        msg = Mensagem(
            remetente=remetente,
            destinatario=destinatario,
            conteudo=conteudo,
            timestamp=datetime.datetime.now()
        )
        self._mensagens.append(msg)
        
        # O Padrão Observer entra em ação aqui
        self.notify()
