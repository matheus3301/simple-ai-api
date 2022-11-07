# Teste Tensorflow Lite + HTTP no Raspberry 4 

## Conectando Via SSH Localmente

1 - Descobrir o IP do Raspberry na rede usando mDNS
```
ping raspberrypi.local
```

2 - Conectar via ssh (usuário e senha: pi)
```
ssh pi@<ip_raspberry>
```

## Instalando e Resolvendo as dependências

Usando o terminal SSH:

1 - Clonar repositório
```
git clone https://github.com/matheus3301/simple-ai-api.git
```

2 - Entrar no repositório
```
cd simple-ai-api
```

3 - Criar ambiente virtual e instalar as dependências
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Executando
Para rodar o servidor flask, é necessário primeiramente configurar algumas variáveis de ambiente:

1 - Configurar variável de ambiente
```
export FLASK_APP=api.py
```

2 - Rodar o servidor
```
flask run --host=0.0.0.0
```
a flag --host serve para habilitar o acesso remoto ao servidor