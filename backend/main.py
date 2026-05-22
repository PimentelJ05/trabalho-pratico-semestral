from fastapi import FastAPI
from routes.filme_routes import router as filme_router
from routes.avaliacao_routes import router as avaliacao_router

app = FastAPI(
    title="CineReview API",
    description="API para gerenciamento de filmes e avaliações",
    version="1.0.0"
)

app.include_router(filme_router)
app.include_router(avaliacao_router)

@app.get("/")
def home():
    return {"message": "API CineReview funcionando!"}