# Padrão Builder no Projeto

## Introdução  
Dentro do contexto do sistema desenvolvido, o padrão Builder surge como uma solução criacional para instanciar objetos complexos de forma clara, organizada e escalável [1](https://refactoring.guru/pt-br/design-patterns/builder>). Como muitas entidades do sistema possuem múltiplos atributos opcionais e podem ser construídas de formas variadas, o uso do Builder objetiva evitar a sobrecarga de construtores longos, melhora a legibilidade e reduz a chance de erros. Sendo assim, o padrão se integra ao projeto oferecendo um meio flexível de criação, sem expor detalhes internos de cada classe [1](https://refactoring.guru/pt-br/design-patterns/builder>).

## Objetivo/Metodologia
O objetivo do uso do Builder no projeto é permitir a criação de objetos complexos de forma controlada e passo a passo, melhorando a legibilidade e manutenção do código [2](https://medium.com/@jonesroberto/desing-patterns-parte-6-builder-f20752fb0c35), evitando múltiplos construtores, assim, facilitando a criação de objetos diferentes a partir do mesmo processo de construção, promovendo a reutilização de código [3](https://www.dio.me/articles/o-que-e-o-padrao-builder-javaspring-boot).

A aplicação do padrão seguiu os seguintes passos:  
**Identificação de classes complexas:** Foram analisadas as classes mais ricas em atributos e que demandam flexibilidade na criação, como Usuario, Perfil e Postagem.  

**Definição do Builder:** Criou-se uma classe UsuarioBuilder, responsável por fornecer métodos encadeados para definir atributos como nome, email, senha, bio, amigos etc.

**Implementação do produto final:** A classe Usuario foi mantida coesa, enquanto a lógica de construção foi extraída para o Builder.  

**Aplicação de fluência:** O Builder foi projetado para suportar encadeamento, tornando o código mais limpo e intuitivo.  

O artefato foi desenvolvido em pares por meio de troca de mensagens no WhatsApp, onde fomos desenvolvendo algumas linhas de código e enviando um ao outro para verificar a qualidade e completude dos códigos. Entrando em consenso também em relação à padronização dos comando, como a autora não possuia tanta familiaridade com Java um estudo anterior teve que ser feito. Os primeiros passos foram selecionar quais eram as classes, em seguida seus conteúdos. O builder foi aplicado apenas em 3 classes, apenas para demonstrar seu desenvolvimento.

## Desenvolvimento

### Tecnologias usadas
**Java**
- Classes internas estáticas (UsuarioBuilder, PostagemBuilder, ConversaBuilder)
- Fluent Interface (métodos encadeados como .setNome().setEmail().build())
- Collections (List, ArrayList) para gerenciar listas de usuários, mensagens e comentários.
- Date/Time API (LocalDataTime) para manipular datas de criação e publicação. 

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

### Postagem
O PostagemBuilder foi criado para facilitar a criação de publicações dentro do feed social. Além do conteúdo principal, o builder permite adicionar comentários de maneira progressiva, assim como controlar a data de publicação. Essa abordagem facilita a manutenção de postagens dinâmicas e interativas, reforçando a ideia de engajamento dentro da plataforma.

```java
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

### Conversa
O ConversaBuilder organiza a criação de conversas entre os usuários. Ele permite adicionar participantes e mensagens de forma incremental, garantindo que uma conversa seja construída passo a passo. Esse padrão é útil, pois uma conversa pode começar vazia e ir evoluindo conforme os usuários interagem. Além disso, mantém a consistência entre participantes e mensagens.

```java
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
