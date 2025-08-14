# Configurações da VPS

## Informações de Acesso

- **IP da VPS**: 56.125.6.182
- **Chave SSH**: servidormigrado.pem
- **Usuário**: ubuntu (padrão AWS)

## Comandos de Acesso

### Conectar via SSH
```bash
ssh -i servidormigrado.pem ubuntu@56.125.6.182
```

### Transferir arquivos (SCP)
```bash
# Enviar arquivo para VPS
scp -i servidormigrado.pem arquivo.txt ubuntu@56.125.6.182:/home/ubuntu/

# Baixar arquivo da VPS
scp -i servidormigrado.pem ubuntu@56.125.6.182:/home/ubuntu/arquivo.txt ./
```

### Transferir diretório completo (rsync)
```bash
# Sincronizar projeto local com VPS
rsync -avz -e "ssh -i servidormigrado.pem" ./migradonew/ ubuntu@56.125.6.182:/home/ubuntu/migradonew/
```

## Configuração do Ambiente de Produção

### Dependências do Sistema
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm nginx postgresql postgresql-contrib
```

### Configuração do Banco PostgreSQL
```bash
sudo -u postgres createuser --interactive
sudo -u postgres createdb flashcards_db
```

### Configuração do Nginx
```bash
sudo systemctl enable nginx
sudo systemctl start nginx
```

### Configuração do Firewall
```bash
sudo ufw allow 22      # SSH
sudo ufw allow 80      # HTTP
sudo ufw allow 443     # HTTPS
sudo ufw enable
```

## Deploy do Projeto

### 1. Transferir arquivos
```bash
rsync -avz -e "ssh -i servidormigrado.pem" --exclude 'node_modules' --exclude '.git' ./migradonew/ ubuntu@56.125.6.182:/home/ubuntu/migradonew/
```

### 2. Configurar Backend (Flask)
```bash
ssh -i servidormigrado.pem ubuntu@56.125.6.182
cd /home/ubuntu/migradonew/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar Frontend (React)
```bash
cd /home/ubuntu/migradonew/frontend
npm install
npm run build
```

### 4. Configurar Nginx
```bash
sudo cp /home/ubuntu/migradonew/docs/nginx.conf /etc/nginx/sites-available/migrado
sudo ln -s /etc/nginx/sites-available/migrado /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 5. Configurar Systemd Service
```bash
sudo cp /home/ubuntu/migradonew/docs/migrado.service /etc/systemd/system/
sudo systemctl enable migrado
sudo systemctl start migrado
```

## Monitoramento

### Verificar status dos serviços
```bash
sudo systemctl status nginx
sudo systemctl status migrado
sudo systemctl status postgresql
```

### Logs da aplicação
```bash
sudo journalctl -u migrado -f
```

### Logs do Nginx
```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

