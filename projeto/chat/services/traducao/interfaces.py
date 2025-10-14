from abc import ABC, abstractmethod

class TraducaoError(Exception):
    """Erro de domínio para falhas na tradução."""
    pass

class ITradutor(ABC):
    @abstractmethod
    def traduzir(self, texto: str, idioma_destino: str) -> str:
        """Traduz o texto para o idioma destino e retorna a tradução."""
        raise NotImplementedError
