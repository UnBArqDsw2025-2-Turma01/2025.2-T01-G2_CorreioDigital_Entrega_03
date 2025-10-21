import interfaces.Message;

/**
 * Implementação concreta de Message para E-mail
 * Formata o conteúdo como HTML para envio por e-mail
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class EmailMessage implements Message {
    private String content;
    
    /**
     * Construtor da mensagem de e-mail
     * @param content Conteúdo da mensagem
     */
    public EmailMessage(String content) {
        this.content = content;
    }
    
    /**
     * Renderiza a mensagem em formato HTML
     * @return String com a mensagem formatada em HTML
     */
    @Override
    public String render() {
        return "<html><body>" + content + "</body></html>";
    }
}
