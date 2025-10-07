import interfaces.NotificationFactory;
import interfaces.Message;
import interfaces.Sender;
import interfaces.DeliveryService;

/**
 * Fábrica concreta para criação de objetos de notificação por SMS
 * Implementa o padrão Abstract Factory para a família de produtos de SMS
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class SmsNotificationFactory implements NotificationFactory {
    
    /**
     * Cria uma mensagem de SMS com o conteúdo especificado
     * @param content Conteúdo da mensagem
     * @return Message instância de SmsMessage
     */
    @Override
    public Message createMessage(String content) {
        return new SmsMessage(content);
    }
    
    /**
     * Cria um remetente de SMS
     * @return Sender instância de SmsSender
     */
    @Override
    public Sender createSender() {
        return new SmsSender();
    }
    
    /**
     * Cria um serviço de envio de SMS
     * @return DeliveryService instância de SmsDeliveryService
     */
    @Override
    public DeliveryService createDeliveryService() {
        return new SmsDeliveryService();
    }
}
