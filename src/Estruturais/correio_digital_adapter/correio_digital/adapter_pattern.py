"""
Interfaces do padrão Adapter para tradução de mensagens.
Define o contrato (Target) que todos os adaptadores devem seguir.
"""

from abc import ABC, abstractmethod


class TraducaoError(Exception):
    """
    Exceção de domínio para falhas no serviço de tradução.
    Permite tratamento específico de erros de tradução.
    """
    pass


class ITradutor(ABC):
    """
    Interface Target do padrão Adapter.
    Define o contrato padrão que o cliente (ServicoTraducao) espera.
    
    Qualquer novo adaptador de API de tradução deve implementar esta interface.
    """
    
    @abstractmethod
    def traduzir(self, texto: str, idioma_destino: str) -> str:
        """
        Traduz o texto para o idioma destino.
        
        Args:
            texto: Texto a ser traduzido
            idioma_destino: Código ISO do idioma destino (ex: 'EN', 'PT', 'ES')
            
        Returns:
            Texto traduzido
            
        Raises:
            TraducaoError: Quando a tradução falhar
        """
        pass
    
    def validar_idioma(self, codigo_idioma: str) -> bool:
        """
        Valida se o código de idioma é suportado.
        Implementação padrão - pode ser sobrescrita.
        """
        # Códigos ISO 639-1 mais comuns
        idiomas_suportados = {'PT', 'EN', 'ES', 'FR', 'DE', 'IT', 'JA', 'ZH', 'AR', 'RU'}
        return codigo_idioma.upper() in idiomas_suportados
