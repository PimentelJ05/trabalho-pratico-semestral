const API_URL = "http://127.0.0.1:8000";

const token = localStorage.getItem("token");

if (!token) {
  window.location.href = "index.html";
}

const listaFilmes = document.getElementById("lista-filmes");
const listaAvaliacoes = document.getElementById("lista-avaliacoes");
const formFilme = document.getElementById("form-filme");
const formAvaliacao = document.getElementById("form-avaliacao");

let filmeEditandoId = null;
let avaliacaoEditandoId = null;

function getHeaders() {
  return {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${token}`
  };
}

function mostrarTela(tela) {

  document.querySelectorAll(".tela").forEach((secao) => {
    secao.classList.remove("ativa");
  });

  document.querySelectorAll(".nav-btn").forEach((botao) => {
    botao.classList.remove("active");
  });

  document.getElementById(`tela-${tela}`).classList.add("ativa");

  const botao = document.querySelector(`[data-tela="${tela}"]`);

  if (botao) {
    botao.classList.add("active");
  }

  lucide.createIcons();
}

async function listarFilmes() {

  try {

    const resposta = await fetch(`${API_URL}/filmes/`, {
      headers: getHeaders()
    });

    const filmes = await resposta.json();

    listaFilmes.innerHTML = "";

    filmes.forEach((filme) => {

      const card = document.createElement("article");

      card.className = "card";

      card.innerHTML = `
        <h3>🎬 ${filme.titulo}</h3>

        <p>
          <strong>Gênero:</strong>
          ${filme.genero}
        </p>

        <p>
          <strong>Ano:</strong>
          ${filme.ano}
        </p>

        <p>
          <strong>Diretor:</strong>
          ${filme.diretor}
        </p>

        <p>
          <strong>Descrição:</strong>
          ${filme.descricao}
        </p>

        <span class="id">
          ID: ${filme.id}
        </span>

        <div class="acoes-card">

          <button class="btn-editar">
            <i data-lucide="edit"></i>
            Editar
          </button>

          <button class="btn-excluir">
            <i data-lucide="trash"></i>
            Excluir
          </button>

          <button class="btn-avaliacoes">
            <i data-lucide="message-circle"></i>
            Avaliações
          </button>

        </div>
      `;

      card
        .querySelector(".btn-editar")
        .addEventListener("click", () => editarFilme(filme));

      card
        .querySelector(".btn-excluir")
        .addEventListener("click", () => deletarFilme(filme.id));

      card
        .querySelector(".btn-avaliacoes")
        .addEventListener("click", () => verAvaliacoesDoFilme(filme.id));

      listaFilmes.appendChild(card);
    });

    lucide.createIcons();

  } catch (erro) {

    console.error(erro);

    listaFilmes.innerHTML = `
      <p>Erro ao carregar filmes 😭</p>
    `;
  }
}

function editarFilme(filme) {

  filmeEditandoId = filme.id;

  document.getElementById("titulo").value = filme.titulo;
  document.getElementById("descricao").value = filme.descricao;
  document.getElementById("genero").value = filme.genero;
  document.getElementById("ano").value = filme.ano;
  document.getElementById("diretor").value = filme.diretor;
  document.getElementById("poster_url").value = filme.poster_url || "";

  mostrarTela("novo-filme");
}

async function deletarFilme(id) {

  const confirmar = confirm(
    "Tem certeza que deseja excluir este filme?"
  );

  if (!confirmar) return;

  await fetch(`${API_URL}/filmes/${id}`, {
    method: "DELETE",
    headers: getHeaders()
  });

  listarFilmes();
}

formFilme.addEventListener("submit", async (event) => {

  event.preventDefault();

  const filme = {
    titulo: document.getElementById("titulo").value,
    descricao: document.getElementById("descricao").value,
    genero: document.getElementById("genero").value,
    ano: Number(document.getElementById("ano").value),
    diretor: document.getElementById("diretor").value,
    poster_url: document.getElementById("poster_url").value
  };

  if (filmeEditandoId) {

    await fetch(`${API_URL}/filmes/${filmeEditandoId}`, {
      method: "PUT",
      headers: getHeaders(),
      body: JSON.stringify(filme)
    });

    filmeEditandoId = null;

  } else {

    await fetch(`${API_URL}/filmes/`, {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify(filme)
    });
  }

  formFilme.reset();

  mostrarTela("filmes");

  listarFilmes();
});

async function listarAvaliacoes() {

  const resposta = await fetch(`${API_URL}/avaliacoes/`, {
    headers: getHeaders()
  });

  const avaliacoes = await resposta.json();

  renderizarAvaliacoes(avaliacoes);
}

function renderizarAvaliacoes(avaliacoes) {

  listaAvaliacoes.innerHTML = "";

  avaliacoes.forEach((avaliacao) => {

    const card = document.createElement("article");

    card.className = "card";

    card.innerHTML = `
      <h3>⭐ Nota ${avaliacao.nota}/5</h3>

      <p>
        <strong>Usuário:</strong>
        ${avaliacao.usuario}
      </p>

      <p>
        <strong>Comentário:</strong>
        ${avaliacao.comentario}
      </p>

      <span class="id">
        Filme ID: ${avaliacao.filme_id}
      </span>

      <div class="acoes-card">

        <button class="btn-editar-avaliacao">
          <i data-lucide="edit"></i>
          Editar
        </button>

        <button class="btn-excluir-avaliacao">
          <i data-lucide="trash"></i>
          Excluir
        </button>

      </div>
    `;

    card
      .querySelector(".btn-editar-avaliacao")
      .addEventListener("click", () => editarAvaliacao(avaliacao));

    card
      .querySelector(".btn-excluir-avaliacao")
      .addEventListener("click", () => deletarAvaliacao(avaliacao.id));

    listaAvaliacoes.appendChild(card);
  });

  lucide.createIcons();
}

function editarAvaliacao(avaliacao) {

  avaliacaoEditandoId = avaliacao.id;

  document.getElementById("filme_id").value = avaliacao.filme_id;
  document.getElementById("usuario").value = avaliacao.usuario;
  document.getElementById("nota").value = avaliacao.nota;
  document.getElementById("comentario").value = avaliacao.comentario;

  mostrarTela("avaliacoes");
}

async function deletarAvaliacao(id) {

  const confirmar = confirm(
    "Tem certeza que deseja excluir esta avaliação?"
  );

  if (!confirmar) return;

  await fetch(`${API_URL}/avaliacoes/${id}`, {
    method: "DELETE",
    headers: getHeaders()
  });

  listarAvaliacoes();
}

formAvaliacao.addEventListener("submit", async (event) => {

  event.preventDefault();

  const avaliacao = {
    filme_id: document.getElementById("filme_id").value,
    usuario: document.getElementById("usuario").value,
    nota: Number(document.getElementById("nota").value),
    comentario: document.getElementById("comentario").value
  };

  if (avaliacaoEditandoId) {

    await fetch(`${API_URL}/avaliacoes/${avaliacaoEditandoId}`, {
      method: "PUT",
      headers: getHeaders(),
      body: JSON.stringify(avaliacao)
    });

    avaliacaoEditandoId = null;

  } else {

    await fetch(`${API_URL}/avaliacoes/`, {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify(avaliacao)
    });
  }

  formAvaliacao.reset();

  listarAvaliacoes();
});

async function verAvaliacoesDoFilme(filmeId) {

  const resposta = await fetch(
    `${API_URL}/avaliacoes/filme/${filmeId}`,
    {
      headers: getHeaders()
    }
  );

  const avaliacoes = await resposta.json();

  mostrarTela("avaliacoes");

  renderizarAvaliacoes(avaliacoes);
}

listarFilmes();
listarAvaliacoes();

lucide.createIcons();
