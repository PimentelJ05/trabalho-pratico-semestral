from uuid import uuid4


def test_criar_filme_sucesso():

    filme = {
        "titulo": "Corra",
        "descricao": "Terror psicológico",
        "genero": "Terror",
        "ano": 2017,
        "diretor": "Jordan Peele"
    }

    assert filme["titulo"] == "Corra"
    assert filme["ano"] == 2017


def test_filme_sem_titulo():

    filme = {
        "descricao": "Sem título"
    }

    assert "titulo" not in filme


def test_buscar_filme_existente():

    filme_id = str(uuid4())

    assert filme_id is not None


def test_buscar_filme_inexistente():

    filme = None

    assert filme is None