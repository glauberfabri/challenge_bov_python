# Milk Management API

Esta API gerencia fazendas, produções de leite e cálculos de preços baseados em regras de negócio.

## Como Rodar o Projeto

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Acesse a documentação em `http://127.0.0.1:8000/docs`.

## Estrutura do Projeto
- **app/**: Contém a lógica da aplicação.
- **tests/**: Testes unitários e de integração.

## Endpoints Principais
- `POST /api/farmers/`: Cadastro de fazendeiros.
- `POST /api/productions/`: Cadastro de produções.
- `GET /api/price/{farm_id}/{month}`: Preço do litro de leite calculado.