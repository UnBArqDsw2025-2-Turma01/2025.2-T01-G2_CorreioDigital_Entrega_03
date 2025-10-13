# Padrão Decorator no Projeto

## Introdução  

O **Decorator** é um padrão de projeto estrutural da UML que permite **adicionar funcionalidades a objetos de forma dinâmica**, sem modificar sua estrutura original.  

No contexto deste projeto, ele foi aplicado ao módulo de **Chat**, possibilitando que uma mensagem básica seja enriquecida progressivamente com novos comportamentos, de acordo com as necessidades do usuário.  

Em vez de criar diversas subclasses específicas para cada tipo de mensagem (como mensagens com emoji, com anexo, criptografadas ou formatadas), utilizamos **decoradores encadeáveis** que ampliam as capacidades da mensagem original de forma flexível e modular.  

Com essa abordagem, conseguimos:  
- **Reuso de código**: reaproveitar a mensagem base sem duplicação.  
- **Extensibilidade**: adicionar novas funcionalidades sem alterar classes existentes.  
- **Composição dinâmica**: combinar múltiplos recursos (emoji + anexo + criptografia + formatação).  

 Assim, o uso do Decorator garante que o sistema de mensagens seja **flexível, escalável e aderente a boas práticas de Arquitetura e Desenho de Software**.

## Objetivo/Metodologia

O objetivo da aplicação do padrão **Decorator** neste projeto é possibilitar a **extensão dinâmica das funcionalidades do módulo de Chat**, garantindo que novas capacidades possam ser incorporadas às mensagens sem a necessidade de alterar a estrutura das classes originais.  
Essa abordagem visa promover **flexibilidade, reuso de código e escalabilidade**, aspectos essenciais para manter a qualidade do software e atender aos requisitos evolutivos do sistema de comunicação entre usuários. 

Para a construção desta solução, seguimos as seguintes etapas metodológicas:  

1. **Identificação da entidade principal**  
   - O objeto central é a classe `Mensagem`, que representa uma mensagem simples enviada entre usuários.  

2. **Definição de uma abstração base**  
   - Foi criada a interface `Mensagem` e a classe concreta `MensagemSimples`, responsável por representar o conteúdo básico do chat.  

3. **Criação do Decorador Abstrato**  
   - Implementamos a classe `MensagemDecorator`, responsável por servir como camada intermediária para a extensão de comportamentos, mantendo a aderência ao princípio **Open/Closed** (OCP).  

4. **Desenvolvimento dos Decoradores Concretos**  
   - Foram adicionadas especializações que representam funcionalidades adicionais:  
     - `MensagemComEmoji`  
     - `MensagemComAnexo`  
     - `MensagemCriptografada`  
     - `MensagemFormatada`  

5. **Encadeamento de Decoradores**  
   - As mensagens podem ser combinadas de forma incremental, permitindo que uma mensagem simples seja enriquecida com múltiplos recursos de maneira **modular e configurável**.  

Assim, a metodologia adotada garante que o sistema de mensagens permaneça **extensível e adaptável**, em conformidade com os princípios da **Arquitetura e Desenho de Software**, além de favorecer a manutenção a longo prazo.

## Implementação

## Vantagens

## Desvantagens

## Bibliografia

## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 11/10/2025  | Criação do esqueleto do documento | [Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
| `1.1`  | 13/10/2025  | Criação da introdução e metodologia | [Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|
