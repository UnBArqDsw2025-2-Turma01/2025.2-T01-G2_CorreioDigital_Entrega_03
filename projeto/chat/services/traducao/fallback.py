from .interfaces import ITradutor, TraducaoError


def traduz_com_fallback(texto: str, idioma: str, adaptadores: list[ITradutor]) -> str:
    for adaptador in adaptadores:
        try:
            return adaptador.traduzir(texto, idioma)
        except TraducaoError:
            continue
    return texto
