from .interfaces import ITradutor, TraducaoError

class GoogleTranslateAPI:
    def traduzir_texto(self, texto: str, destino: str) -> str:
        return f"[Google] {texto} -> {destino}"

class DeepLAPI:
    def translate(self, texto: str, target_lang: str) -> str:
        return f"[DeepL] {texto} -> {target_lang}"

class GoogleAdapter(ITradutor):
    def __init__(self, google_api: GoogleTranslateAPI):
        self.google_api = google_api

    def traduzir(self, texto: str, idioma_destino: str) -> str:
        try:
            return self.google_api.traduzir_texto(texto, destino=idioma_destino)
        except Exception as e:
            raise TraducaoError("Falha na tradução via Google") from e

class DeepLAdapter(ITradutor):
    def __init__(self, deepl_api: DeepLAPI):
        self.deepl_api = deepl_api

    def traduzir(self, texto: str, idioma_destino: str) -> str:
        try:
            return self.deepl_api.translate(texto, target_lang=idioma_destino)
        except Exception as e:
            raise TraducaoError("Falha na tradução via DeepL") from e
