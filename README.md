# 🎓 Exercício Avaliativo 2 - S202

Este projeto implementa um sistema de gerenciamento de professores, escolas e cidades usando Neo4j como banco de dados.

## 🚀 Como Executar

### 1. Configuração do Banco de Dados
Antes de tudo, você precisa configurar o arquivo `Questao1/configuracao.py` com suas credenciais do Neo4j:

```python
DB_URL = "bolt://localhost:7687"  # URL do seu banco Neo4j
DB_USER = "neo4j"                 # Seu usuário
DB_PASSWORD = "sua_senha"         # Sua senha
```

### 2. Iniciar o Neo4j
Execute o Neo4j usando Docker:
```bash
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/sua_senha \
    -d \
    neo4j:latest
```

### 3. Instalar Dependências
```bash
pip install neo4j
```

### 4. Executar o Projeto
```bash
python Questao1/main.py
```

## 📋 Funcionalidades

### Questão 1
- Consulta de professor específico
- Listagem de professores com nome iniciado por 'M'
- Listagem de cidades
- Consulta de escolas por número

### Questão 2
- Cálculo de idade mais jovem e mais velha
- Média de população das cidades
- Consulta de cidade por CEP
- Listagem da terceira letra dos professores

### Questão 3
- CRUD completo de professores
- Interface CLI interativa
- Validações de operações
- Tratamento de erros

## 🛠️ Estrutura do Projeto

```
Questao1/
├── main.py           # Arquivo principal
├── configuracao.py   # Configurações do banco
├── database.py       # Classe de conexão com o banco
├── query.py         # Consultas da Questão 1 e 2
├── setup.py         # Inicialização do banco
├── teacher_crud.py  # CRUD de professores
└── teacher_cli.py   # Interface CLI
```

## 🔍 Comandos do CLI

- `create`: Criar novo professor
- `read`: Consultar professor
- `update`: Atualizar CPF
- `delete`: Remover professor
- `quit`: Sair do programa

## ⚠️ Observações

- Certifique-se de que o Neo4j está rodando antes de executar o programa
- O banco é limpo e reinicializado a cada execução do programa
- Todas as operações CRUD são validadas antes de serem executadas

## 🐛 Troubleshooting

Se encontrar problemas:
1. Verifique se o Neo4j está rodando
2. Confirme se as credenciais em `configuracao.py` estão corretas
3. Verifique se a porta 7687 está disponível
4. Certifique-se de que todas as dependências estão instaladas 