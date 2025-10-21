import interfaces.DeliveryService;
import interfaces.Message;

/**
 * Implementação concreta de DeliveryService para SMS
 * Responsável pelo envio de mensagens via SMS
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class SmsDeliveryService implements DeliveryService {
    
    /**
     * Envia uma mensagem por SMS
     * @param recipient Número de telefone do destinatário
     * @param message Mensagem a ser enviada
     * @return boolean indicando se o envio foi bem-sucedido
     */
    @Override
    public boolean send(String recipient, Message message) {
        System.out.println("Enviando SMS para: " + recipient);
        System.out.println("Conteúdo: " + message.render());
        // Aqui seria feita a integração real com o gateway de SMS
        return true;
    }
}
