# Guia de Continuidade para Instâncias da MANUS

## 📋 Como Continuar o Projeto

### 1. Arquivo Principal de Referência
**`todo.md`** - Este é o arquivo mais importante para entender o estado atual do projeto.
- Contém todas as fases do projeto
- Mostra tarefas concluídas [x] e pendentes [ ]
- Indica exatamente onde o projeto parou

### 2. Arquivos Complementares
- **`README.md`** - Arquitetura geral e tecnologias utilizadas
- **`docs/vps-config.md`** - Configurações da VPS e comandos de deploy
- **`.env.example`** - Variáveis de ambiente necessárias

### 3. Estado Atual do Projeto
**Fase Atual**: 4 - Desenvolvimento da interface moderna com glassmorphism
**Última Fase Concluída**: 3 - Implementação do sistema de autenticação e usuários

### 4. Informações Técnicas Importantes

#### Repositório GitHub
- **URL**: https://github.com/jrbomjardim/newmigrado.git
- **Branch principal**: master
- **Credenciais**: Usar token clássico do GitHub fornecido pelo usuário

#### VPS AWS
- **IP**: 56.125.6.182
- **Usuário**: ubuntu
- **Chave SSH**: servidormigrado.pem (fornecida pelo usuário)
- **Diretório do projeto**: /home/ubuntu/newmigrado

#### Estrutura do Projeto
```
newmigrado/
├── frontend/          # React + TailwindCSS + Shadcn/ui
├── backend/           # Flask + SQLAlchemy + PostgreSQL
├── docs/              # Documentação
├── tests/             # Testes automatizados
├── todo.md            # ⭐ ARQUIVO PRINCIPAL DE REFERÊNCIA
├── README.md          # Arquitetura geral
└── CONTINUIDADE.md    # Este arquivo
```

### 5. Tecnologias Configuradas
- **Frontend**: React 18, TailwindCSS, Shadcn/ui, Lucide Icons, Recharts
- **Backend**: Flask, SQLAlchemy, PostgreSQL, CORS habilitado
- **Deploy**: VPS AWS com Nginx
- **Banco**: PostgreSQL configurado na VPS

### 6. Próximos Passos (Conforme todo.md)
1. Ler o arquivo `todo.md` para identificar tarefas pendentes
2. Verificar a fase atual e suas tarefas não concluídas
3. Continuar o desenvolvimento a partir da próxima tarefa marcada como [ ]

### 7. Comandos Úteis para Continuidade

#### Conectar à VPS
```bash
ssh -i servidormigrado.pem ubuntu@56.125.6.182
```

#### Atualizar código na VPS
```bash
cd /home/ubuntu/newmigrado
git pull origin master
```

#### Testar Backend
```bash
cd /home/ubuntu/newmigrado/backend
source venv/bin/activate
python src/main.py
```

#### Testar Frontend
```bash
cd /home/ubuntu/newmigrado/frontend
npm run dev
```

### 8. Credenciais Importantes
- **Mercado Pago**: Configurar no arquivo .env (credenciais fornecidas pelo usuário)
- **PostgreSQL**: Usuário `flashcards_user` já configurado na VPS
- **GitHub**: Token clássico fornecido pelo usuário

### ⚠️ IMPORTANTE
- Sempre ler o `todo.md` primeiro para entender o estado atual
- Não pular fases - seguir a sequência estabelecida
- Fazer commits frequentes com mensagens descritivas
- Testar localmente antes de fazer deploy na VPS

