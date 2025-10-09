# Padrão Facade no Projeto

## Introdução  
O padrão Facade é um padrão estrutural que tem como objetivo fornecer uma interface unificada para um conjunto de interfaces em um subsistema [1](https://refactoring.guru/pt-br/design-patterns/facade). Ele define uma camada de abstração que simplifica o uso de componentes complexos, oferecendo ao cliente um ponto de acesso único e intuitivo [2](https://www.devmedia.com.br/padrao-de-projeto-facade-em-java/26476). No contexto do nosso projeto, o Facade foi utilizado para integrar e simplificar as operações relacionadas às principais entidades do sistema (Usuário, Conversa e Postagem). Assim, em vez de o cliente interagir diretamente com cada classe e seus detalhes de implementação, ele passa a utilizar apenas a fachada, tornando o processo mais ágil, seguro e de fácil manutenção.

## Objetivo/Metodologia
O objetivo do uso do Facade neste projeto é simplificar o uso do sistema, fornecendo uma interface única para operações comuns, buscando reduzir o acoplamento entre o cliente e as classes internas do sistema, e também facilitando a manutenção, isolando mudanças internas sem impactar a interface utilizada pelos clientes [3](https://climaco.medium.com/design-pattern-facade-6b0b2220a604).  
Para conseguirmos desenvolver o artefato corretamente atualizamos o [diagrama de classes](https://mermaid.live/view#pako:eNqtV9tu20YQ_RVigQBpKqmS6JoWUQRw7KQIkDRGnL4Uehlxx9QW5K6yuzTcGv6aPAQt0K_Qj3WWF5XLi5Wm1YvImdm5z5nlPUsURxazJANjLgWkGvK1DOj35EkwnU6DC8iBQ8AxON9pNCgt7D_vPynHrATLo8FraVHfQII_mwK0UMF9xXW_b3NlrAb9ATN4o1Ihn37TZ75C5B4d78RG6Ist2Ib8sJajvmUiqR37LngFCRCx4-G1MBZzqJlt9zSmovSh9t1zI-s5TBRVWI8kpEgEeM6W9F2xcY7pK4oRUsz9AKWzeQ0ZHA_wUuX7v6TopX0g21PB40BI26JIlWMcUIhCpi0yZUNkA3Sq8haG6BZsYd7JTEhSt1EqQ5D_NlXIhQX9opNl4JRAJUGf5yL1WRpzdYs-45CoKgtX1Hoi85KwEWogAiqCiYM3VO0fKt5zLx3qVzHGrf2uLI244cp_pBI5SkONIBsv3lbveduPoqppI1KX2PNF3lK3NWc72YJUDLOaJlWS0mnA4yUq34G2ItuWAhYLPpbsRveRSJNay0AVOFh4SSEQjx7RihxbXIogUWiOFGIwwkMXvScdMNot9TD-twCuqtEmM4NRJAVlk4Ppa80dhrbq248w0WIMMqom7LC6bagk3sExTKiGuR8cddDHQhhnZ7BTCOJrnjMy4oIDtQ8EL5Yy9HXYxNFQGsrs9nhfMiBdaC3JBsQw3lZe_4gaJY2Iq5C_wDaZ-ljg8IKAW8jGxipF7ZoxA6tax8ZhnuDFUEj7P50bI1h_ef7O881AdgvaM7spTLl09GvesukD1f-gpunDr1blZeFFITJO8Y-EXbN9Q2h_ovbxa4z2pdtrXeK1W2odn0jjo4GN2OwCZEO_9GDhC201fTNkCzgf7DjOB-Gva8RLr-vCEhzL7m5luXdzm06f-5elSs6_Pzmh-sAY23XZGK_J8Bi_DSBjMt64NtE2QazZYs1KseqpviLEwU4ZUwgnPiT6jJ7KNU6Cbh8mYgePyR52SRw41H5UbQ3LcYB0ZoMZJujkS3Nd4cOSJb3Ubfs_cifqweqazWezZ4dT9UtjPQ7oLl9Uzvu41qocSeV0_9fQyZ4b6F6BG9DwS9vGAL-wnsamu3tau6PWb47ugPxjn01YqgVnsdUFTliOmgafXlk5Q2tmt0g7mcX0yPEGisyu2Vo-0LEdyF-UypuTWhXplsU3kBl6K3Zun9cfQwcRlGT8QhXSsvhsWapg8T27Y_HJajELw-X383B5FobRKjqdsN-IvJjNw8XJ2TxcRcvFabR4mLDfS6PzWXQaRauTKApXyzBahBPmFrvSb-uPMff38Df2ZRhc)
  

Para aplicar o padrão Facade, seguimos os seguintes passos:  
**Identificação das operações principais**: foram selecionadas funcionalidades críticas como criação de usuários, postagem de conteúdos e gerenciamento de conversas.  
**Encapsulamento**: essas funcionalidades foram encapsuladas em classes específicas, já construídas com Builders.  
**Criação da fachada**: foi implementada a classe SistemaFacade, responsável por centralizar o acesso a essas operações, oferecendo métodos simplificados que utilizam os subsistemas internos.  
**Integração**: o cliente agora interage apenas com a SistemaFacade, sem necessidade de lidar com a complexidade dos objetos internos.  

O artefato foi desenvolvido em pares por meio de troca de mensagens no WhatsApp, onde fomos desenvolvendo algumas linhas de código e enviando um ao outro para verificar a qualidade e completude dos códigos. Entrando em consenso também em relação à padronização dos comando, como a autora não possuia tanta familiaridade com Java um estudo anterior teve que ser feito. Os primeiros passos foram selecionar quais eram as classes, em seguida seus conteúdos. O facade foi aplicado apenas em 3 classes, apenas para demonstrar seu desenvolvimento.


## Implementação

```java
public class SistemaFacade {

    public Usuario criarUsuario(String nome, String email, String senha, String bio) {
        return new Usuario.UsuarioBuilder()
                .setNome(nome)
                .setEmail(email)
                .setSenha(senha)
                .setBio(bio)
                .build();
    }

    public Postagem criarPostagem(String conteudo) {
        return new Postagem.PostagemBuilder()
                .setConteudo(conteudo)
                .build();
    }

    public Conversa iniciarConversa(Usuario u1, Usuario u2, String mensagemInicial) {
        return new Conversa.ConversaBuilder()
                .adicionarParticipante(u1)
                .adicionarParticipante(u2)
                .adicionarMensagem(mensagemInicial)
                .build();
    }
}
```
SistemaFacade é a classe fachada que centraliza o acesso às funcionalidades principais do sistema.
Ela oferece três métodos principais:
- criarUsuario() para encapsular a lógica de criação de novos usuários,
- criarPostagem() para facilitar a geração de postagens,
- iniciarConversa() para permitir a criação de conversas entre usuários.

As classes Usuario, Postagem e Conversa representam os subsistemas internos. Elas contêm os atributos e métodos específicos de cada entidade, mas o cliente não precisa interagir diretamente com elas — basta chamar a SistemaFacade. As setas no diagrama mostram a relação de dependência: a fachada utiliza (ou cria) os objetos de cada uma dessas classes, mas mantém a interface de interação simples e unificada para o cliente. Podemos ver a representação desse diagrama abaixo na imagem 1:

**Figura 1:** Diagrama UML Facade  

![Diagrama UML do Facade](../../assets/uml_facade.png)  

**Autores:** [João Pedro Costa](https://github.com/johnaopedro) e [Julia Gabriela](https://github.com/JuliaGabP). 

## Vantagens
- Simplificação da interface;  
- Redução de acoplamento;  
- Melhor organização do código;  
- Flexibilidade de evolução;  
- Facilidade de integração.  

## Desvantagens
- Ocultação excessiva;  
- Aumento indireto da complexidade;  
- Possível dificuldade em testes;  
- Dependência centralizada.  

## Bibliografia

Conjunto de obras consultadas. 

> Facade. Disponível em: <https://refactoring.guru/pt-br/design-patterns/facade>.

> Padrão de Projeto Facade em Java. Disponível em: <https://www.devmedia.com.br/padrao-de-projeto-facade-em-java/26476>.

> CLIMACO, V. Design Pattern: Facade. Disponível em: <https://climaco.medium.com/design-pattern-facade-6b0b2220a604>.

## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 24/09/2025  | Criação do documento, código do facade e diagrama UML|[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)|-|-|
| `1.1`  | 27/09/2025  | Adicionando referências nos respectivos lugares e complementando a metodologia|[Julia Gabriela](https://github.com/JuliaGabP) e [João Pedro Costa](https://github.com/johnaopedro)|-|-|