# Padrão Composite

## Introdução  

No contexto do sistema, o padrão **Composite** — um dos padrões estruturais do GoF — é aplicado para **tratar objetos individuais e composições de objetos de forma uniforme**.  
Esse padrão é especialmente útil em cenários onde há **relações hierárquicas parte-todo**, permitindo que operações sejam executadas de maneira recursiva e transparente em toda a estrutura, sem a necessidade de verificar se o elemento é simples (folha) ou composto.

Na aplicação proposta, o Composite é utilizado para gerenciar a **distribuição de atividades linguísticas** (como exercícios, práticas de conversação e testes) tanto para **estudantes individuais** quanto para **grupos de estudo ou turmas**.  

---

## Objetivo

O principal objetivo do padrão **Composite** neste projeto é permitir que o sistema trate **elementos individuais** (`Estudante`) e **estruturas compostas** (`GrupoDeEstudo`) de forma uniforme, facilitando o gerenciamento de atividades linguísticas, práticas e interações.  
Com isso, elimina-se a necessidade de lógica condicional para diferenciar um aluno de um grupo, garantindo que a mesma operação — como iniciar uma prática, atribuir um exercício ou distribuir um conteúdo — possa ser aplicada de maneira homogênea, independentemente da complexidade da estrutura.

Essa abordagem traz os seguintes benefícios ao projeto:
- **Redução do acoplamento** entre as partes do sistema.  
- **Simplificação da lógica** de distribuição de conteúdo.  
- **Escalabilidade** para suportar novos tipos de participantes no futuro.  

### Exemplos práticos de uso no projeto

- **Atividade individual:**  
  Atribuir uma prática de vocabulário específica para um único estudante, permitindo acompanhar seu progresso individualmente.

- **Distribuição em grupo:**  
  Enviar a mesma atividade para uma turma inteira, propagando automaticamente para todos os membros sem necessidade de lógica adicional.

- **Subgrupos específicos:**  
  Criar subgrupos dentro de uma turma (por exemplo, alunos com dificuldades em pronúncia) e atribuir atividades direcionadas apenas a eles.

- **Hierarquia de distribuição:**  
  Atribuir uma tarefa a um grupo principal, garantindo que ela seja repassada a todos os subgrupos e estudantes pertencentes à hierarquia.

- **Expansão e manutenção simples:**  
  Adicionar novos estudantes ou grupos sem alterar a lógica de distribuição, mantendo a escalabilidade e a flexibilidade do sistema.

## Metodologia
O processo de aplicação do padrão **Composite** neste projeto seguiu um fluxo estruturado e iterativo, dividido em várias etapas que combinaram teoria e prática:

1. **Estudo teórico inicial**  
   - O ponto de partida foi o estudo do conteúdo apresentado em aula, com base em materiais e slides fornecidos na disciplina de Arquitetura e Desenho de Software.  
   - A partir dessa etapa, compreendi o conceito central do Composite: **tratar objetos simples e compostos de maneira uniforme** e estruturar sistemas em **árvores hierárquicas**.

2. **Análise de exemplos reais e estudo de casos**  
   - Em seguida, analisei exemplos práticos apresentados pela professora e disponíveis em fontes clássicas como *Design Patterns* (Gamma et al., 1994) e [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/composite).  
   - Essa análise foi essencial para entender como o padrão é aplicado em cenários reais, como gerenciadores de arquivos (arquivos e pastas), sistemas gráficos (elementos e containers) e plataformas de ensino (alunos e turmas).

3. **Compreensão do funcionamento prático através de código**  
   - A partir de exemplos implementados em Java, foi possível observar como cada componente do padrão (Component, Leaf e Composite) se relaciona e como a recursividade é utilizada para propagar ações em toda a hierarquia.  
   - Essa etapa prática ajudou a consolidar a teoria e facilitou a transposição para o contexto do meu projeto.

4. **Mapeamento do domínio do projeto**  
   - Com base no entendimento teórico e prático, o próximo passo foi mapear quais entidades do **Correio Digital** poderiam se beneficiar do Composite.  
   - Foram identificados como candidatos principais:  
     - `Estudante` — representando um usuário individual do sistema.  
     - `GrupoDeEstudo` — representando uma turma ou grupo formado por estudantes e outros subgrupos.

5. **Modelagem da estrutura hierárquica**  
   - Estruturei a interface `ParticipanteDeEstudo` para servir como **Component**, definindo a operação comum `iniciarPratica()`.  
   - Implementei a classe `Estudante` como **Leaf**, responsável por executar a prática individualmente.  
   - Implementei a classe `GrupoDeEstudo` como **Composite**, responsável por propagar a prática para todos os membros da estrutura, inclusive para subgrupos.

6. **Validação e integração ao projeto**  
   - Por fim, a implementação foi testada com uma estrutura hierárquica complexa, contendo múltiplos estudantes, grupos e subgrupos.  
   - A prática foi iniciada a partir do nível mais alto da hierarquia e propagada automaticamente a todos os níveis inferiores, comprovando a eficácia do padrão.

### Resultado da Metodologia

Com esse processo, consegui transformar um conceito teórico em uma solução aplicada ao contexto do projeto, tornando o sistema mais **modular, escalável e de fácil manutenção**.  
A metodologia adotada — que começou com a teoria, passou pela análise de exemplos e culminou com a implementação prática — foi essencial para compreender profundamente o padrão **Composite** e aplicá-lo de forma eficiente ao problema real do sistema.



---

## Aplicação do Padrão no Projeto

A aplicação do padrão seguiu os seguintes passos:  

**1. Identificação dos participantes:**  
Foram identificados os principais elementos que representam participantes do sistema de aprendizado:  
- `Estudante` — elemento básico (Leaf).  
- `GrupoDeEstudo` — elemento composto (Composite) que pode conter estudantes e outros grupos.  

**2. Definição da interface Component:**  
Foi criada a interface `ParticipanteDeEstudo`, que define a operação comum `iniciarPratica(String nomeDaAtividade, String idiomaAlvo)`.

**3. Implementação do Composite e Leaf:**  
- A classe `Estudante` implementa a interface e executa a prática individualmente.  
- A classe `GrupoDeEstudo` implementa a interface e propaga a prática para todos os seus participantes.  

**4. Propagação recursiva:**  
A operação `iniciarPratica` no Composite chama o mesmo método em todos os filhos, permitindo que subgrupos aninhados recebam atividades automaticamente.  

**5. Teste e validação:**  
Um cliente de teste demonstra a criação de uma estrutura hierárquica com estudantes, grupos e subgrupos, executando uma prática única de forma uniforme em toda a hierarquia.

---

## Desenvolvimento

### Component — Interface Base

```java
public interface ParticipanteDeEstudo {
    void iniciarPratica(String nomeDaAtividade, String idiomaAlvo);
}
```

### Leaf — Estudante

```java
import java.util.Objects;

public class Estudante implements ParticipanteDeEstudo {
    private final String nome;

    public Estudante(String nome) {
        this.nome = Objects.requireNonNull(nome, "nome não pode ser nulo");
    }

    @Override
    public void iniciarPratica(String nomeDaAtividade, String idiomaAlvo) {
        System.out.printf("Estudante '%s' iniciou a prática '%s' em '%s'%n",
                nome, nomeDaAtividade, idiomaAlvo);
    }
}
```

### Composite — Grupo de Estudo
```java

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class GrupoDeEstudo implements ParticipanteDeEstudo {
    private final String nomeDoGrupo;
    private final List<ParticipanteDeEstudo> participantes = new ArrayList<>();

    public GrupoDeEstudo(String nomeDoGrupo) {
        this.nomeDoGrupo = Objects.requireNonNull(nomeDoGrupo, "nomeDoGrupo não pode ser nulo");
    }

    public void adicionarParticipante(ParticipanteDeEstudo participante) {
        participantes.add(Objects.requireNonNull(participante, "participante não pode ser nulo"));
    }

    public void removerParticipante(ParticipanteDeEstudo participante) {
        participantes.remove(participante);
    }

    @Override
    public void iniciarPratica(String nomeDaAtividade, String idiomaAlvo) {
        System.out.printf("📚 Grupo '%s' recebeu a prática '%s' em '%s'%n",
                nomeDoGrupo, nomeDaAtividade, idiomaAlvo);
        for (ParticipanteDeEstudo p : participantes) {
            p.iniciarPratica(nomeDaAtividade, idiomaAlvo);
        }
    }
}
```


### Cliente — Demonstração do Uso do Composite
```java

public class ClienteDemo {
    public static void main(String[] args) {
        Estudante ana   = new Estudante("Ana");
        Estudante bruno = new Estudante("Bruno");
        Estudante carla = new Estudante("Carla");
        Estudante diego = new Estudante("Diego");

        GrupoDeEstudo subgrupo = new GrupoDeEstudo("Subgrupo Intensivo");
        subgrupo.adicionarParticipante(carla);
        subgrupo.adicionarParticipante(diego);

        GrupoDeEstudo turma = new GrupoDeEstudo("Turma Espanhol A1");
        turma.adicionarParticipante(ana);
        turma.adicionarParticipante(bruno);
        turma.adicionarParticipante(subgrupo);

        String atividade = "Prática de Conversação";
        String idioma    = "Espanhol Básico";

        turma.iniciarPratica(atividade, idioma);

        System.out.println("\n— Execução isolada —");
        ana.iniciarPratica("Revisão de Vocabulário", "Espanhol Básico");
    }
}

```

## Justificativa de Uso

- O padrão **Composite** elimina a necessidade de condicionais para diferenciar estudantes e grupos.  
- Ele promove **extensibilidade**: novos tipos de participantes podem ser adicionados sem alterar a lógica do cliente.  
- Facilita a **propagação automática** de atividades em estruturas complexas.  
- Alinha-se a práticas reais de **sistemas de aprendizado e plataformas de ensino online**, onde turmas e subgrupos coexistem de forma hierárquica.

---

## Bibliografia
 
- Vídeo Aula: [Aula Composite](
https://unbbr-my.sharepoint.com/personal/mileneserrano_unb_br/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmileneserrano%5Funb%5Fbr%2FDocuments%2FArqDSW%20%2D%20V%C3%ADdeosOriginais%2F09c%20%2D%20Video%2DAula%20%2D%20DSW%20%2D%20GoFs%20%2D%20Estruturais%20%2D%20Composite%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E7746451f%2D540e%2D4b6f%2Da3ea%2D6461ca83d832)

- GAMMA, E. et al. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.  
- Composite. Disponível em: [https://refactoring.guru/pt-br/design-patterns/composite](https://refactoring.guru/pt-br/design-patterns/composite) 
 
- Slides: [Arquitetura e Desenho de Software — Aula GoFs Estruturais — Profa. Milene](https://aprender3.unb.br/pluginfile.php/3178397/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf)

---

## Histórico de Versões
| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 15/10/2025 | Criação do documento e implementação inicial do padrão Composite | [Thales Germano](https://github.com/thalesgvl) | -           |  -  |
| `1.1`  | 15/10/2025 | Adicionando metodologia e correções na bibliografia | [Thales Germano](https://github.com/thalesgvl) | -           |  -  |
