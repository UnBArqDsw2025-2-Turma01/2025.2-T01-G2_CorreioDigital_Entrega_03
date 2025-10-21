import interfaces.NotificationFactory;
import client.NotificationService;
import email.EmailNotificationFactory;
import sms.SmsNotificationFactory;

/**
 * Exemplo de uso do padrão Abstract Factory
 * Demonstra como utilizar diferentes fábricas de notificação
 * sem modificar o código cliente
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class Main {
    
    public static void main(String[] args) {
        System.out.println("=== Exemplo do Padrão Abstract Factory ===\n");
        
        // Exemplo 1: Enviar notificação por E-mail
        System.out.println("1. Enviando notificação por E-MAIL:");
        System.out.println("-----------------------------------");
        NotificationFactory emailFactory = new EmailNotificationFactory();
        NotificationService emailService = new NotificationService(emailFactory);
        emailService.sendNotification("usuario@email.com", "Sua fatura chegou!");
        
        System.out.println("\n");
        
        // Exemplo 2: Enviar notificação por SMS
        System.out.println("2. Enviando notificação por SMS:");
        System.out.println("--------------------------------");
        NotificationFactory smsFactory = new SmsNotificationFactory();
        NotificationService smsService = new NotificationService(smsFactory);
        smsService.sendNotification("+5561999999999", "Sua fatura chegou!");
        
        System.out.println("\n");
        
        // Exemplo 3: Demonstração da flexibilidade do padrão
        System.out.println("3. Demonstração da flexibilidade:");
        System.out.println("----------------------------------");
        System.out.println("Para adicionar um novo canal (ex: Push Notification):");
        System.out.println("1. Criar PushMessage, PushSender, PushDeliveryService");
        System.out.println("2. Criar PushNotificationFactory");
        System.out.println("3. Usar: NotificationService pushService = new NotificationService(new PushNotificationFactory());");
        System.out.println("4. Nenhuma modificação no NotificationService é necessária!");
        
        System.out.println("\n=== Benefícios do Padrão Abstract Factory ===");
        System.out.println("✓ Isolamento das classes concretas");
        System.out.println("✓ Consistência entre produtos da mesma família");
        System.out.println("✓ Facilidade para adicionar novos canais");
        System.out.println("✓ Baixo acoplamento e alta coesão");
    }
}
