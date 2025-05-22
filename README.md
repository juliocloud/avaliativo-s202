# Exercício Avaliativo 2 - S202

Sistema de gerenciamento de professores, escolas e cidades usando Neo4j.

## Como Executar

### 1. Configuração do Banco
Primeiro, configure o arquivo `Questao1/configuracao.py` com suas credenciais do Neo4j:

```python
DB_URL = "bolt://localhost:7687"  # URL do seu banco Neo4j
DB_USER = "neo4j"                 # Seu usuário
DB_PASSWORD = "sua_senha"         # Sua senha
```

### 2. Neo4j
Rode o Neo4j via Docker:
```bash
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/sua_senha \
    -d \
    neo4j:latest
```

### 3. Dependências
```bash
pip install neo4j
```

### 4. Rodar
```bash
python Questao1/main.py
```

## O que tem aqui?

### Questão 1
- Busca de professor específico
- Professores com nome começando em 'M'
- Lista de cidades
- Escolas por número

### Questão 2
- Idade mais jovem e mais velha
- Média de população das cidades
- Cidade por CEP
- Terceira letra dos professores

### Questão 3
- CRUD de professores
- CLI interativa
- Validações
- Tratamento de erros

## Estrutura

```
Questao1/
├── main.py           # Principal
├── configuracao.py   # Config do banco
├── database.py       # Conexão
├── query.py         # Queries Q1 e Q2
├── setup.py         # Setup do banco
├── teacher_crud.py  # CRUD
└── teacher_cli.py   # CLI
```

## Comandos do CLI

- `create`: Novo professor
- `read`: Buscar professor
- `update`: Atualizar CPF
- `delete`: Remover professor
- `quit`: Sair

## Dicas

- Neo4j precisa estar rodando
- Banco é resetado a cada execução
- Operações CRUD são validadas

## Se der problema

1. Neo4j rodando?
2. Credenciais corretas?
3. Porta 7687 livre?
4. Dependências instaladas?
