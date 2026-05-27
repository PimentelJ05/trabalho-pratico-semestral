````md
# 🎬 CineReview API

Sistema completo de catálogo e avaliações de filmes desenvolvido com FastAPI, MongoDB e frontend moderno responsivo.

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

Permissões:
- Administradores podem editar/deletar filmes
- Usuários comuns possuem acesso limitado

---

## ✅ Frontend Moderno

Interface desenvolvida com:
- glassmorphism
- animações
- layout responsivo
- efeitos modernos
- dashboard administrativa

---

# 🛠️ Tecnologias Utilizadas

## Backend
- Python
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- JWT
- Passlib
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

# 📂 Estrutura do Projeto

```txt
trabalho-pratico-semestral/
│
├── backend/
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
│   │   └── styles.css
│   │
│   └── js/
│       ├── login.js
│       ├── cadastro.js
│       └── script.js
│
├── SOLID.md
├── .gitignore
└── README.md
````

---

# ⚙️ Como Executar o Projeto

# 1️⃣ Clonar o repositório

```bash
git clone https://github.com/PimentelJ05/trabalho-pratico-semestral.git
```

---

# 2️⃣ Entrar na pasta backend

```bash
cd backend
```

---

# 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

# 4️⃣ Ativar ambiente virtual

## Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

# 5️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 6️⃣ Executar o servidor

```bash
python -m uvicorn main:app --reload
```

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

* Live Server

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

* Criação de filme válido
* Busca de filme existente

## Erro

* Filme sem título
* Busca de filme inexistente

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

* rotas
* autenticação
* dependências
* modelos

---

## O — Open/Closed Principle

Os modelos e rotas podem ser estendidos sem modificar a estrutura principal.

---

## D — Dependency Inversion Principle

As regras de autenticação foram desacopladas das rotas usando dependências do FastAPI.

---

# 🎨 Características do Frontend

* Responsivo
* Glassmorphism
* Sidebar moderna
* Cards animados
* Dashboard administrativa
* Tela de login
* Tela de cadastro
* Tema cinematográfico

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

---

# 👩‍💻 Desenvolvedores

* Júlia Carla Ferreira Pimentel

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

```
```
