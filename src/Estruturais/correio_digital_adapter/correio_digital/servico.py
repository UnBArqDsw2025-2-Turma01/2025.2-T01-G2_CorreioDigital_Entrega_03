"""
Serviço de tradução do CorreioDigital.
Utiliza o padrão Adapter com fallback para garantir resiliência.
"""

from typing import List, Optional
from .adapter_pattern import ITradutor, TraducaoError
from .models import Mensagem


class ServicoTraducao:
    """
    Cliente (Client) do padrão Adapter.
    
    Gerencia tradução de mensagens usando múltiplos adaptadores com fallback.
    Não conhece detalhes das APIs externas - trabalha apenas com a interface ITradutor.
    """
    
    def __init__(self, adaptadores: List[ITradutor]):
        """
        Args:
            adaptadores: Lista de adaptadores de tradução (ordem define prioridade)
        """
        if not adaptadores:
            raise ValueError("É necessário fornecer pelo menos um adaptador")
        
        self._adaptadores = adaptadores
        self._mensagens_traduzidas: List[Mensagem] = []
    
    def traduzir_mensagem(self, mensagem: Mensagem) -> bool:
        """
        Traduz uma mensagem usando adaptadores com fallback.
        
        Tenta traduzir usando o primeiro adaptador. Se falhar, tenta o próximo.
        Se todos falharem, mantém mensagem original sem tradução.
        
        Args:
            mensagem: Mensagem a ser traduzida
            
        Returns:
            True se tradução foi bem-sucedida, False se todos adaptadores falharam
        """
        if not mensagem.idioma_destino:
            print(f"⚠️  Mensagem sem idioma destino definido - mantendo texto original")
            return False
        
        if mensagem.idioma_origem == mensagem.idioma_destino:
            print(f"ℹ️  Idioma origem igual ao destino - tradução desnecessária")
            mensagem.definir_traducao(mensagem.conteudo)
            return True
        
        for i, adaptador in enumerate(self._adaptadores, 1):
            try:
                print(f"🔄 Tentativa {i}: Usando {adaptador.obter_provedor()}...")
                
                texto_traduzido = adaptador.traduzir(
                    mensagem.conteudo,
                    mensagem.idioma_destino
                )
                
                mensagem.definir_traducao(texto_traduzido)
                self._mensagens_traduzidas.append(mensagem)
                
                print(f"✅ Tradução bem-sucedida com {adaptador.obter_provedor()}")
                return True
                
            except TraducaoError as e:
                print(f"❌ Falha com {adaptador.obter_provedor()}: {e}")
                if i < len(self._adaptadores):
                    print(f"   Tentando próximo adaptador...")
                continue
        
        print(f"⚠️  Todos os adaptadores falharam - mantendo texto original")
        return False
    
    def traduzir_texto(self, texto: str, idioma_destino: str) -> Optional[str]:
        """
        Traduz um texto diretamente (sem criar objeto Mensagem).
        
        Args:
            texto: Texto a ser traduzido
            idioma_destino: Código ISO do idioma destino
            
        Returns:
            Texto traduzido ou None se todos adaptadores falharem
        """
        for adaptador in self._adaptadores:
            try:
                return adaptador.traduzir(texto, idioma_destino)
            except TraducaoError:
                continue
        return None
    
    def obter_estatisticas(self) -> dict:
        """
        Retorna estatísticas do serviço de tradução.
        
        Returns:
            Dict com estatísticas de uso
        """
        return {
            'adaptadores_disponiveis': len(self._adaptadores),
            'provedores': [a.obter_provedor() for a in self._adaptadores],
            'mensagens_traduzidas': len(self._mensagens_traduzidas)
        }
    
    def obter_historico(self) -> List[Mensagem]:
        """Retorna histórico de mensagens traduzidas."""
        return self._mensagens_traduzidas.copy()
    
    def limpar_historico(self) -> None:
        """Limpa o histórico de traduções."""
        self._mensagens_traduzidas.clear()
