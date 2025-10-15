/**
 * Interface para o Remetente
 * Define o contrato para obtenção do endereço de origem
 * 
 * @author Esther Sena
 * @author Mariiana Siqueira
 * @version 1.0
 */
public interface Sender {
    /**
     * Obtém o endereço de origem do remetente
     * @return String com o endereço de origem
     */
    String getFromAddress();
}
