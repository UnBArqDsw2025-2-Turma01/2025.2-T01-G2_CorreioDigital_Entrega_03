# Padrão Builder no Projeto

## Introdução  
Dentro do contexto do sistema desenvolvido, o padrão Builder surge como uma solução criacional para instanciar objetos complexos de forma clara, organizada e escalável [1](https://refactoring.guru/pt-br/design-patterns/builder>). Como muitas entidades do sistema possuem múltiplos atributos opcionais e podem ser construídas de formas variadas, o uso do Builder objetiva evitar a sobrecarga de construtores longos, melhora a legibilidade e reduz a chance de erros. Sendo assim, o padrão se integra ao projeto oferecendo um meio flexível de criação, sem expor detalhes internos de cada classe [1](https://refactoring.guru/pt-br/design-patterns/builder>).

## Objetivo/Metodologia
O objetivo do uso do Builder no projeto é permitir a criação de objetos complexos de forma controlada e passo a passo, melhorando a legibilidade e manutenção do código [2](https://medium.com/@jonesroberto/desing-patterns-parte-6-builder-f20752fb0c35), evitando múltiplos construtores, assim, facilitando a criação de objetos diferentes a partir do mesmo processo de construção, promovendo a reutilização de código [3](https://www.dio.me/articles/o-que-e-o-padrao-builder-javaspring-boot).  
Para conseguirmos desenvolver o artefato corretamente atualizamos o [diagrama de classes](https://mermaid.live/view#pako:eNqtV9tu20YQ_RVigQBpKqmS6JoWUQRw7KQIkDRGnL4Uehlxx9QW5K6yuzTcGv6aPAQt0K_Qj3WWF5XLi5Wm1YvImdm5z5nlPUsURxazJANjLgWkGvK1DOj35EkwnU6DC8iBQ8AxON9pNCgt7D_vPynHrATLo8FraVHfQII_mwK0UMF9xXW_b3NlrAb9ATN4o1Ihn37TZ75C5B4d78RG6Ist2Ib8sJajvmUiqR37LngFCRCx4-G1MBZzqJlt9zSmovSh9t1zI-s5TBRVWI8kpEgEeM6W9F2xcY7pK4oRUsz9AKWzeQ0ZHA_wUuX7v6TopX0g21PB40BI26JIlWMcUIhCpi0yZUNkA3Sq8haG6BZsYd7JTEhSt1EqQ5D_NlXIhQX9opNl4JRAJUGf5yL1WRpzdYs-45CoKgtX1Hoi85KwEWogAiqCiYM3VO0fKt5zLx3qVzHGrf2uLI244cp_pBI5SkONIBsv3lbveduPoqppI1KX2PNF3lK3NWc72YJUDLOaJlWS0mnA4yUq34G2ItuWAhYLPpbsRveRSJNay0AVOFh4SSEQjx7RihxbXIogUWiOFGIwwkMXvScdMNot9TD-twCuqtEmM4NRJAVlk4Ppa80dhrbq248w0WIMMqom7LC6bagk3sExTKiGuR8cddDHQhhnZ7BTCOJrnjMy4oIDtQ8EL5Yy9HXYxNFQGsrs9nhfMiBdaC3JBsQw3lZe_4gaJY2Iq5C_wDaZ-ljg8IKAW8jGxipF7ZoxA6tax8ZhnuDFUEj7P50bI1h_ef7O881AdgvaM7spTLl09GvesukD1f-gpunDr1blZeFFITJO8Y-EXbN9Q2h_ovbxa4z2pdtrXeK1W2odn0jjo4GN2OwCZEO_9GDhC201fTNkCzgf7DjOB-Gva8RLr-vCEhzL7m5luXdzm06f-5elSs6_Pzmh-sAY23XZGK_J8Bi_DSBjMt64NtE2QazZYs1KseqpviLEwU4ZUwgnPiT6jJ7KNU6Cbh8mYgePyR52SRw41H5UbQ3LcYB0ZoMZJujkS3Nd4cOSJb3Ubfs_cifqweqazWezZ4dT9UtjPQ7oLl9Uzvu41qocSeV0_9fQyZ4b6F6BG9DwS9vGAL-wnsamu3tau6PWb47ugPxjn01YqgVnsdUFTliOmgafXlk5Q2tmt0g7mcX0yPEGisyu2Vo-0LEdyF-UypuTWhXplsU3kBl6K3Zun9cfQwcRlGT8QhXSsvhsWapg8T27Y_HJajELw-X383B5FobRKjqdsN-IvJjNw8XJ2TxcRcvFabR4mLDfS6PzWXQaRauTKApXyzBahBPmFrvSb-uPMff38Df2ZRhc)

A aplicação do padrão seguiu os seguintes passos:  
**Identificação de classes complexas:** Foram analisadas as classes mais ricas em atributos e que demandam flexibilidade na criação, como `Usuario`, `Perfil` e `Postagem`.

**Definição do Builder:** Criou-se uma classe `UsuarioBuilder`, responsável por fornecer métodos encadeados para definir atributos como nome, email, senha, bio, amigos, etc.

**Implementação do produto final:** A classe `Usuario` foi mantida coesa, enquanto a lógica de construção foi extraída para o Builder.  

**Aplicação de fluência:** O Builder foi projetado para suportar encadeamento, tornando o código mais limpo e intuitivo.  

O artefato foi desenvolvido em pares por meio de troca de mensagens no WhatsApp, onde fomos desenvolvendo algumas linhas de código e enviando um ao outro para verificar a qualidade e completude dos códigos. Entrando em consenso também em relação à padronização dos comandos, como a autora não possuía tanta familiaridade com Java um estudo anterior teve que ser feito. Os primeiros passos foram selecionar quais eram as classes, em seguida seus conteúdos. O builder foi aplicado apenas em 3 classes, apenas para demonstrar seu desenvolvimento.

## Desenvolvimento

### Tecnologias usadas
**Java**
- Classes internas estáticas (`UsuarioBuilder`, `PostagemBuilder`, `ConversaBuilder`)
- Fluent Interface (métodos encadeados como `.setNome().setEmail().build()`)
- Collections (`List`, `ArrayList`) para gerenciar listas de usuários, mensagens e comentários.
- Date/Time API (`LocalDateTime`) para manipular datas de criação e publicação. 

### Usuário
O `UsuarioBuilder` permite criar usuários de forma incremental, atribuindo apenas os atributos necessários no momento da criação (nome, email, senha, bio). Essa flexibilidade ajuda tanto na etapa de cadastro quanto em edições futuras de perfil. Esse builder é essencial para garantir a consistência dos dados do usuário no sistema.  
```java
public class Usuario {
    private String nome;
    private String email;
    private String senha;
    private String bio;

    private Usuario(UsuarioBuilder builder) {
        this.nome = builder.nome;
        this.email = builder.email;
        this.senha = builder.senha;
        this.bio = builder.bio;
    }

    public static class UsuarioBuilder {
        private String nome;
        private String email;
        private String senha;
        private String bio;

        public UsuarioBuilder setNome(String nome) {
            this.nome = nome;
            return this;
        }

        public UsuarioBuilder setEmail(String email) {
            this.email = email;
            return this;
        }

        public UsuarioBuilder setSenha(String senha) {
            this.senha = senha;
            return this;
        }

        public UsuarioBuilder setBio(String bio) {
            this.bio = bio;
            return this;
        }

        public Usuario build() {
            return new Usuario(this);
        }
    }
}

```
#### Exemplo de Uso

```java
// Aqui temos a criação de um usuário básico para cadastro inicial
Usuario novoUsuario = new Usuario.UsuarioBuilder()
    .setNome("Marquinhos")
    .setEmail("Marcãoa@example.com")
    .setSenha("senhaForte123")
    .build();

// Aqui temos a criação de um usuário com todos os campos, como em uma edição de perfil
Usuario usuarioCompleto = new Usuario.UsuarioBuilder()
    .setNome("Sarinha")
    .setEmail("Sarão@example.com")
    .setSenha("outraSenha456")
    .setBio("Desenvolvedora Java e entusiasta de Design Patterns.")
    .build();
```

### Postagem
O `PostagemBuilder` foi criado para facilitar a criação de publicações dentro do feed social. Além do conteúdo principal, o builder permite adicionar comentários de maneira progressiva, assim como controlar a data de publicação. Essa abordagem facilita a manutenção de postagens dinâmicas e interativas, reforçando a ideia de engajamento dentro da plataforma.

```java
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Postagem {
    private String conteudo;
    private LocalDateTime dataPublicacao;
    private List<String> comentarios;

    private Postagem(PostagemBuilder builder) {
        this.conteudo = builder.conteudo;
        this.dataPublicacao = builder.dataPublicacao;
        this.comentarios = builder.comentarios;
    }

    public static class PostagemBuilder {
        private String conteudo;
        private LocalDateTime dataPublicacao = LocalDateTime.now();
        private List<String> comentarios = new ArrayList<>();

        public PostagemBuilder setConteudo(String conteudo) {
            this.conteudo = conteudo;
            return this;
        }

        public PostagemBuilder adicionarComentario(String comentario) {
            this.comentarios.add(comentario);
            return this;
        }

        public Postagem build() {
            return new Postagem(this);
        }
    }
}

```
#### Exemplo de Uso

```java
// Aqui temos, a criação de uma nova postagem e adicionando comentários
Postagem minhaPostagem = new Postagem.PostagemBuilder()
    .setConteudo("Hojeo")
    .adicionarComentario("Parabéns")
    .adicionarComentario("legal")
    .build();
```

### Conversa
O `ConversaBuilder` organiza a criação de conversas entre os usuários. Ele permite adicionar participantes e mensagens de forma incremental, garantindo que uma conversa seja construída passo a passo. Esse padrão é útil, pois uma conversa pode começar vazia e ir evoluindo conforme os usuários interagem. Além disso, mantém a consistência entre participantes e mensagens.

```java
import java.util.ArrayList;
import java.util.List;

public class Conversa {
    private List<Usuario> participantes;
    private List<String> mensagens;

    private Conversa(ConversaBuilder builder) {
        this.participantes = builder.participantes;
        this.mensagens = builder.mensagens;
    }

    public static class ConversaBuilder {
        private List<Usuario> participantes = new ArrayList<>();
        private List<String> mensagens = new ArrayList<>();

        public ConversaBuilder adicionarParticipante(Usuario usuario) {
            this.participantes.add(usuario);
            return this;
        }

        public ConversaBuilder adicionarMensagem(String mensagem) {
            this.mensagens.add(mensagem);
            return this;
        }

        public Conversa build() {
            return new Conversa(this);
        }
    }
}

```
#### Exemplo de Uso

```java
// Aqui temos uma suposição de que 'novoUsuario' e 'usuarioCompleto' foram criados anteriormente
Conversa chat = new Conversa.ConversaBuilder()
    .adicionarParticipante(novoUsuario)
    .adicionarParticipante(usuarioCompleto)
    .adicionarMensagem("Oie Sarah, blz?")
    .build();
```
## Bibliografia

Conjunto de obras consultadas. 

> Builder. Disponível em: <https://refactoring.guru/pt-br/design-patterns/builder>.

> JONES ROBERTO NUZZI. Design Patterns — Parte 6 — Builder - Jones Roberto Nuzzi - Medium. Disponível em: <https://medium.com/@jonesroberto/desing-patterns-parte-6-builder-f20752fb0c35>.

> AFONSO, N. O que é o padrão Builder? Java/Spring Boot. Disponível em: <https://www.dio.me/articles/o-que-e-o-padrao-builder-javaspring-boot>. 

## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 24/09/2025  | Criação do documento e códigos da builder |[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)|-|-|
| `1.1`  | 27/09/2025  | A metodologia foi melhor completada e as referências foram inseridas em seus respectivos lugares  |[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)|-|-|
| `1.2`  | 27/09/2025  | Atualização do diagrama de classes e inserção do seu link  |[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)| Ajustes na grámatica e formatação | [João Pedro Costa](https://github.com/johnaopedro) |
| `1.3`  | 30/09/2025  | Adição de exemplos de uso dos códigos e enfatisando pontos da documentação com aspas  |[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)|-|-|


