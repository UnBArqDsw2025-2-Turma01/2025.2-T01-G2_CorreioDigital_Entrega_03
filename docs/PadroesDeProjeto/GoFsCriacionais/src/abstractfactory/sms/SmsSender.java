import interfaces.Sender;

/**
 * Implementação concreta de Sender para SMS
 * Fornece o número de telefone de origem para envio de SMS
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public class SmsSender implements Sender {
    
    /**
     * Obtém o número de telefone de origem para SMS
     * @return String com o número de telefone de origem
     */
    @Override
    public String getFromAddress() {
        return "+5561999999999"; // Número do CorreioDigital
    }
}
