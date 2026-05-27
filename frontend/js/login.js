const API_URL = "http://127.0.0.1:8000"

const form = document.getElementById("form-login")

form.addEventListener("submit", async (event) => {

    event.preventDefault()

    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    try {

        const response = await fetch(
            `${API_URL}/auth/login`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email,
                    senha
                })
            }
        )

        const data = await response.json()

        if (!response.ok) {
            throw new Error(data.detail)
        }

        localStorage.setItem(
            "token",
            data.access_token
        )

        alert("Login realizado com sucesso!")

        window.location.href = "dashboard.html"

    } catch (error) {

        alert(error.message)

    }

})