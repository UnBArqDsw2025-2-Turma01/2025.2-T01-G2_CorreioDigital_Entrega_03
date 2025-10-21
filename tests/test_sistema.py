# tests/test_sistema.py

import unittest
import io
from contextlib import redirect_stdout

# Os testes estão fora de 'src', então importamos de 'src.correio_digital'
from src.Comportamentais.correio_digital_observer.correio_digital import (
    SistemaDeMensagens, 
    NotificadorWeb, 
    NotificadorEmail, 
    NotificadorMobile
)

class TestObserverPatternCorreioDigital(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente de teste antes de cada método de teste.
        """
        self.sistema = SistemaDeMensagens()
        self.obs_web = NotificadorWeb()
        self.obs_email = NotificadorEmail()
        self.obs_mobile = NotificadorMobile()

    def test_attach_and_notify_all_observers(self):
        """
        Testa se todos os observadores anexados são notificados.
        """
        self.sistema.attach(self.obs_web)
        self.sistema.attach(self.obs_email)
        self.sistema.attach(self.obs_mobile)

        # Usamos redirect_stdout para capturar as saídas do 'print'
        with io.StringIO() as buf, redirect_stdout(buf):
            self.sistema.novaMensagem("remetente1", "dest1", "Olá mundo")
            output = buf.getvalue()

        # Verifica se a saída capturada contém as strings de cada notificador
        self.assertIn("[WEB] Notificação Push", output)
        self.assertIn("[EMAIL] Enviando e-mail", output)
        self.assertIn("[MOBILE] Notificação (Pling!)", output)
        self.assertIn("Notificando 3 observadores", output)

    def test_detach_observer(self):
        """
        Testa se um observador desanexado não recebe mais notificações.
        """
        self.sistema.attach(self.obs_web)
        self.sistema.attach(self.obs_email)
        self.sistema.attach(self.obs_mobile)

        # Desanexa o de e-mail
        self.sistema.detach(self.obs_email)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.sistema.novaMensagem("remetente2", "dest2", "Teste sem email")
            output = buf.getvalue()

        # Verifica se WEB e MOBILE receberam, mas EMAIL não
        self.assertIn("[WEB] Notificação Push", output)
        self.assertIn("[MOBILE] Notificação (Pling!)", output)
        self.assertNotIn("[EMAIL] Enviando e-mail", output) # <-- A asserção principal
        self.assertIn("Notificando 2 observadores", output)

    def test_notify_with_no_observers(self):
        """
        Testa se o sistema não quebra ao notificar sem observadores.
        """
        with io.StringIO() as buf, redirect_stdout(buf):
            self.sistema.novaMensagem("remetente3", "dest3", "Ninguém ouvindo")
            output = buf.getvalue()

            # O sistema deve notificar 0 observadores sem quebrar
            self.assertIn("Notificando 0 observadores", output)
        self.assertNotIn("[WEB]", output)
        self.assertNotIn("[EMAIL]", output)
        self.assertNotIn("[MOBILE]", output)

    def test_detach_non_existent_observer(self):
        """
        Testa a tentativa de desanexar um observador que não está na lista.
        """
        self.sistema.attach(self.obs_web)
        
        # Tenta desanexar o 'obs_email' que nunca foi anexado
        with io.StringIO() as buf, redirect_stdout(buf):
            self.sistema.detach(self.obs_email)
            output = buf.getvalue()
        
        # O sistema deve imprimir uma mensagem de aviso
        self.assertIn(f"{self.obs_email.__class__.__name__} não está na lista", output)

if __name__ == "__main__":
    unittest.main()
