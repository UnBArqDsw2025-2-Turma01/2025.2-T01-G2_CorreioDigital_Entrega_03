"""
Implementações concretas dos adaptadores para APIs externas de tradução.
Adaptadores (Adapters) que convertem a interface das APIs (Adaptees) para ITradutor (Target).
"""

from .adapter_pattern import ITradutor, TraducaoError


# ============================================
# APIs Externas (Adaptees)
# ============================================

class GoogleTranslateAPI:
    """
    Simula a API externa do Google Translate (Adaptee).
    Na implementação real, seria uma biblioteca ou cliente HTTP.
    """
    
    def traduzir_texto(self, texto: str, destino: str) -> str:
        """
        Método específico da API do Google Translate.
        Assinatura diferente do que nosso sistema espera.
        """
        # Simulação - na prática faria requisição HTTP
        if not texto:
            raise ValueError("Texto vazio")
        return f"[Google Translate] {texto} traduzido para {destino}"
    
    def obter_idiomas_suportados(self) -> list:
        """Método adicional específico do Google."""
        return ['EN', 'PT', 'ES', 'FR', 'DE', 'IT', 'JA', 'ZH']


class DeepLAPI:
    """
    Simula a API externa do DeepL (Adaptee).
    Interface completamente diferente do Google e do nosso sistema.
    """
    
    def translate(self, text: str, target_lang: str, source_lang: str = 'auto') -> dict:
        """
        Método da API DeepL - retorna dict com metadados.
        Assinatura e retorno diferentes do esperado pelo sistema.
        """
        if not text:
            raise ValueError("Empty text")
        
        # Simulação - DeepL retorna um objeto complexo
        return {
            'translations': [{
                'detected_source_language': source_lang,
                'text': f"[DeepL] {text} translated to {target_lang}"
            }],
            'metadata': {
                'provider': 'deepl',
                'confidence': 0.95
            }
        }
    
    def get_usage_stats(self) -> dict:
        """Método específico do DeepL para verificar quota."""
        return {'character_count': 1000, 'character_limit': 500000}


# ============================================
# Adaptadores (Adapters)
# ============================================

class GoogleAdapter(ITradutor):
    """
    Adapter para Google Translate API.
    Converte a interface do Google (traduzir_texto) para o padrão ITradutor (traduzir).
    """
    
    def __init__(self, google_api: GoogleTranslateAPI):
        """
        Args:
            google_api: Instância da API do Google Translate
        """
        self._google_api = google_api
    
    def traduzir(self, texto: str, idioma_destino: str) -> str:
        """
        Implementa a interface ITradutor adaptando chamadas para Google API.
        
        Args:
            texto: Texto a ser traduzido
            idioma_destino: Código ISO do idioma destino
            
        Returns:
            Texto traduzido
            
        Raises:
            TraducaoError: Quando a tradução falhar
        """
        if not self.validar_idioma(idioma_destino):
            raise TraducaoError(f"Idioma {idioma_destino} não suportado")
        
        try:
            # Adapta a chamada: nosso método -> método do Google
            resultado = self._google_api.traduzir_texto(texto, destino=idioma_destino)
            return resultado
        except Exception as e:
            raise TraducaoError(f"Falha na tradução via Google: {str(e)}") from e
    
    def obter_provedor(self) -> str:
        """Retorna o nome do provedor."""
        return "Google Translate"


class DeepLAdapter(ITradutor):
    """
    Adapter para DeepL API.
    Converte a interface complexa do DeepL (translate com dict) para o padrão ITradutor.
    """
    
    def __init__(self, deepl_api: DeepLAPI):
        """
        Args:
            deepl_api: Instância da API do DeepL
        """
        self._deepl_api = deepl_api
    
    def traduzir(self, texto: str, idioma_destino: str) -> str:
        """
        Implementa a interface ITradutor adaptando chamadas para DeepL API.
        
        A API DeepL retorna um dict complexo - este adapter extrai apenas o texto traduzido.
        
        Args:
            texto: Texto a ser traduzido
            idioma_destino: Código ISO do idioma destino
            
        Returns:
            Texto traduzido (extraído do dict da resposta)
            
        Raises:
            TraducaoError: Quando a tradução falhar
        """
        if not self.validar_idioma(idioma_destino):
            raise TraducaoError(f"Idioma {idioma_destino} não suportado")
        
        try:
            # Adapta a chamada: nosso método -> método do DeepL
            resultado = self._deepl_api.translate(texto, target_lang=idioma_destino)
            
            # Extrai o texto traduzido do dict complexo
            return resultado['translations'][0]['text']
        except Exception as e:
            raise TraducaoError(f"Falha na tradução via DeepL: {str(e)}") from e
    
    def obter_provedor(self) -> str:
        """Retorna o nome do provedor."""
        return "DeepL"
    
    def verificar_quota(self) -> dict:
        """Método adicional que expõe funcionalidade específica do DeepL."""
        try:
            return self._deepl_api.get_usage_stats()
        except Exception:
            return {'error': 'Não foi possível verificar quota'}
