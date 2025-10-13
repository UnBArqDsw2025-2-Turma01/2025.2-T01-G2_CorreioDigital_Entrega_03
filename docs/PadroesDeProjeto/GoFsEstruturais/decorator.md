# Padrão Decorator no Projeto

## Introdução  

O **Decorator** é um padrão de projeto **estrutural** que tem como objetivo
acrescentar funcionalidades adicionais a um objeto de forma **flexível e
dinâmica**, sem a necessidade de modificar a sua estrutura original.  
Em vez de criar várias subclasses para cada variação de comportamento, o
Decorator permite **combinar responsabilidades** por meio de objetos que
“decoram” a classe base, empilhando funcionalidades conforme a necessidade.

A ideia central é envolver um objeto dentro de outro que implementa a mesma
interface, adicionando comportamento antes ou depois da execução dos métodos
originais. Assim, o objeto decorado mantém sua identidade, mas ganha **novas
capacidades em tempo de execução**.  

Esse padrão é bastante útil em cenários onde o sistema deve permanecer **aberto
para extensão, mas fechado para modificação** (Princípio Aberto/Fechado da
programação orientada a objetos). Ele promove **reuso de código**, evita a
explosão de subclasses e aumenta a **manutenibilidade** da aplicação.

No contexto deste projeto, o Decorator foi aplicado para estender dinamicamente
entidades do domínio, como perfis de usuários (premium, verificado), postagens
(com tags, fixadas), mensagens (com criptografia, confirmação de leitura) e
notificações (urgentes, com som). Essa abordagem garante um sistema mais
modular, escalável e fácil de evoluir.

## Objetivo/Metodologia

O principal objetivo da aplicação do **padrão de projeto Decorator** neste
projeto é fornecer um mecanismo de **extensão flexível** para as classes do
domínio, permitindo adicionar comportamentos ou responsabilidades de forma
dinâmica, sem a necessidade de modificar as implementações originais. Essa
abordagem garante maior modularidade, evita a duplicação de código e mantém
a base do sistema mais clara e fácil de evoluir ao longo do tempo.  

A utilização do Decorator foi orientada por dois fatores principais:  
1. A necessidade de **personalizar funcionalidades** de acordo com cenários
distintos, como usuários comuns que podem se tornar premium ou verificados;  
2. A possibilidade de **empilhar comportamentos** para enriquecer objetos já
existentes, como posts que podem ser fixados, receber tags ou passar por
processos de moderação mais rigorosos.  

A metodologia seguida envolveu a identificação de classes com **potencial de
evolução contínua**, como `Perfil`, `Post`, `Mensagem` e `Notificacao`. Em
vez de criar múltiplas subclasses para cada variação, foram definidos
**decoradores especializados**, cada um responsável por acrescentar uma
função extra, como destaque visual, criptografia, alerta sonoro ou marcação
de status.  

Com isso, é possível **combinar dinamicamente** diferentes decoradores,
adaptando o comportamento do sistema às necessidades do usuário ou às regras
de negócio. Essa abordagem reforça princípios importantes de engenharia de
software, como **baixo acoplamento, alto reuso de código e aderência ao
Princípio Aberto/Fechado (OCP)**.  

No contexto do projeto, o Decorator viabilizou a evolução incremental do
sistema, permitindo que novas funcionalidades sejam incorporadas de forma
não-invasiva, mantendo a arquitetura coesa e a manutenção simplificada.

## Implementação

**Figura 1:** Diagrama UML Decorator  

![Diagrama UML do Decorator](../../Assets/uml_decorator.png)

### Aplicação em código

A seguir, são apresentados os decorators aplicados às principais funcionalidades do sistema, demonstrando como o padrão de projeto Decorator foi utilizado para estender dinamicamente os comportamentos de perfis, postagens, mensagens e notificações sem alterar suas estruturas originais. Os componentes concretos podem ser encontrados [aqui](/docs/PadroesDeProjeto/GoFsCriacionais/factorymethod.md).

**Perfil**

Os decorators aplicados à funcionalidade de perfil permitem adicionar comportamentos complementares, como perfis verificados ou premium.

```java
// DECORATOR BASE PARA PERFIL
abstract class PerfilDecorator extends Perfil {
    protected Perfil perfilDecorado;

    public PerfilDecorator(Perfil perfil) {
        super(perfil.getDisplayName(), perfil.getBio());
        this.perfilDecorado = perfil;
    }

    @Override
    public String toString() {
        return perfilDecorado.toString();
    }
}

// DECORATOR PARA PERFIL PREMIUM (ADICIONA BADGE E BIO PERSONALIZADA)
class PerfilPremiumDecorator extends PerfilDecorator {
    private LocalDateTime dataAssinatura;

    public PerfilPremiumDecorator(Perfil perfil) {
        super(perfil);
        this.dataAssinatura = LocalDateTime.now();
    }

    @Override
    public String toString() {
        return "[PREMIUM ⭐] " + perfilDecorado.getDisplayName() + " - Assinante desde: " + dataAssinatura.toLocalDate();
    }
}

// DECORATOR PARA PERFIL VERIFICADO
class PerfilVerificadoDecorator extends PerfilDecorator {
    public PerfilVerificadoDecorator(Perfil perfil) {
        super(perfil);
    }

    @Override
    public String toString() {
        return perfilDecorado.getDisplayName() + " ✅ (Verificado)";
    }
}
```

**Postagem**

Na funcionalidade de postagem, o uso do padrão Decorator possibilita enriquecer as publicações com novas características, como tags personalizadas ou destaque de posts fixados.

```java
// DECORATOR BASE PARA POST
abstract class PostDecorator extends Post {
    protected Post postDecorado;

    public PostDecorator(Post post) {
        super(post.getId(), post.getAuthor());
        this.postDecorado = post;
    }

    @Override
    public String preview() {
        return postDecorado.preview();
    }

    @Override
    public String getType() {
        return postDecorado.getType();
    }
}

// DECORATOR QUE ADICIONA TAGS A UM POST
class PostComTagsDecorator extends PostDecorator {
    private Set<String> tags = new HashSet<>();

    public PostComTagsDecorator(Post post) {
        super(post);
    }

    public void adicionarTag(String tag) {
        tags.add(tag);
        System.out.println("Tag adicionada ao post " + postDecorado.getId() + ": " + tag);
    }

    @Override
    public String preview() {
        return postDecorado.preview() + " | Tags: " + tags;
    }
}

// DECORATOR QUE MARCA UM POST COMO FIXADO
class PostFixadoDecorator extends PostDecorator {
    public PostFixadoDecorator(Post post) {
        super(post);
    }

    @Override
    public String preview() {
        return "[📌 FIXADO] " + postDecorado.preview();
    }
}

```

**Mensagem**

Para o módulo de mensagens, os decorators ampliam as funcionalidades de envio, permitindo incluir criptografia, confirmações de leitura e outros mecanismos de segurança e rastreabilidade.

```java
// DECORATOR BASE PARA MENSAGEM
abstract class MensagemDecorator extends Mensagem {
    protected Mensagem mensagemDecorada;

    public MensagemDecorator(Mensagem mensagem) {
        super(mensagem.id, mensagem.sender, mensagem.receiver);
        this.mensagemDecorada = mensagem;
    }

    @Override
    public void deliver() {
        mensagemDecorada.deliver();
    }
}

// DECORATOR QUE ADICIONA CRIPTOGRAFIA À MENSAGEM
class MensagemCriptografadaDecorator extends MensagemDecorator {
    public MensagemCriptografadaDecorator(Mensagem mensagem) {
        super(mensagem);
    }

    @Override
    public void deliver() {
        System.out.println("🔐 Mensagem criptografada antes do envio.");
        mensagemDecorada.deliver();
        System.out.println("🔓 Mensagem descriptografada ao chegar no destinatário.");
    }
}

// DECORATOR QUE ADICIONA CONFIRMAÇÃO DE LEITURA
class MensagemComConfirmacaoDecorator extends MensagemDecorator {
    public MensagemComConfirmacaoDecorator(Mensagem mensagem) {
        super(mensagem);
    }

    @Override
    public void deliver() {
        mensagemDecorada.deliver();
        System.out.println("✅ " + mensagemDecorada.receiver.getUsername() + " leu a mensagem.");
    }
}
```

**Notificação**

No contexto de notificações, os decorators são empregados para estender o comportamento padrão, permitindo criar notificações com prioridade, som, ou diferentes formas de alerta.

```java
// DECORATOR BASE PARA NOTIFICAÇÃO
abstract class NotificacaoDecorator extends Notificacao {
    protected Notificacao notificacaoDecorada;

    public NotificacaoDecorator(Notificacao notificacao) {
        super(notificacao.id, notificacao.recipient, notificacao.content);
        this.notificacaoDecorada = notificacao;
    }

    @Override
    public void deliver() {
        notificacaoDecorada.deliver();
    }
}

// DECORATOR PARA NOTIFICAÇÃO URGENTE
class NotificacaoUrgenteDecorator extends NotificacaoDecorator {
    public NotificacaoUrgenteDecorator(Notificacao notificacao) {
        super(notificacao);
    }

    @Override
    public void deliver() {
        System.out.println("🚨 URGENTE 🚨");
        notificacaoDecorada.deliver();
    }
}

// DECORATOR PARA NOTIFICAÇÃO SONORA
class NotificacaoComSomDecorator extends NotificacaoDecorator {
    public NotificacaoComSomDecorator(Notificacao notificacao) {
        super(notificacao);
    }

    @Override
    public void deliver() {
        System.out.println("🔔 Som de notificação reproduzido!");
        notificacaoDecorada.deliver();
    }
}
```

### Exemplo de Uso

Abaixo estão exemplos de uso dos decorators criados, aplicados sobre as classes do projeto

```java
public class ExemploDecorators {
    public static void main(String[] args) {
        // =============================
        // PERFIS DECORADOS
        // =============================
        Perfil joao = new Perfil("João", "Desenvolvedor backend");
        Perfil maria = new Perfil("Maria", "Designer UX/UI");

        // Decorando perfis
        Perfil joaoPremium = new PerfilPremiumDecorator(joao);
        Perfil mariaVerificada = new PerfilVerificadoDecorator(maria);

        System.out.println("Perfis:");
        System.out.println(" - " + joaoPremium);
        System.out.println(" - " + mariaVerificada);
        System.out.println();


        // =============================
        // POSTS DECORADOS
        // =============================
        Post postJoao = new TextoPost("p001", joao, "Dicas de arquitetura limpa em Java!");
        Post postComTags = new PostComTagsDecorator(postJoao);
        ((PostComTagsDecorator) postComTags).adicionarTag("Java");
        ((PostComTagsDecorator) postComTags).adicionarTag("CleanCode");

        Post postFixado = new PostFixadoDecorator(postComTags);

        System.out.println("Posts:");
        System.out.println(" - " + postFixado.preview());
        System.out.println();


        // =============================
        // MENSAGENS DECORADAS
        // =============================
        Mensagem msg = new Mensagem("m001", joao, maria);
        Mensagem msgCriptografada = new MensagemCriptografadaDecorator(msg);
        Mensagem msgCriptoComConfirmacao = new MensagemComConfirmacaoDecorator(msgCriptografada);

        System.out.println("Mensagens:");
        msgCriptoComConfirmacao.deliver();
        System.out.println();


        // =============================
        // NOTIFICAÇÕES DECORADAS
        // =============================
        Notificacao not = new Notificacao("n001", maria, "Você recebeu uma nova mensagem de João!");
        Notificacao notUrgente = new NotificacaoUrgenteDecorator(not);
        Notificacao notComSom = new NotificacaoComSomDecorator(notUrgente);

        System.out.println("Notificações:");
        notComSom.deliver();
    }
}

```

**Saída Esperada**

```
Perfis:
 - [PREMIUM ⭐] João - Assinante desde: 2025-10-06
 - Maria ✅ (Verificado)

Posts:
Tag adicionada ao post p001: Java
Tag adicionada ao post p001: CleanCode
 - [📌 FIXADO] [TextoPost] Dicas de arquitetura limpa em Java! | Tags: [Java, CleanCode]

Mensagens:
🔐 Mensagem criptografada antes do envio.
Mensagem enviada de João para Maria
🔓 Mensagem descriptografada ao chegar no destinatário.
✅ Maria leu a mensagem.

Notificações:
🚨 URGENTE 🚨
🔔 Som de notificação reproduzido!
[Notificação] Para Maria: Você recebeu uma nova mensagem de João!

```

## Vantagens

- Extensibilidade Dinâmica
- Reutilização de código
- Baixo Acoplamento
- Flexibilidade

## Desvantagens

- Complexidade Aumentada
- Sobrecarga de Instâncias
- Dificuldade de Rastreabilidade


## Bibliografia

> GAMMA, E.; HELM, R.; JOHNSON, R.; VLISSIDES, J.  
> **Padrões de Projeto: Soluções Reutilizáveis de Software Orientado a Objetos**.  
> Bookman, Porto Alegre, 2000. (Clássico catálogo GoF onde o padrão Decorator foi descrito).

> Refactoring.Guru.  
> **Decorator**. Disponível em: <https://refactoring.guru/pt-br/design-patterns/decorator>.  
> Acesso em: 13 out. 2025.

> ALUR, D. et al.  
> **Core J2EE Patterns: Best Practices and Design Strategies**.  
> Prentice Hall, 2003. (Referência sobre uso de Decorator em arquiteturas Java corporativas).

## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 11/10/2025  | Criação do esqueleto do documento | [Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
| `1.1`  | 13/10/2025  | Criação da introdução e metodologia | [Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
| `1.2`  | 13/10/2025  | Criação do Diagrama UML Decorator e atualização da introdução e metodologia | [Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
| `1.3`  | 13/10/2025  | Adição da implementação em código dos Decorators | [Pedro Ferreira Gondim](https://github.com/G0ndim) e [Túlio Augusto Celeri](https://github.com/TulioCeleri) |-|-|
