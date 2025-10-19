# Padrão Strategy

## 1. Introdução

O padrão de projeto **Strategy** é um padrão comportamental que tem como objetivo definir uma família de algoritmos, encapsulá-los de forma independente e torná-los intercambiáveis durante a execução de um sistema. Esse padrão é amplamente utilizado quando existe a necessidade de oferecer diferentes comportamentos para uma mesma funcionalidade, sem que seja preciso alterar o código da classe principal que utiliza esses comportamentos. Em essência, o Strategy promove a separação entre **a lógica do contexto** e **as estratégias de execução**, permitindo que o sistema seja facilmente extensível e configurável conforme diferentes cenários [1](https://refactoring.guru/pt-br/design-patterns/strategy).  

Outra característica importante é que o Strategy favorece a aplicação do **Princípio do Aberto/Fechado (OCP)**, já que novos algoritmos podem ser adicionados sem modificar o código existente. Além disso, esse padrão incentiva a utilização da **composição ao invés da herança**, promovendo maior flexibilidade e reduzindo o acoplamento entre os componentes [2](https://www.devmedia.com.br/estudo-e-aplicacao-do-padrao-de-projeto-strategy/25856).  

No contexto de sistemas orientados a objetos, o Strategy é bastante aplicável em casos como ordenação de elementos, cálculos de tarifas, processamento de pagamentos, algoritmos de recomendação e até moderação de conteúdo em plataformas digitais. Assim, ele representa uma solução robusta e elegante para a manutenção e evolução de softwares complexos [3](https://www-digitalocean-com.translate.goog/community/tutorials/strategy-design-pattern-in-java-example-tutorial?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true).

## 2. Metodologia

A aplicação do padrão **Strategy** neste projeto foi conduzida a partir da identificação de pontos do sistema onde a flexibilidade de comportamento era essencial. Foram analisadas funcionalidades como a moderação de postagens e usuários, a ordenação de posts por diferentes critérios, a entrega de mensagens (imediata ou agendada) e a forma de envio de notificações. Em cada um desses casos, observou-se que existiam múltiplas formas de execução possíveis, o que justificou a adoção desse padrão [1](https://refactoring.guru/pt-br/design-patterns/strategy).  

A metodologia consistiu, primeiramente, na criação de **interfaces abstratas** representando as estratégias genéricas. Em seguida, foram implementadas classes concretas que encapsulam comportamentos específicos, como `ModeracaoPostStrategy` e `ModeracaoUsuarioStrategy`, ou ainda `OrdenarPorLikes` e `OrdenarPorData`. Por fim, as classes principais (como `Usuario`, `Moderador` e `Mensagem`) foram adaptadas apenas para permitir a utilização dessas estratégias, sem que houvesse necessidade de alterar sua lógica interna.  

Dessa forma, garantiu-se que o projeto mantivesse alta **coesão interna** e baixo **acoplamento externo**, princípios fundamentais da Arquitetura de Software. O processo de escolha e aplicação das estratégias foi guiado por reuniões de grupo, discussões sobre casos de uso práticos e pelo critério de reduzir a complexidade de manutenção futura, garantindo que o código possa ser expandido de forma incremental e sustentável [3](https://www-digitalocean-com.translate.goog/community/tutorials/strategy-design-pattern-in-java-example-tutorial?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true).

## Implementação


### Estrutura Base


### Exemplo de Uso no Sistema


### Diagrama UML da Implementação

**Figura 1:** Diagrama UML Padrão Strategy  

![Diagrama UML Strategy](../../Assets/strategy.png)

## Considerações de Projeto


### Vantagens Obtidas no CorreioDigital


### Pontos de Atenção


## Conclusão


## Bibliografia

1. Refactoring.Guru. *Padrão Strategy*. Disponível em: [https://refactoring.guru/pt-br/design-patterns/strategy](https://refactoring.guru/pt-br/design-patterns/strategy). Acesso em: 19 out. 2025.  
2. DevMedia. *Padrão de Projeto Strategy em Java*. Disponível em: [https://www.devmedia.com.br/estudo-e-aplicacao-do-padrao-de-projeto-strategy/25856](https://www.devmedia.com.br/estudo-e-aplicacao-do-padrao-de-projeto-strategy/25856). Acesso em: 19 out. 2025.  
3. DigitalOcean. *Strategy Design Pattern in Java*. Disponível em: [https://www-digitalocean-com.translate.goog/community/tutorials/strategy-design-pattern-in-java-example-tutorial?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true](https://www-digitalocean-com.translate.goog/community/tutorials/strategy-design-pattern-in-java-example-tutorial?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true). Acesso em: 19 out. 2025.  

## Histórico de Versões

| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 19/10/2025 | Criação do esqueleto do documento |[Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim)|-|-|
| `1.1`  | 19/10/2025 | Criação da introdução, metodogia e diagrama UML do padrão strategy |[Túlio Augusto Celeri](https://github.com/TulioCeleri) e [Pedro Ferreira Gondim](https://github.com/G0ndim)|-|-|
