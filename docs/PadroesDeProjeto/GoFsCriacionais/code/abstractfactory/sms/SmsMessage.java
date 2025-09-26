import interfaces.Message;

/**
 * Implementação concreta de Message para SMS
 * Formata o conteúdo como texto puro para envio por SMS
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class SmsMessage implements Message {
    private String content;
    
    /**
     * Construtor da mensagem de SMS
     * @param content Conteúdo da mensagem
     */
    public SmsMessage(String content) {
        this.content = content;
    }
    
    /**
     * Renderiza a mensagem em formato de texto puro
     * @return String com a mensagem formatada para SMS
     */
    @Override
    public String render() {
        return content; // SMS usa texto puro, sem formatação HTML
    }
}
