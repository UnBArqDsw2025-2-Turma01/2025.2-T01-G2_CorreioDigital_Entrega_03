# Pacote para módulos de tradução do CorreioDigital
from .interfaces import ITradutor, TraducaoError
from .adapters import GoogleAdapter, DeepLAdapter, GoogleTranslateAPI, DeepLAPI
from .fallback import traduz_com_fallback
