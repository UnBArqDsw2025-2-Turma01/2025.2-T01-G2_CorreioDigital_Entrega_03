"""
Testes para o padrão Adapter no CorreioDigital.
Valida adaptadores, serviço de tradução e mecanismo de fallback.
"""

import pytest
import unittest
from src.Estruturais.correio_digital_adapter.correio_digital import (
    Mensagem,
    ITradutor,
    TraducaoError,
    GoogleTranslateAPI,
    DeepLAPI,
    GoogleAdapter,
    DeepLAdapter,
    ServicoTraducao
)


class TestAdaptadores(unittest.TestCase):
    """Testes para os adaptadores de tradução."""
    
    def setUp(self):
        """Configura adaptadores antes de cada teste."""
        self.google_api = GoogleTranslateAPI()
        self.deepl_api = DeepLAPI()
        self.google_adapter = GoogleAdapter(self.google_api)
        self.deepl_adapter = DeepLAdapter(self.deepl_api)
    
    def test_google_adapter_traduz_com_sucesso(self):
        """Testa se GoogleAdapter traduz corretamente."""
        resultado = self.google_adapter.traduzir("Olá", "EN")
        self.assertIn("Google Translate", resultado)
        self.assertIn("Olá", resultado)
        self.assertIn("EN", resultado)
    
    def test_deepl_adapter_traduz_com_sucesso(self):
        """Testa se DeepLAdapter traduz corretamente."""
        resultado = self.deepl_adapter.traduzir("Hello", "PT")
        self.assertIn("DeepL", resultado)
        self.assertIn("Hello", resultado)
        self.assertIn("PT", resultado)
    
    def test_google_adapter_idioma_invalido(self):
        """Testa se GoogleAdapter rejeita idioma inválido."""
        with self.assertRaises(TraducaoError):
            self.google_adapter.traduzir("Texto", "XX")
    
    def test_deepl_adapter_idioma_invalido(self):
        """Testa se DeepLAdapter rejeita idioma inválido."""
        with self.assertRaises(TraducaoError):
            self.deepl_adapter.traduzir("Texto", "YY")
    
    def test_adaptadores_implementam_interface(self):
        """Verifica se adaptadores implementam ITradutor."""
        self.assertIsInstance(self.google_adapter, ITradutor)
        self.assertIsInstance(self.deepl_adapter, ITradutor)
    
    def test_google_adapter_obter_provedor(self):
        """Testa método obter_provedor do GoogleAdapter."""
        self.assertEqual(self.google_adapter.obter_provedor(), "Google Translate")
    
    def test_deepl_adapter_obter_provedor(self):
        """Testa método obter_provedor do DeepLAdapter."""
        self.assertEqual(self.deepl_adapter.obter_provedor(), "DeepL")
    
    def test_deepl_adapter_verificar_quota(self):
        """Testa funcionalidade específica do DeepL."""
        quota = self.deepl_adapter.verificar_quota()
        self.assertIn('character_count', quota)


class TestServicoTraducao(unittest.TestCase):
    """Testes para o serviço de tradução com fallback."""
    
    def setUp(self):
        """Configura serviço antes de cada teste."""
        google_api = GoogleTranslateAPI()
        deepl_api = DeepLAPI()
        self.google_adapter = GoogleAdapter(google_api)
        self.deepl_adapter = DeepLAdapter(deepl_api)
        self.servico = ServicoTraducao([self.google_adapter, self.deepl_adapter])
    
    def test_servico_inicializa_com_adaptadores(self):
        """Testa se serviço inicializa corretamente."""
        stats = self.servico.obter_estatisticas()
        self.assertEqual(stats['adaptadores_disponiveis'], 2)
        self.assertEqual(len(stats['provedores']), 2)
    
    def test_servico_requer_adaptador(self):
        """Testa se serviço rejeita inicialização sem adaptadores."""
        with self.assertRaises(ValueError):
            ServicoTraducao([])
    
    def test_traduz_mensagem_com_sucesso(self):
        """Testa tradução de mensagem."""
        mensagem = Mensagem(
            conteudo="Olá",
            idioma_origem="PT",
            idioma_destino="EN",
            remetente="user1",
            destinatario="user2"
        )
        
        sucesso = self.servico.traduzir_mensagem(mensagem)
        self.assertTrue(sucesso)
        self.assertIsNotNone(mensagem.traducao)
        self.assertIn("Google", mensagem.traducao)
    
    def test_traduz_mensagem_idiomas_iguais(self):
        """Testa comportamento quando idioma origem = destino."""
        mensagem = Mensagem(
            conteudo="Hello",
            idioma_origem="EN",
            idioma_destino="EN",
            remetente="user1",
            destinatario="user2"
        )
        
        sucesso = self.servico.traduzir_mensagem(mensagem)
        self.assertTrue(sucesso)
        self.assertEqual(mensagem.traducao, mensagem.conteudo)
    
    def test_traduz_mensagem_sem_idioma_destino(self):
        """Testa comportamento sem idioma destino."""
        mensagem = Mensagem(
            conteudo="Olá",
            idioma_origem="PT",
            remetente="user1",
            destinatario="user2"
        )
        
        sucesso = self.servico.traduzir_mensagem(mensagem)
        self.assertFalse(sucesso)
        self.assertIsNone(mensagem.traducao)
    
    def test_traduz_texto_direto(self):
        """Testa tradução direta de texto."""
        resultado = self.servico.traduzir_texto("Bom dia", "EN")
        self.assertIsNotNone(resultado)
        self.assertIn("Bom dia", resultado)
    
    def test_historico_mensagens(self):
        """Testa histórico de mensagens traduzidas."""
        mensagem1 = Mensagem("Olá", "PT", "user1", "user2", "EN")
        mensagem2 = Mensagem("Hello", "EN", "user3", "user4", "PT")
        
        self.servico.traduzir_mensagem(mensagem1)
        self.servico.traduzir_mensagem(mensagem2)
        
        historico = self.servico.obter_historico()
        self.assertEqual(len(historico), 2)
    
    def test_limpar_historico(self):
        """Testa limpeza do histórico."""
        mensagem = Mensagem("Teste", "PT", "user1", "user2", "EN")
        self.servico.traduzir_mensagem(mensagem)
        
        self.servico.limpar_historico()
        
        historico = self.servico.obter_historico()
        self.assertEqual(len(historico), 0)


class TestFallback(unittest.TestCase):
    """Testes para mecanismo de fallback."""
    
    def test_fallback_usa_segundo_adaptador_quando_primeiro_falha(self):
        """Testa se fallback funciona quando primeiro adaptador falha."""
        
        # Criar adaptador que falha
        class APIQueFalha:
            def traduzir_texto(self, texto, destino):
                raise RuntimeError("Falha simulada")
        
        adapter_falho = GoogleAdapter(APIQueFalha())
        adapter_sucesso = GoogleAdapter(GoogleTranslateAPI())
        
        servico = ServicoTraducao([adapter_falho, adapter_sucesso])
        
        resultado = servico.traduzir_texto("Teste", "EN")
        self.assertIsNotNone(resultado)
        self.assertIn("Google", resultado)
    
    def test_fallback_retorna_none_quando_todos_falham(self):
        """Testa comportamento quando todos adaptadores falham."""
        
        class APIQueFalha:
            def traduzir_texto(self, texto, destino):
                raise RuntimeError("Falha")
        
        adapter1 = GoogleAdapter(APIQueFalha())
        
        class APIQueFalha2:
            def translate(self, text, target_lang, source_lang='auto'):
                raise RuntimeError("Falha")
        
        adapter2 = DeepLAdapter(APIQueFalha2())
        
        servico = ServicoTraducao([adapter1, adapter2])
        
        resultado = servico.traduzir_texto("Teste", "EN")
        self.assertIsNone(resultado)


class TestModelos(unittest.TestCase):
    """Testes para o modelo Mensagem."""
    
    def test_mensagem_cria_timestamp_automatico(self):
        """Testa se Mensagem cria timestamp automaticamente."""
        mensagem = Mensagem("Olá", "PT", "user1", "user2")
        self.assertIsNotNone(mensagem.timestamp)
    
    def test_mensagem_define_traducao(self):
        """Testa método definir_traducao."""
        mensagem = Mensagem("Olá", "PT", "user1", "user2")
        mensagem.definir_traducao("Hello")
        self.assertEqual(mensagem.traducao, "Hello")
    
    def test_mensagem_obter_texto_exibicao_com_traducao(self):
        """Testa obter_texto_exibicao quando há tradução."""
        mensagem = Mensagem("Olá", "PT", "user1", "user2")
        mensagem.definir_traducao("Hello")
        self.assertEqual(mensagem.obter_texto_exibicao(), "Hello")
    
    def test_mensagem_obter_texto_exibicao_sem_traducao(self):
        """Testa obter_texto_exibicao quando não há tradução."""
        mensagem = Mensagem("Olá", "PT", "user1", "user2")
        self.assertEqual(mensagem.obter_texto_exibicao(), "Olá")


if __name__ == '__main__':
    unittest.main()
