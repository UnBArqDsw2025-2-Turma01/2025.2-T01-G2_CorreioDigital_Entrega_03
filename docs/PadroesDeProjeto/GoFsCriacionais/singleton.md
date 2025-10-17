# Padrão Singleton

## Introdução  
Dentro do contexto do **Correio Eletrônico**, o padrão **Singleton** é uma solução criacional para garantir **uma única instância** de componentes transversais ao sistema, fornecendo um **ponto global de acesso** e evitando inconsistências [1](https://refactoring.guru/pt-br/design-patterns/singleton).  

Na nossa aplicação, isso é especialmente útil para:  
- **Logger Central**: registro padronizado de eventos e erros.  
- **Provedor de Configurações**: parâmetros globais de envio e suporte a idiomas.  
- **Cliente de Tradução**: controle centralizado de chamadas e cache de resultados.  

---

## Objetivo

O principal objetivo da aplicação do padrão **Singleton** no sistema de **Correio Eletrônico Multilíngue** é garantir que componentes críticos — aqueles que precisam manter **um estado global único e consistente** — sejam acessados de forma centralizada por toda a aplicação.  

Ao fazer isso, buscamos alcançar três metas fundamentais:

- **Consistência global:** assegurar que diferentes módulos do sistema compartilhem as mesmas configurações, políticas e serviços centrais, evitando comportamentos conflitantes e reduzindo falhas.  
- **Centralização de recursos:** concentrar funcionalidades essenciais (como logging, tradução e parâmetros globais) em instâncias únicas, simplificando o acesso e reduzindo o acoplamento entre módulos.  
- **Rastreabilidade e controle:** fornecer um ponto único para monitoramento, auditoria e ajuste de parâmetros, facilitando a manutenção, depuração e evolução do sistema ao longo do tempo.  

Em termos práticos, isso significa que qualquer parte do sistema — seja a interface de usuário, os módulos de tradução ou os serviços de entrega de mensagens — acessará as mesmas instâncias de componentes como `Logger`, `AppConfig` e `TranslationClient`. Assim, decisões e estados importantes são aplicados **de forma uniforme em todo o ecossistema**, aumentando a confiabilidade e a previsibilidade da aplicação.
 

## Metodologia

O processo de aplicação do padrão **Singleton** no projeto do **Correio Eletrônico** foi conduzido de forma estruturada e iterativa, partindo do entendimento teórico até a implementação prática e integração ao sistema. As etapas foram as seguintes:

### 1. Estudo teórico e contextualização  
Antes de iniciar a implementação, foi realizado um estudo aprofundado sobre o padrão Singleton por meio de aulas, materiais teóricos e documentação especializada, como o livro *Design Patterns* (Gamma et al., 1994) e recursos do [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/singleton).  
Essa etapa permitiu compreender o conceito central do padrão: **garantir uma única instância global de uma classe durante todo o ciclo de vida da aplicação**, fornecendo um ponto de acesso centralizado e evitando estados conflitantes.

---

### 2. Identificação dos candidatos ideais  
A partir da análise da arquitetura do sistema, foram mapeados os componentes que **precisam ser únicos e globais**, ou seja, aqueles cujo estado compartilhado deve ser acessado de forma consistente por diferentes módulos:  

- **Logger** – responsável por registrar logs de eventos, erros e auditorias.  
- **AppConfig** – gerenciador de configurações globais do sistema, como idioma padrão, tamanho máximo de anexos e políticas de privacidade.  
- **TranslationClient** – cliente central para tradução automática e cache de resultados, evitando chamadas redundantes.

A escolha desses elementos se baseou no fato de que múltiplas instâncias poderiam gerar comportamentos inconsistentes, duplicação de recursos ou falhas de segurança.

---

### 3. Definição do ciclo de vida da instância  
Foi definido que cada classe Singleton deve possuir **apenas uma instância por processo de execução da aplicação**.  
Essa decisão garante que:  
- O estado global seja **compartilhado entre todos os componentes** que acessam a instância.  
- Alterações em configurações ou dados de cache tenham **efeito imediato em todo o sistema**.  
- Recursos sensíveis, como logs e conexões de tradução, sejam gerenciados de forma centralizada.

---

### 4. Planejamento da implementação  
Antes da codificação, foram estabelecidos os princípios fundamentais a serem seguidos na implementação do Singleton:

- **Construtor privado:** impedir a criação direta de instâncias fora da classe.  
- **Método de acesso estático (`getInstance()`):** responsável por retornar a instância única.  
- **Thread-safe:** garantir que, mesmo em ambientes concorrentes, apenas uma instância seja criada.  
- **Lazy Initialization (Holder Pattern):** adiar a criação da instância até o primeiro uso, melhorando desempenho e reduzindo consumo de memória.

---

### 5. Implementação em Java  
Com os requisitos definidos, iniciou-se a implementação prática em Java.  
Cada candidato foi estruturado como uma classe Singleton seguindo o padrão `Lazy Holder`, garantindo inicialização sob demanda e segurança em ambientes multithread.  
Exemplo de aplicação prática:
- `Logger` registra eventos em todos os módulos.  
- `AppConfig` mantém consistência nas configurações globais.  
- `TranslationClient` armazena traduções recentes em cache e reduz o consumo de API.

---

### 6. Integração ao sistema  
Após a implementação, os Singletons foram integrados aos principais **pacotes do sistema**:

- **Interface:** fornece feedback e notificações baseadas em logs e configurações.  
- **Operações:** usa o `Logger` para rastrear envios e recebimentos de e-mails.  
- **Idiomas:** utiliza `TranslationClient` para traduções automáticas em tempo real.  
- **Dados:** aplica configurações globais e políticas de retenção de mensagens do `AppConfig`.

Essa integração garantiu que todos os módulos compartilhassem as mesmas configurações e serviços centrais, eliminando comportamentos divergentes e aumentando a confiabilidade do sistema.

---

### 7. Testes e validação  
Por fim, foram realizados testes unitários e de integração para confirmar que:  
- Apenas uma instância de cada Singleton é criada durante a execução.  
- A instância é reutilizada por diferentes componentes sem perda de estado.  
- As operações permanecem consistentes em cenários concorrentes.  

Com os testes concluídos, a implementação foi considerada estável e alinhada às melhores práticas do padrão Singleton.

---

### Resultado Final  
A aplicação do padrão **Singleton** no projeto resultou em um sistema mais **consistente, seguro e fácil de manter**.  
A centralização de logs, configurações e traduções eliminou redundâncias e melhorou a eficiência global, além de facilitar a evolução futura do projeto sem comprometer a integridade dos componentes principais.

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
| `1.0`  | 24/09/2025 | Criação do documento para o padrão Singleton | [Thales Germano](https://github.com/thalesgvl) e [Eric Akio](https://github.com/eric-kingu) | - | - |
| `1.1`  | 15/09/2025 | Ajustando metodologia e bibliografia para Singleton | [Thales Germano](https://github.com/thalesgvl) | - | - |