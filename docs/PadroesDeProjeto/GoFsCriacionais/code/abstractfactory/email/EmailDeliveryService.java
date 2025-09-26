import interfaces.DeliveryService;
import interfaces.Message;

/**
 * Implementação concreta de DeliveryService para E-mail
 * Responsável pelo envio de mensagens via e-mail
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class EmailDeliveryService implements DeliveryService {
    
    /**
     * Envia uma mensagem por e-mail
     * @param recipient Endereço de e-mail do destinatário
     * @param message Mensagem a ser enviada
     * @return boolean indicando se o envio foi bem-sucedido
     */
    @Override
    public boolean send(String recipient, Message message) {
        System.out.println("Enviando E-MAIL para: " + recipient);
        System.out.println("Conteúdo: " + message.render());
        // Aqui seria feita a integração real com o serviço de e-mail
        return true;
    }
}
