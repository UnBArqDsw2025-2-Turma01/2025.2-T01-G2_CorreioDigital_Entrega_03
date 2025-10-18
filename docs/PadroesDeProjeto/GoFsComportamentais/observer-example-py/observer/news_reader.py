from __future__ import annotations
from .observer import Observer
from .news_agency import NewsAgency


class NewsReader(Observer):
    def __init__(self, agency: NewsAgency, name: str) -> None:
        self._agency = agency
        self._name = name
        self._agency.attach(self)

    def update(self) -> None:
        print(f"[{self._name}] Nova notícia: {self._agency.get_news()}")
