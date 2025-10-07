import interfaces.Sender;

/**
 * Implementação concreta de Sender para E-mail
 * Fornece o endereço de origem para envio de e-mails
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class EmailSender implements Sender {
    
    /**
     * Obtém o endereço de origem para e-mails
     * @return String com o endereço de e-mail de origem
     */
    @Override
    public String getFromAddress() {
        return "contato@correiodigital.com";
    }
}
