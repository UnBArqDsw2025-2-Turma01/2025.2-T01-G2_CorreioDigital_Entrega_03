# Abstract Factory Pattern - CorreioDigital

Este projeto implementa o padrão **Abstract Factory** para o sistema CorreioDigital, demonstrando como criar famílias de objetos de notificação (E-mail e SMS) de forma flexível e extensível.

##  Estrutura do Projeto

```
abstractfactory/
├── interfaces/           # Interfaces abstratas (AbstractProduct e AbstractFactory)
│   ├── Message.java
│   ├── Sender.java
│   ├── DeliveryService.java
│   └── NotificationFactory.java
├── email/               # Implementações concretas para E-mail
│   ├── EmailMessage.java
│   ├── EmailSender.java
│   ├── EmailDeliveryService.java
│   └── EmailNotificationFactory.java
├── sms/                 # Implementações concretas para SMS
│   ├── SmsMessage.java
│   ├── SmsSender.java
│   ├── SmsDeliveryService.java
│   └── SmsNotificationFactory.java
├── client/              # Cliente do padrão
│   └── NotificationService.java
├── Main.java           # Exemplo de uso
└── README.md           # Este arquivo
```

##  Participantes do Padrão

### AbstractFactory
- **`NotificationFactory`**: Interface que declara métodos para criar produtos abstratos

### ConcreteFactory
- **`EmailNotificationFactory`**: Cria família de produtos para E-mail
- **`SmsNotificationFactory`**: Cria família de produtos para SMS

### AbstractProduct
- **`Message`**: Interface para mensagens
- **`Sender`**: Interface para remetentes
- **`DeliveryService`**: Interface para serviços de envio

### ConcreteProduct
- **Email**: `EmailMessage`, `EmailSender`, `EmailDeliveryService`
- **SMS**: `SmsMessage`, `SmsSender`, `SmsDeliveryService`

### Client
- **`NotificationService`**: Utiliza as interfaces sem conhecer implementações concretas

##  Como Executar

```bash
# Compilar o projeto
javac -cp . Main.java

# Executar o exemplo
java -cp . Main
```

##  Benefícios Demonstrados

1. **Isolamento das Classes Concretas**: O cliente não depende de implementações específicas
2. **Consistência entre Produtos**: Garante que objetos da mesma família sejam compatíveis
3. **Facilidade para Adicionar Novos Canais**: Basta criar nova fábrica e produtos
4. **Baixo Acoplamento**: Cliente depende apenas de interfaces
5. **Alta Coesão**: Responsabilidades bem organizadas

##  Extensibilidade

Para adicionar um novo canal (ex: Push Notification):

1. Criar `PushMessage`, `PushSender`, `PushDeliveryService`
2. Criar `PushNotificationFactory`
3. Usar: `new NotificationService(new PushNotificationFactory())`

**Nenhuma modificação no `NotificationService` é necessária!**

##  Referências

- GAMMA, E. et al. **Padrões de Projeto: Soluções Reutilizáveis de Software Orientado a Objetos**. Bookman, 2000.
- [Refactoring Guru - Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

---
## Histórico de Versões

| Versão | Data       | Descrição  | Autor(es) | Revisor(es) | Detalhes  da revisão |
|--------|-----------|-----------------------------|-----------|-------------|----------|
| `1.0`  | 25/09/2025 | Criação  do documento README. |[Esther Sena](https://github.com/esmsena) | - | - |
