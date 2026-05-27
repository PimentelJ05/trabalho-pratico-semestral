const API_URL = "http://127.0.0.1:8000"

const formCadastro = document.getElementById(
    "form-cadastro"
)

formCadastro.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault()

        const nome = document.getElementById(
            "nome"
        ).value

        const email = document.getElementById(
            "email"
        ).value

        const senha = document.getElementById(
            "senha"
        ).value

        const perfil = document.getElementById(
            "perfil"
        ).value

        try {

            const response = await fetch(
                `${API_URL}/auth/registro`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        nome,
                        email,
                        senha,
                        perfil
                    })
                }
            )

            const data = await response.json()

            if (!response.ok) {
                throw new Error(
                    data.detail || "Erro ao cadastrar"
                )
            }

            alert("Conta criada com sucesso!")

            window.location.href = "cadastro.html"

        } catch (error) {

            alert(error.message)

        }

    }
)