# Padrão Composite

## Introdução  

No contexto do sistema, o padrão **Composite** — um dos padrões estruturais do GoF — é aplicado para **tratar objetos individuais e composições de objetos de forma uniforme**.  
Esse padrão é especialmente útil em cenários onde há **relações hierárquicas parte-todo**, permitindo que operações sejam executadas de maneira recursiva e transparente em toda a estrutura, sem a necessidade de verificar se o elemento é simples (folha) ou composto.

Na aplicação proposta, o Composite é utilizado para gerenciar a **distribuição de atividades linguísticas** (como exercícios, práticas de conversação e testes) tanto para **estudantes individuais** quanto para **grupos de estudo ou turmas**.  

---

## Objetivo e Justificativa

O objetivo principal do **Composite** é possibilitar que o sistema trate elementos individuais (`Estudante`) e composições de elementos (`GrupoDeEstudo`) da mesma maneira.  
Essa abordagem reduz o acoplamento e simplifica a lógica de distribuição de conteúdo, garantindo que as atividades possam ser iniciadas sem depender da estrutura da hierarquia.

**Exemplos práticos de uso no projeto:**
- Atribuir uma prática de vocabulário a um único estudante.
- Atribuir a mesma prática a uma turma inteira, propagando automaticamente a atividade para todos os membros.
- Criar subgrupos dentro de turmas e distribuir atividades recursivamente.

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
 
Vídeo Aula:
[Aula Composite](
https://unbbr-my.sharepoint.com/personal/mileneserrano_unb_br/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmileneserrano%5Funb%5Fbr%2FDocuments%2FArqDSW%20%2D%20V%C3%ADdeosOriginais%2F09c%20%2D%20Video%2DAula%20%2D%20DSW%20%2D%20GoFs%20%2D%20Estruturais%20%2D%20Composite%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E7746451f%2D540e%2D4b6f%2Da3ea%2D6461ca83d832)

- GAMMA, E. et al. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.  
- Composite. Disponível em: [https://refactoring.guru/pt-br/design-patterns/composite](https://refactoring.guru/pt-br/design-patterns/composite) 
 
- Slides: [Arquitetura e Desenho de Software — Aula GoFs Estruturais — Profa. Milene](https://aprender3.unb.br/pluginfile.php/3178397/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Estruturais%20-%20Profa.%20Milene.pdf)

---

## Histórico de Versões
| Versão |     Data    | Descrição   | Autor(es) | Revisor(es) | Detalhes da revisão | 
| ------ | ----------- | ----------- | --------- | ----------- | --------------------|
| `1.0`  | 15/10/2025 | Criação do documento e implementação inicial do padrão Composite | [Thales Germano](https://github.com/thalesgvl) | -           |  -  |
