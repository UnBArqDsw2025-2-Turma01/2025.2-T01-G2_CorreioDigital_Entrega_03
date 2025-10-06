# Padrão Factory Method no Projeto

## Introdução  

O **Factory Method** é um padrão de projeto criacional da Engenharia de Software cujo objetivo é **definir uma interface para a criação de objetos**, permitindo que as subclasses decidam **qual classe concreta instanciar**. Em vez de criar objetos diretamente através do operador `new`, o padrão delega a responsabilidade de construção para métodos especializados, conhecidos como *métodos fábrica*.  

Esse mecanismo promove o **baixo acoplamento** entre classes, já que o código cliente não precisa conhecer detalhes sobre como os objetos são instanciados, apenas sobre a interface ou classe abstrata que será retornada. Como consequência, a arquitetura torna-se mais **flexível e extensível**, permitindo a introdução de novos tipos de produtos sem modificar o código já existente.  

Na modelagem UML, o padrão é representado por uma **classe abstrata (Creator)** que declara o método fábrica, e por **subclasses concretas (ConcreteCreator)** que implementam esse método retornando objetos de **produtos específicos (ConcreteProduct)**, os quais geralmente compartilham uma mesma **interface comum (Product)**.  

O Factory Method é especialmente útil em sistemas que lidam com **famílias de objetos complexos ou variáveis**, como no caso de plataformas sociais que precisam instanciar diferentes tipos de **mensagens, postagens, notificações ou usuários**. Assim, garante-se que a criação desses elementos ocorra de forma centralizada e padronizada, contribuindo para a **manutenção, clareza e evolução** do software.


## Objetivo/Metodologia

O uso do padrão **Factory Method** neste projeto tem como objetivo **organizar e padronizar o processo de criação de objetos**, evitando a dependência direta do código em classes concretas e facilitando a manutenção e evolução do sistema. Dessa forma, busca-se **reduzir o acoplamento**, aumentar a **extensibilidade** e permitir a inclusão de novos tipos de elementos (como mensagens, posts, notificações e comentários) sem a necessidade de modificar partes centrais da aplicação.  

A metodologia adotada para implementação consistiu, inicialmente, na **identificação das principais entidades do sistema** que apresentam múltiplas variações de comportamento ou conteúdo. Entre elas destacam-se: **usuários e moderadores, mensagens (texto, imagem, vídeo), postagens (texto, imagem, vídeo), notificações (amizade, mensagens, post, moderação) e comentários**.  

Com base nessa análise, foram definidos **creators abstratos** para cada família de objetos, responsáveis por declarar o método fábrica, e **creators concretos** para cada tipo específico de produto. Assim, cada fábrica concreta encapsula a lógica de criação de sua respectiva classe, garantindo maior clareza e isolamento da responsabilidade de construção.  

Essa abordagem foi fundamentada em práticas de **engenharia de software orientada a objetos**, aliada a uma **modelagem UML** que permitiu visualizar as relações entre criadores, produtos e suas variações. Por fim, o padrão foi validado dentro do escopo do projeto por meio de exemplos de uso, demonstrando sua aplicabilidade na gestão de conteúdos e interações da plataforma. 

Para acessar o Diagrama UML (Factory Method) construído [clique aqui](https://mermaid.live/view#pako:eNq1WP1q2zoUfxVjGKRcp9SZ-2VKYbQMBrdj7G77Y-SfE0tNxWzJk-XQj3Xvch9gT7EXmyTHseRIbtJmoTS2zqfOOTq_ozyEGUM4TMMsh6q6JDDnUExpID-vXgXj8Ti4UARcBSUnNCMlkCpATP4Vv39RwhRLw64VBJ-rGrhcfmgW1WdMUJAG_wkpPzdW6wpzCgV20XABJHcRSsyvNeWDfjAokAmyUMpmjOUYaEf6B9MFAX6FaQVzXIwQrgShIJSfUVAsl_cMAY4zPMOdhIsHEMkIo8DfFGTORnWzb5NjlrPvNQa-DEmP5XFKzbhdySxwQIybkZOOLEgF_AOrxKiU_0z1-DbLa-KmzYASj11NlyF4igUo5Mr2Jaa1zDvIsDUPbv-bfFhpR6Qqc7h778nxTFaJY5kgwgqoFAmLnw35p0EXMHcS-_7IiGxQhFCLGxnztK1bg5RxDAKjN0JS_2UZ5Jfy9RMpsJkDRMQoY1TgGvUCnGOBR3bBoAsmK0nXnRRqH02enHzDw3Wi9vUJ3wr7hAm9Yu_PIfiuUFVsh0UtfebOw5ZBKWSJP633C0HYdmihVl6itgvVy7LoikyXOsoWTEfTn7v-OV22gg28qjCVZ9rplWowsls5icq-oo229ulZddEK_43aaHX_hfp4zwS5JhlksEmByHiTksiCcp90dYA1ba1KXLkogH_7iAF5smF41u7fQ5bIcQ8Ie6jqYPn0arCQD7bltlVvFJCSceGpTkFKZ2vmcA_Os8RxxfIFHunvWiWvH5rlLPH29_8zLvdQBaO3ErAZv5M1Is8u2vPMEReqCdugeHYGs0rI7Yvzc8OHpl23gEZQFLQDRhTocSIKmuFhz95xL3utXVbUhcP4rsys4P6FNlZ6vL152wjqeULZbJqqNAV3OQOZoa4gfZjk38ywVi38BGo9V3cjPQxdz9WthQc737bRX42cymYDIFHQooVh3e4sQ3jg39u2tvxZsjFkdxYHcmdBy-4s-jNqtN9tk2qIaj9WaBQFS-jZM9Vviir-XW9pcLCY1vFqZ3Yt_POb9XSx59n0NjEXvO4uwh1gu2DxI85BXybVzMuqDgvb2_TZD8nV6_UtbTw-t27D1vpqt-aqnW-TslaF-hqlrff6tE0wD6pNMQ6UJigr3WzfEFYzdbPN9XbjZjCNujkM4-a8qHm89T_EaVXsEGMX-EHD_TmuN_VofsdE4mfuzxVd5C22PmIPsFk9fYDPbMR2TmwHHdi0AbvDi0H-dW8c_dtXB9vK2X1xYzEjjJu72GtNUxpG4ZwTFKaC1zgKC8zlhChfQ920pqG4wQWehql8RPga6lxMwyl9lGIl0K-MFa0kZ_X8JkyvIa_kW10i2eaWvweuWDSAXrCaijA91hrC9CG8DdM4jvfj5PD1wWmSnEySSXwahXdhOkni_ddHk4Ojg8Pk6OT48DEK77XJyf4kTpKj-OD4-CQ5jeNEalM3csavlj9Hqq_HP6v9pLs)



## Desenvolvimento


### Tecnologias usadas

A tecnologia utilizada para implementar o Factory Method neste projeto foi a linguagem de programação **Java**, escolhida por sua forte orientação a objetos e suporte nativo a princípios de design patterns. Para o desenvolvimento, foram utilizadas as bibliotecas padrão do Java SE, `java.time.LocalDateTime` e `java.util.*`, responsáveis respectivamente pelo gerenciamento de datas e pela manipulação de listas e coleções. A combinação dessas bibliotecas com o padrão Factory Method permitiu estruturar um sistema modular e extensível, facilitando a criação e o gerenciamento de diferentes tipos de objetos de maneira organizada e de baixo acoplamento.

### **Domínio**

O domínio deste projeto corresponde ao conjunto de entidades, regras e interações que representam o funcionamento do sistema de troca de idiomas entre usuários. Ele abrange os elementos centrais do aplicativo, como usuários, moderadores, postagens, comentários, mensagens, denúncias e notificações, e define como esses componentes se relacionam e operam entre si.

### Perfil

O domínio de **Perfil** é responsável por encapsular as informações complementares e preferências associadas a um usuário, além de prover métodos para atualização e exibição de dados pessoais.

```java
    class Perfil {
        private String displayName;
        private String bio;
        private Set<String> idiomas = new HashSet<>();
        private Set<String> tags = new HashSet<>();
        private String avatarUrl;

        public Perfil(String displayName, String bio) {
            this.displayName = displayName;
            this.bio = bio;
        }

        public String getDisplayName() { return displayName; }
        public void setDisplayName(String displayName) { this.displayName = displayName; }
        public String getBio() { return bio; }
        public void setBio(String bio) { this.bio = bio; }
        public Set<String> getIdiomas() { return idiomas; }
        public Set<String> getTags() { return tags; }
        public String getAvatarUrl() { return avatarUrl; }
        public void setAvatarUrl(String avatarUrl) { this.avatarUrl = avatarUrl; }

        public void adicionarIdioma(String idioma) { idiomas.add(idioma); }
        public void removerIdioma(String idioma) { idiomas.remove(idioma); }
        public void adicionarTag(String tag) { tags.add(tag); }
        public void removerTag(String tag) { tags.remove(tag); }

        @Override
        public String toString() {
            return "Perfil{" +
                    "displayName='" + displayName + '\'' +
                    ", bio='" + bio + '\'' +
                    ", idiomas=" + idiomas +
                    ", tags=" + tags +
                    ", avatarUrl='" + avatarUrl + '\'' +
                    '}';
        }
    }
```


### Usuário

O domínio de **Usuario** é responsável pela representação e gerenciamento de entidades que interagem com o sistema.
Ele define a estrutura e o comportamento básico de um usuário comum, incluindo seus dados de identificação e métodos de interação.

```java
    class Usuario {
        protected String id;
        protected String username;
        protected String email;
        protected Perfil perfil;
        protected boolean active = true;
        protected List<Usuario> amigos = new ArrayList<>();
        protected Set<Usuario> bloqueados = new HashSet<>();
        protected List<Notificacao> notificacoes = new ArrayList<>();

        public Usuario(String id, String username, String email, Perfil perfil) {
            this.id = id;
            this.username = username;
            this.email = email;
            this.perfil = perfil;
        }

        public void enviarMensagem(Usuario destinatario, Mensagem mensagem) {
            System.out.println("[" + username + "] enviando mensagem para [" + destinatario.username + "]: " + mensagem.summary());
            mensagem.deliver();
            destinatario.receberMensagem(mensagem);
        }

        public void receberMensagem(Mensagem mensagem) {
            System.out.println("[" + username + "] recebeu mensagem: " + mensagem.summary());
            Notificacao n = new NotificacaoMensagem(UUID.randomUUID().toString(), this, "Você recebeu uma nova mensagem de " + mensagem.getSender().username);
            receberNotificacao(n);
        }

        public void adicionarAmigo(Usuario u) {
            if (!amigos.contains(u) && !bloqueados.contains(u) && u.active) {
                amigos.add(u);
                System.out.println("[" + username + "] adicionou [" + u.username + "] como amigo.");
            }
        }

        public void removerAmigo(Usuario u) {
            amigos.remove(u);
            System.out.println("[" + username + "] removeu [" + u.username + "] dos amigos.");
        }

        public void bloquearUsuario(Usuario u) {
            bloqueados.add(u);
            amigos.remove(u);
            System.out.println("[" + username + "] bloqueou [" + u.username + "].");
        }

        public void desbloquearUsuario(Usuario u) {
            if (bloqueados.remove(u)) {
                System.out.println("[" + username + "] desbloqueou [" + u.username + "].");
            }
        }

        public void receberNotificacao(Notificacao n) {
            notificacoes.add(n);
            System.out.println("[" + username + "] Notificação recebida: " + n.getContent());
        }

        public void editarPerfil(Perfil novoPerfil) {
            this.perfil = novoPerfil;
            System.out.println("[" + username + "] atualizou o perfil.");
        }

        public String getId() { return id; }
        public String getUsername() { return username; }
        public Perfil getPerfil() { return perfil; }

        @Override
        public String toString() {
            return "Usuario{" +
                    "id='" + id + '\'' +
                    ", username='" + username + '\'' +
                    ", email='" + email + '\'' +
                    ", perfil=" + perfil +
                    ", active=" + active +
                    '}';
        }
    }
```

### Moderador

O domínio de **Moderador** estende as funcionalidades dos usuários, incorporando permissões administrativas voltadas à moderação de conteúdo e controle de interações na plataforma.

```java
    class Moderador extends Usuario {

        public Moderador(String id, String username, String email, Perfil perfil) {
            super(id, username, email, perfil);
        }

        public void revisarPost(Post post) {
            System.out.println("[" + username + " - Moderador] revisando post: " + post.getId());
            if (post.isInadequado()) {
                excluirPost(post);
            } else {
                System.out.println("[" + username + "] não detectou infração no post " + post.getId());
            }
        }

        public void excluirPost(Post post) {
            post.delete();
            System.out.println("[" + username + "] excluiu o post " + post.getId());
        }

        public void banirUsuario(Usuario u) {
            u.active = false;
            System.out.println("[" + username + "] baniu o usuário " + u.username);
        }

        public void desbanirUsuario(Usuario u) {
            u.active = true;
            System.out.println("[" + username + "] desbaniu o usuário " + u.username);
        }

        public void analisarDenuncia(Denuncia d) {
            System.out.println("[" + username + "] analisando denúncia: " + d.getId() + " motivo: " + d.getRazao());
            if (d.getTipo().equalsIgnoreCase("post")) {
                revisarPost(d.getPost());
                d.resolve("Revisado pelo moderador: ação aplicada");
            } else if (d.getTipo().equalsIgnoreCase("usuario")) {
                banirUsuario(d.getReportedUser());
                d.resolve("Usuário banido pelo moderador");
            } else {
                d.resolve("Arquivada sem ação");
            }
        }
    }

```

### Postagem

O domínio de **Post** representa o núcleo de conteúdo da aplicação, definindo a estrutura de uma postagem, suas propriedades e comportamentos relacionados à criação, edição e exclusão de publicações.

```java
    abstract class Post {
        protected String id;
        protected Usuario author;
        protected LocalDateTime createdAt;
        protected LocalDateTime editedAt;
        protected int likes = 0;
        protected List<Comentario> comentarios = new ArrayList<>();
        protected boolean deleted = false;

        public Post(String id, Usuario author) {
            this.id = id;
            this.author = author;
            this.createdAt = LocalDateTime.now();
        }

        public abstract String getType();
        public abstract String preview();

        public void edit(String content) {
            this.editedAt = LocalDateTime.now();
            System.out.println("Post " + id + " editado. Novo preview: " + preview());
        }

        public void delete() {
            this.deleted = true;
            System.out.println("Post " + id + " marcado como excluído.");
        }

        public void addComentario(Comentario c) {
            comentarios.add(c);
            System.out.println("Comentário adicionado ao post " + id + " por " + c.getAuthor().username);
        }

        public void removerComentario(Comentario c) {
            comentarios.remove(c);
            System.out.println("Comentário removido do post " + id);
        }

        public void like(Usuario u) {
            likes++;
            System.out.println("[" + u.username + "] curtiu o post " + id + ". Total likes: " + likes);
        }

        public boolean isInadequado() {
            // Heurística simples para exemplo (no real, regras mais complexas)
            return false;
        }

        public String getId() { return id; }
        public Usuario getAuthor() { return author; }
    }

    class PostTexto extends Post {
        private String texto;

        public PostTexto(String id, Usuario author, String texto) {
            super(id, author);
            this.texto = texto;
        }

        @Override
        public String getType() { return "TEXTO"; }

        @Override
        public String preview() { return texto.length() > 100 ? texto.substring(0, 100) + "..." : texto; }
    }

    class PostImagem extends Post {
        private String imageUrl;
        private String caption;

        public PostImagem(String id, Usuario author, String imageUrl, String caption) {
            super(id, author);
            this.imageUrl = imageUrl;
            this.caption = caption;
        }

        @Override
        public String getType() { return "IMAGEM"; }

        @Override
        public String preview() { return caption != null ? caption : imageUrl; }
    }

    class PostVideo extends Post {
        private String videoUrl;
        private String caption;

        public PostVideo(String id, Usuario author, String videoUrl, String caption) {
            super(id, author);
            this.videoUrl = videoUrl;
            this.caption = caption;
        }

        @Override
        public String getType() { return "VIDEO"; }

        @Override
        public String preview() { return caption != null ? caption : videoUrl; }
    }
```

### Comentário

O domínio de **Comentario** implementa as funcionalidades de interação textual entre usuários em postagens, controlando a criação, associação e exibição de respostas dentro de um contexto de discussão.

```java
    class Comentario {
        private String id;
        private Usuario author;
        private String texto;
        private LocalDateTime createdAt;
        private boolean deleted = false;

        public Comentario(String id, Usuario author, String texto) {
            this.id = id;
            this.author = author;
            this.texto = texto;
            this.createdAt = LocalDateTime.now();
        }

        public void edit(String novoTexto) {
            this.texto = novoTexto;
            System.out.println("Comentário " + id + " editado.");
        }

        public void delete() {
            this.deleted = true;
            System.out.println("Comentário " + id + " excluído.");
        }

        public Usuario getAuthor() { return author; }
        public String getTexto() { return texto; }
    }
```


### Conversa

O domínio de **Mensagem** gerencia a comunicação direta entre usuários, abrangendo o envio, recebimento e histórico de mensagens dentro da plataforma.

```java
    abstract class Mensagem {
        protected String id;
        protected Usuario sender;
        protected Usuario receiver;
        protected LocalDateTime timestamp;
        protected boolean deleted = false;

        public Mensagem(String id, Usuario sender, Usuario receiver) {
            this.id = id;
            this.sender = sender;
            this.receiver = receiver;
            this.timestamp = LocalDateTime.now();
        }

        public abstract void deliver();
        public void delete() {
            this.deleted = true;
            System.out.println("Mensagem " + id + " deletada.");
        }

        public String summary() {
            return "[" + getClass().getSimpleName() + " de " + sender.username + " para " + receiver.username + " em " + timestamp + "]";
        }

        public Usuario getSender() { return sender; }
    }

    class MensagemTexto extends Mensagem {
        private String texto;

        public MensagemTexto(String id, Usuario sender, Usuario receiver, String texto) {
            super(id, sender, receiver);
            this.texto = texto;
        }

        @Override
        public void deliver() {
            System.out.println("Delivering texto: " + texto);
        }

        public String getTexto() { return texto; }
    }

    class MensagemImagem extends Mensagem {
        private String imageUrl;
        private String caption;

        public MensagemImagem(String id, Usuario sender, Usuario receiver, String imageUrl, String caption) {
            super(id, sender, receiver);
            this.imageUrl = imageUrl;
            this.caption = caption;
        }

        @Override
        public void deliver() {
            System.out.println("Delivering imagem: " + imageUrl + " (caption: " + caption + ")");
        }
    }

    class MensagemVideo extends Mensagem {
        private String videoUrl;
        private String caption;

        public MensagemVideo(String id, Usuario sender, Usuario receiver, String videoUrl, String caption) {
            super(id, sender, receiver);
            this.videoUrl = videoUrl;
            this.caption = caption;
        }

        @Override
        public void deliver() {
            System.out.println("Delivering vídeo: " + videoUrl + " (caption: " + caption + ")");
        }
    }
```




### Notificação

O domínio de **Notificacao** é responsável por criar e distribuir alertas relacionados a eventos relevantes do sistema, como novas mensagens, comentários ou interações.

```java
    abstract class Notificacao {
        protected String id;
        protected Usuario recipient;
        protected String content;
        protected LocalDateTime timestamp;
        protected boolean read = false;

        public Notificacao(String id, Usuario recipient, String content) {
            this.id = id;
            this.recipient = recipient;
            this.content = content;
            this.timestamp = LocalDateTime.now();
        }

        public void deliver() {
            System.out.println("Notificação para " + recipient.username + ": " + content);
        }

        public void markRead() {
            this.read = true;
            System.out.println("Notificação " + id + " marcada como lida.");
        }

        public String getContent() { return content; }
    }

    class NotificacaoMensagem extends Notificacao {
        public NotificacaoMensagem(String id, Usuario recipient, String content) {
            super(id, recipient, content);
        }
    }

    class NotificacaoAmizade extends Notificacao {
        public NotificacaoAmizade(String id, Usuario recipient, String content) {
            super(id, recipient, content);
        }
    }

    class NotificacaoPost extends Notificacao {
        public NotificacaoPost(String id, Usuario recipient, String content) {
            super(id, recipient, content);
        }
    }

    class NotificacaoModeracao extends Notificacao {
        public NotificacaoModeracao(String id, Usuario recipient, String content) {
            super(id, recipient, content);
        }
    }
```


### Denúncia

O domínio de **Denuncia** trata do gerenciamento de reclamações ou sinalizações feitas por usuários sobre conteúdos inadequados, viabilizando a moderação e o controle da qualidade da comunidade.

```java
    class Denuncia {
        private String id;
        private Usuario reporter;
        private Post post;
        private Usuario reportedUser;
        private String tipo;
        private String razao;
        private LocalDateTime createdAt;
        private boolean resolved = false;
        private String resolution;

        public Denuncia(String id, Usuario reporter, String tipo, String razao) {
            this.id = id;
            this.reporter = reporter;
            this.tipo = tipo;
            this.razao = razao;
            this.createdAt = LocalDateTime.now();
        }

        public String getId() { return id; }
        public String getTipo() { return tipo; }
        public String getRazao() { return razao; }
        public Post getPost() { return post; }
        public Usuario getReportedUser() { return reportedUser; }

        public void attachPost(Post p) { this.post = p; }
        public void attachReportedUser(Usuario u) { this.reportedUser = u; }

        public void resolve(String resolution) {
            this.resolved = true;
            this.resolution = resolution;
            System.out.println("Denúncia " + id + " resolvida: " + resolution);
        }
    }
```


### Creators

Os creators neste contexto representam as classes responsáveis pela criação e gerenciamento das instâncias das entidades do domínio, seguindo o padrão de projeto Factory Method. Elas centralizam a lógica de construção de objetos, garantindo que cada elemento do sistema seja criado de forma padronizada e coerente com as regras de negócio.

### Perfil

```java
    abstract class PerfilCreator {
        public abstract Perfil createPerfil(String displayName, String bio, Set<String> idiomas, Set<String> tags, String avatarUrl);
    }

    class PerfilDefaultCreator extends PerfilCreator {
        @Override
        public Perfil createPerfil(String displayName, String bio, Set<String> idiomas, Set<String> tags, String avatarUrl) {
            Perfil p = new Perfil(displayName, bio);
            if (idiomas != null) idiomas.forEach(p::adicionarIdioma);
            if (tags != null) tags.forEach(p::adicionarTag);
            p.setAvatarUrl(avatarUrl);
            return p;
        }
    }
```


### Usuário

```java
    abstract class UsuarioCreator {
        public abstract Usuario createUsuario(String id, String username, String email, Perfil perfil);
    }

    class UsuarioComumCreator extends UsuarioCreator {
        @Override
        public Usuario createUsuario(String id, String username, String email, Perfil perfil) {
            return new Usuario(id, username, email, perfil);
        }
    }
```

### Moderador

```java
    class ModeradorCreator extends UsuarioCreator {
        @Override
        public Usuario createUsuario(String id, String username, String email, Perfil perfil) {
            return new Moderador(id, username, email, perfil);
        }
    }
```

### Postagem

```java
    abstract class PostCreator {
        public abstract Post createPost(String id, Usuario author, Map<String,String> payload);
    }

    class PostTextoCreator extends PostCreator {
        @Override
        public Post createPost(String id, Usuario author, Map<String,String> payload) {
            String texto = payload.getOrDefault("texto", "");
            return new PostTexto(id, author, texto);
        }
    }

    class PostImagemCreator extends PostCreator {
        @Override
        public Post createPost(String id, Usuario author, Map<String,String> payload) {
            String imageUrl = payload.get("imageUrl");
            String caption = payload.getOrDefault("caption", "");
            return new PostImagem(id, author, imageUrl, caption);
        }
    }

    class PostVideoCreator extends PostCreator {
        @Override
        public Post createPost(String id, Usuario author, Map<String,String> payload) {
            String videoUrl = payload.get("videoUrl");
            String caption = payload.getOrDefault("caption", "");
            return new PostVideo(id, author, videoUrl, caption);
        }
    }
```

### Comentário

```java
    abstract class ComentarioCreator {
        public abstract Comentario createComentario(String id, Usuario author, String texto);
    }

    /** Criador padrão de comentários */
    class ComentarioSimpleCreator extends ComentarioCreator {
        @Override
        public Comentario createComentario(String id, Usuario author, String texto) {
            // possível lugar para validações (texto não vazio, author ativo etc.)
            if (texto == null) texto = "";
            Comentario c = new Comentario(id, author, texto);
            return c;
        }
    }
```


### Conversa

```java
    abstract class MensagemCreator {
        public abstract Mensagem createMensagem(String id, Usuario sender, Usuario receiver, Map<String,String> payload);
    }

    class MensagemTextoCreator extends MensagemCreator {
        @Override
        public Mensagem createMensagem(String id, Usuario sender, Usuario receiver, Map<String,String> payload) {
            String texto = payload.getOrDefault("texto", "");
            return new MensagemTexto(id, sender, receiver, texto);
        }
    }

    class MensagemImagemCreator extends MensagemCreator {
        @Override
        public Mensagem createMensagem(String id, Usuario sender, Usuario receiver, Map<String,String> payload) {
            String url = payload.get("imageUrl");
            String caption = payload.getOrDefault("caption", "");
            return new MensagemImagem(id, sender, receiver, url, caption);
        }
    }

    class MensagemVideoCreator extends MensagemCreator {
        @Override
        public Mensagem createMensagem(String id, Usuario sender, Usuario receiver, Map<String,String> payload) {
            String url = payload.get("videoUrl");
            String caption = payload.getOrDefault("caption", "");
            return new MensagemVideo(id, sender, receiver, url, caption);
        }
    }
```


### Notificação

```java
    abstract class NotificacaoCreator {
        public abstract Notificacao createNotificacao(String id, Usuario recipient, String message);
    }

    class NotificacaoMensagemCreator extends NotificacaoCreator {
        @Override
        public Notificacao createNotificacao(String id, Usuario recipient, String message) {
            return new NotificacaoMensagem(id, recipient, message);
        }
    }

    class NotificacaoAmizadeCreator extends NotificacaoCreator {
        @Override
        public Notificacao createNotificacao(String id, Usuario recipient, String message) {
            return new NotificacaoAmizade(id, recipient, message);
        }
    }

    class NotificacaoPostCreator extends NotificacaoCreator {
        @Override
        public Notificacao createNotificacao(String id, Usuario recipient, String message) {
            return new NotificacaoPost(id, recipient, message);
        }
    }

    class NotificacaoModeracaoCreator extends NotificacaoCreator {
        @Override
        public Notificacao createNotificacao(String id, Usuario recipient, String message) {
            return new NotificacaoModeracao(id, recipient, message);
        }
    }
```

### Denúncia

```java
    abstract class DenunciaCreator {
        public abstract Denuncia createDenuncia(String id, Usuario reporter, String tipo, String razao, Map<String,Object> context);
    }

    class DenunciaPostCreator extends DenunciaCreator {
        @Override
        public Denuncia createDenuncia(String id, Usuario reporter, String tipo, String razao, Map<String,Object> context) {
            Denuncia d = new Denuncia(id, reporter, tipo, razao);
            // espera que context contenha a chave "post"
            if (context != null && context.containsKey("post")) {
                Post p = (Post) context.get("post");
                d.attachPost(p);
            }
            return d;
        }
    }

    class DenunciaUsuarioCreator extends DenunciaCreator {
        @Override
        public Denuncia createDenuncia(String id, Usuario reporter, String tipo, String razao, Map<String,Object> context) {
            Denuncia d = new Denuncia(id, reporter, tipo, razao);
            if (context != null && context.containsKey("reportedUser")) {
                Usuario reported = (Usuario) context.get("reportedUser");
                d.attachReportedUser(reported);
            }
            return d;
        }
    }
```


### Exemplo de Uso

O código abaixo demonstra um cenário completo de uso do sistema, representando a interação entre diferentes classes do domínio:

- Dois perfis são criados: Joao e Maria.
- Em seguida, são instanciados um usuário e uma moderadora com base nesses perfis.
- Joao cria uma postagem convidando outros usuários a praticarem italiano.
- Maria comenta no post, iniciando uma interação pública.
- Depois, ela envia uma mensagem privada a Joao, gerando uma notificação automática.
- Por fim, Joao cria uma denúncia referente a um post (exemplo de moderação de conteúdo), e Maria, como moderadora, remove o post denunciado.

Esse fluxo cobre todas as principais funcionalidades do sistema como criação de contas, interação social (post e comentários), comunicação privada (mensagens), alertas (notificações) e mecanismos de moderação (denúncias).

```java
    public class MainFactoryUpdated {
        public static void main(String[] args) {
            // 1) CRIANDO PERFIS
            PerfilCreator perfilCreator = new PerfilDefaultCreator();

            Set<String> idiomasJoao = new HashSet<>(Arrays.asList("Português", "Inglês"));
            Set<String> tagsJoao = new HashSet<>(Arrays.asList("viagens", "tecnologia"));
            Perfil perfilJoao = perfilCreator.createPerfil(
                    "João",
                    "Amo praticar idiomas e conhecer culturas.",
                    idiomasJoao,
                    tagsJoao,
                    "https://img/joao.png"
            );

            Set<String> idiomasMaria = new HashSet<>(Arrays.asList("Inglês", "Espanhol"));
            Set<String> tagsMaria = new HashSet<>(Arrays.asList("educação"));
            Perfil perfilMaria = perfilCreator.createPerfil(
                    "Maria",
                    "Interesse em ensino e intercâmbio cultural.",
                    idiomasMaria,
                    tagsMaria,
                    "https://img/maria.png"
            );

            // 2) CRIANDO USUÁRIOS
            UsuarioCreator userCreator = new UsuarioComumCreator();
            Usuario joao = userCreator.createUsuario("u1", "joao-g", "joao@example.com", perfilJoao);

            UsuarioCreator modCreator = new ModeradorCreator();
            Moderador maria = (Moderador) modCreator.createUsuario("u2", "maria-m", "maria@example.com", perfilMaria);

            // 3) JOÃO CRIA UM POST
            PostCreator postTextoCreator = new PostTextoCreator();
            Map<String, String> payloadPost = new HashMap<>();
            payloadPost.put("texto", "Olá! Alguém para praticar italiano hoje?");
            Post post1 = postTextoCreator.createPost("post1", joao, payloadPost);
            System.out.println("Post criado por " + post1.getAuthor().getUsername() + ": " + post1.preview());

            // 4) MARIA COMENTA NO POST DE JOÃO
            ComentarioCreator comentarioCreator = new ComentarioSimpleCreator();
            Comentario comentarioMaria = comentarioCreator.createComentario("c1", maria, "Posso te ajudar! Quando quer praticar?");
            post1.addComentario(comentarioMaria);
            post1.like(maria);

            // 5) MARIA ENVIA MENSAGEM PRIVADA A JOÃO
            MensagemCreator mensagemCreator = new MensagemTextoCreator();
            Map<String, String> payloadMsg = new HashMap<>();
            payloadMsg.put("texto", "Podemos marcar uma conversa por vídeo amanhã?");
            Mensagem m1 = mensagemCreator.createMensagem("m1", maria, joao, payloadMsg);

            maria.enviarMensagem(joao, m1);

            // 6) SISTEMA GERA UMA NOTIFICAÇÃO
            NotificacaoCreator notifCreator = new NotificacaoAmizadeCreator();
            Notificacao n1 = notifCreator.createNotificacao("n1", joao, "Você tem uma nova solicitação de amizade.");
            n1.deliver();

            // 7) EXEMPLO DE DENÚNCIA E MODERAÇÃO
            DenunciaCreator denunciaCreator = new DenunciaPostCreator();
            Map<String, Object> contexto = Map.of("post", post1);
            Denuncia denuncia = denunciaCreator.createDenuncia("d1", joao, "post", "conteúdo impróprio", contexto);
            System.out.println("Denúncia criada: " + denuncia.getId() + " por " + denuncia.getReporter().getUsername());

            // Maria (moderadora) analisa a denúncia
            maria.analisarDenuncia(denuncia);

            // 8) ESTADO FINAL (simples)
            System.out.println("\n--- ESTADO ATUAL ---");
            System.out.println("Usuário: " + joao);
            System.out.println("Moderadora: " + maria);
            System.out.println("Post preview: " + post1.preview());
        }
    }
```

## Bibliografia

> Factory Method. Disponível em: <https://refactoring.guru/pt-br/design-patterns/factory-method>.  

> GAMMA, E.; HELM, R.; JOHNSON, R.; VLISSIDES, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.  

> JONATHAN. Padrão Factory Method em Java. Disponível em: <https://www.devmedia.com.br/padrao-de-projeto-factory-method-em-java/26348>.  


## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 05/10/2025  | Criação do esqueleto do documento |[Túlio Augusto Celeri](https://github.com/TulioCeleri) | [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|
| `1.1`  | 05/10/2025  | Criação da introdução, metodologia e Diagrama UML (Factory Method) |[Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
| `1.2`  | 06/10/2025  | Adição da implementação em código do factory method |  [Pedro Ferreira Gondim](https://github.com/G0ndim) e [Túlio Augusto Celeri](https://github.com/TulioCeleri)  |-|-|
