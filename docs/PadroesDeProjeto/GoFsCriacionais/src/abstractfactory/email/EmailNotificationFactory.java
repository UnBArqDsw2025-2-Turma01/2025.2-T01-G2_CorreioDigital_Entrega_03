import interfaces.NotificationFactory;
import interfaces.Message;
import interfaces.Sender;
import interfaces.DeliveryService;

/**
 * Fábrica concreta para criação de objetos de notificação por E-mail
 * Implementa o padrão Abstract Factory para a família de produtos de e-mail
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class EmailNotificationFactory implements NotificationFactory {
    
    /**
     * Cria uma mensagem de e-mail com o conteúdo especificado
     * @param content Conteúdo da mensagem
     * @return Message instância de EmailMessage
     */
    @Override
    public Message createMessage(String content) {
        return new EmailMessage(content);
    }
    
    /**
     * Cria um remetente de e-mail
     * @return Sender instância de EmailSender
     */
    @Override
    public Sender createSender() {
        return new EmailSender();
    }
    
    /**
     * Cria um serviço de envio de e-mail
     * @return DeliveryService instância de EmailDeliveryService
     */
    @Override
    public DeliveryService createDeliveryService() {
        return new EmailDeliveryService();
    }
}
