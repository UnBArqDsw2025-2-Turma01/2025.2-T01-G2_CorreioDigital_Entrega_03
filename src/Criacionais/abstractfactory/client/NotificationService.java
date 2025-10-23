import interfaces.NotificationFactory;
import interfaces.Message;
import interfaces.Sender;
import interfaces.DeliveryService;

/**
 * Cliente do padrão Abstract Factory
 * Utiliza a fábrica de notificação para criar e enviar notificações
 * sem conhecer as implementações concretas
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class NotificationService {
    private NotificationFactory factory;
    
    /**
     * Construtor que recebe uma fábrica de notificação via injeção de dependência
     * @param factory Fábrica concreta de notificação (Email ou SMS)
     */
    public NotificationService(NotificationFactory factory) {
        this.factory = factory;
    }
    
    /**
     * Envia uma notificação para um destinatário
     * @param recipient Endereço do destinatário (e-mail ou telefone)
     * @param content Conteúdo da notificação
     */
    public void sendNotification(String recipient, String content) {
        // O cliente usa a fábrica para criar os produtos
        Message message = factory.createMessage(content);
        Sender sender = factory.createSender(); // Poderia ser usado para logging, etc.
        DeliveryService deliveryService = factory.createDeliveryService();
        
        // Log do remetente (opcional)
        System.out.println("Remetente: " + sender.getFromAddress());
        
        // O serviço de envio usa os produtos criados
        boolean success = deliveryService.send(recipient, message);
        
        if (success) {
            System.out.println("Notificação enviada com sucesso!");
        } else {
            System.out.println("Falha ao enviar notificação.");
        }
    }
}
