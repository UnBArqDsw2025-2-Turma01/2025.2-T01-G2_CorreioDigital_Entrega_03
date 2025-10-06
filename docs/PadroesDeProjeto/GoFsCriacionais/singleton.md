# Padrão Singleton

## Introdução  
Dentro do contexto do **Correio Eletrônico**, o padrão **Singleton** é uma solução criacional para garantir **uma única instância** de componentes transversais ao sistema, fornecendo um **ponto global de acesso** e evitando inconsistências [1](https://refactoring.guru/pt-br/design-patterns/singleton).  

Na nossa aplicação, isso é especialmente útil para:  
- **Logger Central**: registro padronizado de eventos e erros.  
- **Provedor de Configurações**: parâmetros globais de envio e suporte a idiomas.  
- **Cliente de Tradução**: controle centralizado de chamadas e cache de resultados.  

---

## Objetivo / Metodologia
**Objetivo**  
Assegurar **consistência, centralização e rastreabilidade** em recursos críticos do sistema, evitando redundâncias e garantindo confiabilidade.  

**Metodologia**  
1. Identificação dos candidatos a Singleton (Logger, Configurações, Cliente de Tradução).  
2. Definição do ciclo de vida (uma instância por processo).  
3. Implementação em Java com construtor privado, acesso controlado e thread-safe.  
4. Integração nos pacotes do sistema (Interface, Operações, Idiomas e Dados).  

---

## A aplicação do padrão seguiu os seguintes passos  

**Identificação de classes candidatas:**  
Foram analisados os componentes que exigem **acesso global, consistência e baixo acoplamento**, sendo selecionados `Logger`, `AppConfig` e `TranslationClient` como candidatos ideais ao padrão Singleton.  

**Definição do Singleton:**  
Cada classe foi projetada para expor **apenas uma instância única** por meio de método estático (`getInstance()`), garantindo acesso controlado e evitando múltiplas inicializações.  

**Implementação do produto final:**  
A lógica interna de cada classe foi mantida coesa, enquanto a criação da instância foi encapsulada com **classe estática interna**, assegurando inicialização sob demanda e **thread-safety** sem necessidade de sincronização explícita.  

**Integração ao sistema:**  
- O `Logger` é utilizado por todos os subsistemas (Interface, Operações, Idiomas, Dados) para registrar eventos e auditoria.  
- O `AppConfig` centraliza parâmetros de configuração (idioma padrão, tamanho máximo de anexos, políticas de privacidade).  
- O `TranslationClient` controla chamadas de tradução e armazena resultados em cache para otimizar desempenho.  

**Colaboração em equipe:**  
O artefato foi discutido e refinado em conjunto, validando sua aplicabilidade ao projeto. Foram levantados exemplos reais de sistemas de correio eletrônico e plataformas multilíngues, confirmando que o uso do Singleton nesses pontos promove escalabilidade e confiabilidade.  

## Desenvolvimento

### Logger Central (Singleton)
O Logger é usado por todos os subsistemas para registrar eventos.

```java
public final class Logger {
    private Logger() { }

    private static class Holder {
        private static final Logger INSTANCE = new Logger();
    }

    public static Logger getInstance() {
        return Holder.INSTANCE;
    }

    public void info(String msg) {
        System.out.println("[INFO] " + msg);
    }

    public void warn(String msg) {
        System.out.println("[WARN] " + msg);
    }

    public void error(String msg) {
        System.err.println("[ERROR] " + msg);
    }
} 
```

### Exemplo de uso:
```java

public class EnviarEmail {
    public void processarEnvio(String corpo, String idioma) {
        Logger log = Logger.getInstance();
        log.info("Iniciando envio de email em " + idioma);
        // ... lógica de envio ...
        log.info("Email enviado com sucesso!");
    }
}
```

## Justificativa de Uso

- O **Logger Singleton** centraliza auditoria e segurança.  
- O **AppConfig Singleton** garante consistência nos parâmetros globais.  
- O **TranslationClient Singleton** reduz overhead e garante desempenho nas traduções.  

Esses componentes seguem práticas comuns em sistemas reais de e-mail e plataformas multilíngues, alinhando consistência com escalabilidade.  

---

## Bibliografia

- Singleton. Disponível em: <https://refactoring.guru/pt-br/design-patterns/singleton>  
- GAMMA, E. et al. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.  

---

## Histórico de Versões

| Versão | Data       | Descrição                               | Autor(es) | Revisor(es) | Detalhes da revisão |
|-------:|------------|------------------------------------------|-----------|-------------|----------------------|
| `1.0`  | 24/09/2025 | Criação do documento para o padrão Singleton | [Thales Germano](https://github.com/thalesgvl) | - | - |
