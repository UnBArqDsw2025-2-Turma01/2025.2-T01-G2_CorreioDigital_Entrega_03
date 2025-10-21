"""
Modelo de dados para o sistema de tradução do CorreioDigital.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Mensagem:
    """
    Representa uma mensagem no sistema CorreioDigital.
    
    Atributos:
        conteudo: Texto da mensagem
        idioma_origem: Código ISO do idioma original (ex: 'PT', 'EN')
        idioma_destino: Código ISO do idioma destino para tradução (opcional)
        traducao: Texto traduzido (preenchido após tradução)
        remetente: Identificador do remetente
        destinatario: Identificador do destinatário
        timestamp: Data e hora de criação da mensagem
    """
    conteudo: str
    idioma_origem: str
    remetente: str
    destinatario: str
    idioma_destino: Optional[str] = None
    traducao: Optional[str] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def definir_traducao(self, texto_traduzido: str) -> None:
        """Define o texto traduzido da mensagem."""
        self.traducao = texto_traduzido
    
    def obter_texto_exibicao(self) -> str:
        """Retorna o texto a ser exibido (tradução se disponível, senão original)."""
        return self.traducao if self.traducao else self.conteudo
