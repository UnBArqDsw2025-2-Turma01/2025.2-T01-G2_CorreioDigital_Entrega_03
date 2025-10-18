from __future__ import annotations
from typing import List
from .subject import Subject
from .observer import Observer


class NewsAgency(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._news: str | None = None

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for o in list(self._observers):
            o.update()

    def set_news(self, news: str) -> None:
        self._news = news
        self.notify()

    def get_news(self) -> str | None:
        return self._news
