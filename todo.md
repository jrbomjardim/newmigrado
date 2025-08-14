## Plano de Projeto - Sistema de Flashcards

### Fase 1: Configuração inicial do ambiente e repositório GitHub
- [x] Clonar o repositório GitHub.
- [x] Apagar todos os arquivos existentes no repositório.
- [x] Criar e configurar o arquivo `todo.md`.
- [x] Configurar as credenciais do GitHub para push.

### Fase 2: Estruturação do projeto e arquitetura base
- [x] Definir a estrutura de pastas para frontend e backend.
- [x] Escolher e configurar os frameworks (ex: Flask para backend, React para frontend).
- [x] Criar um `README.md` inicial com a arquitetura do projeto.

### Fase 3: Implementação do sistema de autenticação e usuários
- [x] Desenvolver o backend para cadastro e login de usuários.
- [x] Implementar a interface de login moderna com design glassmorphism.
- [x] Adicionar animações e micro-interações na tela de login.
- [x] Implementar validação visual de formulários.
- [x] Adicionar toggle de visualização de senha.
- [x] Configurar período de teste gratuito de 24 horas.
- [x] Implementar sistema de níveis de acesso (usuário e administrador).
- [x] Adicionar contador de tempo de teste no topo do site.

### Fase 4: Implementação do sistema de notificações e ajuste do timer de teste ✅ CONCLUÍDA
- [x] Sistema de notificações no canto superior direito implementado
- [x] Notificações com diferentes tipos (sucesso, erro, aviso, info)
- [x] Animações suaves de entrada e saída das notificações
- [x] Timer de teste ajustado para iniciar apenas após login
- [x] Período de 24 horas iniciando após autenticação do usuário
- [x] Dados do timer salvos no localStorage para persistência
- [x] Sistema de avisos automáticos (1h, 30min, 5min restantes)
- [x] Backup da versão anterior mantido
- [x] Teste completo do sistema funcionando na VPS

### Fase 5: Implementação do dashboard com estatísticas e gráficos ✅ CONCLUÍDA
- [x] Desenvolver a interface do dashboard baseada no design fornecido
- [x] Implementar cards de estatísticas (Cards Estudados, Sequência, Precisão, Meta Diária)
- [x] Criar seção de Ações Rápidas com botões funcionais
- [x] Implementar seção de Atividade Recente com dados mockados
- [x] Integrar timer de teste no header do dashboard
- [x] Configurar navegação entre páginas (Dashboard, Estudar, Meus Cards, Comunidade)
- [x] Aplicar design responsivo e cores gradientes conforme mockup
- [x] Testar dashboard funcionando na VPS

### Fase 6: Implementação do sistema de flashcards
- [ ] Criar backend Flask com banco de dados 
- [ ] Implementar modelos de dados (User, Card, Study Session)
- [ ] Desenvolver APIs REST para CRUD de flashcards
- [ ] Implementar sistema de autenticação real
- [ ] Criar interface de estudo de flashcards
- [ ] Desenvolver sistema de repetição espaçada
- [ ] Integrar frontend com backend via APIs
- [ ] Implementar estatísticas reais baseadas em dados do banco
- [ ] Exibir atividades recentes.
- [ ] Gerar gráfico de progresso semanal.
- [ ] Criar tutorial animado para novos usuários.

### Fase 6: Sistema de flashcards com CRUD completo
- [ ] Desenvolver funcionalidades de criação, edição e exclusão de flashcards.
- [ ] Implementar categorias pré-definidas (Medicina Interna, Cirurgia, Pediatria, Gineco e Obstetriz, Perguntas do Grado).
- [ ] Criar sistema de estudo com animações.
- [ ] Implementar visualização em grade e lista.

### Fase 7: Integração com sistema de pagamento Mercado Pago
- [ ] Integrar com a API do Mercado Pago.
- [ ] Implementar pagamento via PIX e Cartão de Crédito.
- [ ] Configurar plano Premium: R$ 49,99 por 6 meses.
- [ ] Desenvolver interface moderna de pagamento.

### Fase 8: Sistema de funcionalidades sociais (seguir, feed, publicações)
- [ ] Criar funcionalidade para seguir/deixar de seguir outros usuários.
- [ ] Desenvolver um feed de atividades para exibir publicações de usuários seguidos.
- [ ] Implementar sistema de publicações (texto, imagens).
- [ ] Adicionar funcionalidades de curtir e comentar publicações.

### Fase 9: Sistema de perfis e busca de usuários
- [ ] Desenvolver páginas de perfil de usuário com informações relevantes.
- [ ] Criar funcionalidade de busca para encontrar outros usuários pelo nome.
- [ ] Permitir a visualização de perfis de outros usuários.

### Fase 10: Sistema de mensagens privadas
- [ ] Criar sistema de mensagens privadas entre usuários que se seguem.

### Fase 11: Testes, otimizações e deploy na VPS AWS
- [ ] Realizar testes de unidade e integração.
- [ ] Otimizar o desempenho do sistema.
- [ ] Configurar o ambiente de produção na VPS AWS.
- [ ] Realizar o deploy do frontend e backend.

### Fase 12: Documentação final e entrega do projeto
- [ ] Elaborar a documentação técnica do projeto.
- [ ] Preparar um guia de uso para o usuário final.
- [ ] Entregar o projeto completo ao usuário.

