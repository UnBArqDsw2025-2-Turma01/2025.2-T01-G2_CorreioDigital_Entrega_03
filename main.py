# main.py

# Como este script está fora da pasta 'src', importamos
# as classes do pacote 'src.correio_digital'
from src.Comportamentais.correio_digital_observer.correio_digital import (
    SistemaDeMensagens,
    NotificadorWeb,
    NotificadorEmail,
    NotificadorMobile
)

if __name__ == "__main__":
    
    print("="*50)
    print("Iniciando Simulação do Correio Digital...")
    print("="*50)

    # 1. Cria o Subject (Sistema de Mensagens)
    sistema_mensagens = SistemaDeMensagens()

    # 2. Cria os Observers (Notificadores)
    obs_web = NotificadorWeb()
    obs_email = NotificadorEmail()
    obs_mobile = NotificadorMobile()

    # 3. Anexa os observadores ao sistema
    sistema_mensagens.attach(obs_web)
    sistema_mensagens.attach(obs_email)
    sistema_mensagens.attach(obs_mobile)

    # 4. Simula o recebimento de uma nova mensagem
    #    Isso deve disparar a notificação para todos os 3 observadores.
    sistema_mensagens.novaMensagem(
        remetente="alice@exemplo.com",
        destinatario="bob@exemplo.com",
        conteudo="Olá Bob, tudo bem? Vamos nos encontrar mais tarde."
    )

    # 5. Desanexa um observador (ex: usuário deslogou do mobile)
    print("\n" + "="*50)
    print("Ação: Usuário Mobile deslogou.")
    sistema_mensagens.detach(obs_mobile)
    
    # 6. Simula o recebimento de outra mensagem
    #    Agora, apenas os observadores Web e Email devem ser notificados.
    sistema_mensagens.novaMensagem(
        remetente="charlie@exemplo.com",
        destinatario="alice@exemplo.com",
        conteudo="Ei Alice, você viu meu e-mail sobre o projeto?"
    )

    print("\n" + "="*50)
    print("Simulação finalizada.")
