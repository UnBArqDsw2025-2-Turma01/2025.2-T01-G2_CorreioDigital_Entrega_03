"""
Demonstração do padrão Adapter no CorreioDigital.
Exemplo de uso do sistema de tradução com múltiplos provedores e fallback.
"""

from src.Estruturais.correio_digital_adapter.correio_digital import (
    Mensagem,
    GoogleTranslateAPI,
    DeepLAPI,
    GoogleAdapter,
    DeepLAdapter,
    ServicoTraducao
)


def main():
    print("=" * 70)
    print("CORREIO DIGITAL - DEMONSTRAÇÃO DO PADRÃO ADAPTER")
    print("Sistema de Tradução de Mensagens com Fallback")
    print("=" * 70)
    print()
    
    # ============================================
    # 1. Configurar APIs Externas (Adaptees)
    # ============================================
    print("📦 Inicializando APIs externas...")
    google_api = GoogleTranslateAPI()
    deepl_api = DeepLAPI()
    print("   ✓ Google Translate API")
    print("   ✓ DeepL API")
    print()
    
    # ============================================
    # 2. Criar Adaptadores
    # ============================================
    print("🔌 Criando adaptadores...")
    google_adapter = GoogleAdapter(google_api)
    deepl_adapter = DeepLAdapter(deepl_api)
    print(f"   ✓ {google_adapter.obter_provedor()}")
    print(f"   ✓ {deepl_adapter.obter_provedor()}")
    print()
    
    # ============================================
    # 3. Configurar Serviço com Fallback
    # ============================================
    print("⚙️  Configurando serviço de tradução (prioridade: Google → DeepL)...")
    servico = ServicoTraducao([google_adapter, deepl_adapter])
    print(f"   Adaptadores configurados: {servico.obter_estatisticas()['adaptadores_disponiveis']}")
    print()
    
    # ============================================
    # 4. Cenário 1: Tradução Bem-Sucedida
    # ============================================
    print("-" * 70)
    print("CENÁRIO 1: Tradução bem-sucedida")
    print("-" * 70)
    
    mensagem1 = Mensagem(
        conteudo="Olá, como você está?",
        idioma_origem="PT",
        idioma_destino="EN",
        remetente="usuario@correio.com",
        destinatario="friend@correio.com"
    )
    
    print(f"📨 Mensagem original: '{mensagem1.conteudo}' ({mensagem1.idioma_origem})")
    print(f"🎯 Idioma destino: {mensagem1.idioma_destino}")
    print()
    
    sucesso = servico.traduzir_mensagem(mensagem1)
    
    if sucesso:
        print()
        print(f"📬 Mensagem traduzida: '{mensagem1.obter_texto_exibicao()}'")
    print()
    
    # ============================================
    # 5. Cenário 2: Tradução com Idiomas Iguais
    # ============================================
    print("-" * 70)
    print("CENÁRIO 2: Idioma origem = idioma destino (sem tradução necessária)")
    print("-" * 70)
    
    mensagem2 = Mensagem(
        conteudo="Hello, how are you?",
        idioma_origem="EN",
        idioma_destino="EN",
        remetente="user@correio.com",
        destinatario="another@correio.com"
    )
    
    print(f"📨 Mensagem: '{mensagem2.conteudo}' ({mensagem2.idioma_origem} → {mensagem2.idioma_destino})")
    print()
    
    servico.traduzir_mensagem(mensagem2)
    print()
    
    # ============================================
    # 6. Cenário 3: Tradução Direta (sem Mensagem)
    # ============================================
    print("-" * 70)
    print("CENÁRIO 3: Tradução direta de texto")
    print("-" * 70)
    
    texto_original = "Bom dia!"
    print(f"📝 Texto: '{texto_original}'")
    print(f"🎯 Traduzir para: ES")
    print()
    
    traducao = servico.traduzir_texto(texto_original, "ES")
    if traducao:
        print(f"✅ Resultado: '{traducao}'")
    print()
    
    # ============================================
    # 7. Cenário 4: Verificar Quota do DeepL
    # ============================================
    print("-" * 70)
    print("CENÁRIO 4: Funcionalidade específica do DeepL (verificar quota)")
    print("-" * 70)
    
    quota = deepl_adapter.verificar_quota()
    print(f"📊 Quota DeepL: {quota}")
    print()
    
    # ============================================
    # 8. Estatísticas Finais
    # ============================================
    print("-" * 70)
    print("ESTATÍSTICAS FINAIS")
    print("-" * 70)
    
    stats = servico.obter_estatisticas()
    print(f"📈 Mensagens traduzidas: {stats['mensagens_traduzidas']}")
    print(f"🔌 Provedores disponíveis: {', '.join(stats['provedores'])}")
    print()
    
    print("📜 Histórico de mensagens traduzidas:")
    for i, msg in enumerate(servico.obter_historico(), 1):
        print(f"   {i}. {msg.idioma_origem} → {msg.idioma_destino}: '{msg.conteudo}' → '{msg.traducao}'")
    print()
    
    print("=" * 70)
    print("✅ DEMONSTRAÇÃO CONCLUÍDA")
    print("=" * 70)


if __name__ == "__main__":
    main()
