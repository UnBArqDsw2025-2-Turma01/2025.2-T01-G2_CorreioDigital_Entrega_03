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





### Usuário





#### Exemplo de Uso






### Postagem




#### Exemplo de Uso




### Conversa




#### Exemplo de Uso




## Bibliografia

> Factory Method. Disponível em: <https://refactoring.guru/pt-br/design-patterns/factory-method>.  

> GAMMA, E.; HELM, R.; JOHNSON, R.; VLISSIDES, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.  

> JONATHAN. Padrão Factory Method em Java. Disponível em: <https://www.devmedia.com.br/padrao-de-projeto-factory-method-em-java/26348>.  


## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 05/10/2025  | Criação do esqueleto do documento |[Túlio Augusto Celeri](https://github.com/TulioCeleri) | [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|
| `1.1`  | 05/10/2025  | Criação da introdução, metodologia e Diagrama UML (Factory Method) |[Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim) |-|-|