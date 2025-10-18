from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def detach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
