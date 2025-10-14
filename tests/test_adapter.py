import pytest
import sys
import os

# Garantir que o diretório raiz do repositório esteja no sys.path para imports de testes
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Testes minimalistas para os exemplos de Adapter do documento

class DummyFailAPI:
    def traduzir_texto(self, texto, destino):
        raise RuntimeError("fail")

class DummySuccessAPI:
    def traduzir_texto(self, texto, destino):
        return "sucesso"


def test_google_adapter_success():
    from projeto.chat.services.traducao.adapters import GoogleAdapter, GoogleTranslateAPI  # noqa: E402

    api = GoogleTranslateAPI()
    adapter = GoogleAdapter(api)
    assert adapter.traduzir("x", "EN") == "[Google] x -> EN"


def test_traduz_com_fallback(monkeypatch):
    from projeto.chat.services.traducao.adapters import GoogleAdapter
    from projeto.chat.services.traducao.fallback import traduz_com_fallback

    fail_adapter = GoogleAdapter(DummyFailAPI())
    success_adapter = GoogleAdapter(DummySuccessAPI())

    assert traduz_com_fallback("x", "EN", [fail_adapter, success_adapter]) == "sucesso"
