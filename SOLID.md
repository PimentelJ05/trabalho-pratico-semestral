# Aplicação dos Princípios SOLID

## S — Single Responsibility Principle

Arquivo:
- `routes/filmes_routes.py`

Aplicação:
As rotas possuem apenas responsabilidade de controlar as requisições HTTP relacionadas aos filmes.

---

## O — Open/Closed Principle

Arquivo:
- `models/filme_model.py`

Aplicação:
Os modelos podem ser estendidos com novos atributos sem modificar a estrutura principal da aplicação.

---

## D — Dependency Inversion Principle

Arquivo:
- `dependencies/auth_dependency.py`

Aplicação:
As dependências de autenticação foram separadas das rotas principais, desacoplando regras de autenticação da lógica de negócio.