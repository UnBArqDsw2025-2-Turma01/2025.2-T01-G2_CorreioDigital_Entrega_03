/**
 * Interface para a Fábrica de Notificação (AbstractFactory)
 * Define o contrato para criação de famílias de objetos de notificação
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public interface NotificationFactory {
    /**
     * Cria uma mensagem com o conteúdo especificado
     * @param content Conteúdo da mensagem
     * @return Message instância da mensagem
     */
    Message createMessage(String content);
    
    /**
     * Cria um remetente para o canal de notificação
     * @return Sender instância do remetente
     */
    Sender createSender();
    
    /**
     * Cria um serviço de envio para o canal de notificação
     * @return DeliveryService instância do serviço de envio
     */
    DeliveryService createDeliveryService();
}
