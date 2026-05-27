# 🎬 CineReview API

Sistema completo de catálogo e avaliações de filmes desenvolvido com FastAPI, MongoDB, autenticação JWT e frontend moderno responsivo.

---

# 📌 Sobre o Projeto

O CineReview é uma aplicação full stack desenvolvida para gerenciamento de filmes e avaliações cinematográficas.

O sistema permite:

- cadastro de usuários
- autenticação JWT
- controle de acesso por perfil
- gerenciamento completo de filmes
- gerenciamento de avaliações
- frontend moderno responsivo
- testes unitários
- aplicação de princípios SOLID
- dockerização completa da aplicação

---

# 🚀 Funcionalidades

## ✅ CRUD de Filmes

- Criar filmes
- Listar filmes
- Buscar filme por ID
- Atualizar filmes
- Deletar filmes

---

## ✅ CRUD de Avaliações

- Criar avaliações
- Listar avaliações
- Buscar avaliação por ID
- Atualizar avaliações
- Deletar avaliações

---

## ✅ Sistema de Autenticação JWT

- Registro de usuários
- Login
- Geração de token JWT
- Expiração de token
- Rotas protegidas

---

## ✅ Controle de Acesso (RBAC)

Perfis disponíveis:

- `admin`
- `usuario`

### Permissões

- Administradores podem editar e deletar registros
- Usuários comuns possuem acesso limitado

---

## ✅ Frontend Moderno

Interface desenvolvida com:

- Interface moderna baseada em Glassmorphism
- animações suaves
- layout responsivo
- dashboard administrativa
- telas modernas de login e cadastro
- tema cinematográfico

---

# 🛠️ Tecnologias Utilizadas

## Backend

- Python
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- JWT
- python-jose
- Passlib
- bcrypt
- Uvicorn

---

## Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome

---

## Testes

- Pytest

---

## Docker

- Docker
- Docker Compose
- MongoDB Container
- Python Container

---

# 📂 Estrutura do Projeto

```txt
trabalho-pratico-semestral/
│
├── docker-compose.yml
│
├── backend/
│   │
│   ├── Dockerfile
│   │
│   ├── dependencies/
│   │   └── auth_dependency.py
│   │
│   ├── models/
│   │   ├── filme_model.py
│   │   ├── avaliacao_model.py
│   │   └── usuario_model.py
│   │
│   ├── routes/
│   │   ├── filmes_routes.py
│   │   ├── avaliacoes_routes.py
│   │   └── auth_routes.py
│   │
│   ├── tests/
│   │   └── test_filmes.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── index.html
│   ├── cadastro.html
│   ├── dashboard.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── login.js
│       ├── cadastro.js
│       └── script.js
│
├── SOLID.md
├── .gitignore
└── README.md
```

---

# ⚙️ Como Executar o Projeto Localmente

# 1️⃣ Clonar o repositório

```bash
git clone https://github.com/PimentelJ05/trabalho-pratico-semestral.git
```

---

# 2️⃣ Entrar na pasta do projeto

```bash
cd trabalho-pratico-semestral
```

---

# 3️⃣ Entrar no backend

```bash
cd backend
```

---

# 4️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

# 5️⃣ Ativar ambiente virtual

## Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

# 6️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 7️⃣ Executar o servidor

```bash
python -m uvicorn main:app --reload
```

---

# 🐳 Executando com Docker

## Pré-requisitos

- Docker Desktop instalado

---

## Executar containers

Na raiz do projeto:

```bash
docker compose up --build
```

---

## Acessos

### Backend

```txt
http://localhost:8000
```

### Swagger

```txt
http://localhost:8000/docs
```

---

## Containers utilizados

- FastAPI
- MongoDB
- Docker Compose

---

# 🌐 Endpoints

## API

```txt
http://127.0.0.1:8000
```

---

## Swagger

```txt
http://127.0.0.1:8000/docs
```

---

# 💻 Executando o Frontend

1. Abra a pasta `frontend` no VSCode

2. Instale a extensão:

```txt
Live Server
```

3. Clique com botão direito em:

```txt
index.html
```

4. Clique em:

```txt
Open with Live Server
```

---

# 🔐 Autenticação JWT

Após realizar login:

```txt
POST /auth/login
```

o sistema retorna:

```json
{
  "access_token": "TOKEN_JWT",
  "token_type": "bearer"
}
```

---

# 🔒 Rotas Protegidas

Para acessar rotas protegidas:

```txt
Authorization: Bearer SEU_TOKEN
```

---

# 👥 Usuários de Teste

## Administrador

```json
{
  "nome": "Júlia Admin",
  "email": "admin@cinereview.com",
  "senha": "123456",
  "perfil": "admin"
}
```

---

## Usuário Comum

```json
{
  "nome": "Carlos Silva",
  "email": "carlos@email.com",
  "senha": "123456",
  "perfil": "usuario"
}
```

---

# 🧪 Executando os Testes

```bash
pytest
```

---

# ✅ Cenários Testados

## Sucesso

- Criação de filme válido
- Busca de filme existente

---

## Erro

- Filme sem título
- Busca de filme inexistente

---

# 🧠 Princípios SOLID Aplicados

Os princípios SOLID utilizados no projeto estão documentados no arquivo:

```txt
SOLID.md
```

---

# 📌 Princípios Aplicados

## S — Single Responsibility Principle

Separação de responsabilidades entre:

- rotas
- autenticação
- dependências
- modelos

---

## O — Open/Closed Principle

Os modelos e rotas podem ser estendidos sem modificar a estrutura principal.

---

## D — Dependency Inversion Principle

As regras de autenticação foram desacopladas das rotas utilizando dependências do FastAPI.

---

# 🎨 Características do Frontend

- Responsivo
- Interface moderna baseada em Glassmorphism
- Sidebar moderna
- Cards animados
- Dashboard administrativa
- Tela de login
- Tela de cadastro
- Tema cinematográfico

---

# 📚 Funcionalidades Extras

✅ JWT  
✅ RBAC  
✅ Testes Unitários  
✅ SOLID  
✅ Frontend Responsivo  
✅ Dashboard Moderna  
✅ Swagger  
✅ MongoDB  
✅ Docker  
✅ Docker Compose  

---

# 📖 Documentação

A documentação interativa da API pode ser acessada via Swagger:

```txt
http://localhost:8000/docs
```

---

# 👩‍💻 Desenvolvedores

- Júlia Carla Ferreira Pimentel

---

# 🚀 Status do Projeto

✅ Projeto Finalizado  
✅ Backend Completo  
✅ Frontend Completo  
✅ Autenticação JWT  
✅ Controle de Acesso  
✅ Testes Unitários  
✅ SOLID  
✅ Responsivo  
✅ Dockerizado  
✅ Swagger  
