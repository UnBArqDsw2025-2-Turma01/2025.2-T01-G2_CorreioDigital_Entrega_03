# src/correio_digital/observer_pattern.py

import abc
from .models import Mensagem  # Importação relativa

class Observer(metaclass=abc.ABCMeta):
    """
    Interface do Observer. Define o método update que os
    observadores concretos devem implementar.
    """
    @abc.abstractmethod
    def update(self, mensagem: Mensagem) -> None:
        """Recebe a atualização do Subject (push model)."""
        pass

class Subject(metaclass=abc.ABCMeta):
    """
    Interface do Subject. Define os métodos para anexar,
    desanexar e notificar observadores.
    """
    @abc.abstractmethod
    def attach(self, observer: Observer) -> None:
        """Anexa um observador ao Subject."""
        pass

    @abc.abstractmethod
    def detach(self, observer: Observer) -> None:
        """Desanexa um observador do Subject."""
        pass

    @abc.abstractmethod
    def notify(self) -> None:
        """Notifica todos os observadores sobre uma mudança."""
        pass
