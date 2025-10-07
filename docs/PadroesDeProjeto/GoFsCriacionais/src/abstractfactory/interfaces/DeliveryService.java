/**
 * Interface para o Serviço de Envio
 * Define o contrato para envio de mensagens
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public interface DeliveryService {
    /**
     * Envia uma mensagem para um destinatário
     * @param recipient String com o endereço do destinatário
     * @param message Mensagem a ser enviada
     * @return boolean indicando se o envio foi bem-sucedido
     */
    boolean send(String recipient, Message message);
}
