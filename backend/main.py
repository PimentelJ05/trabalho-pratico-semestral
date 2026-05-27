from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_router
from routes.filme_routes import router as filme_router
from routes.avaliacao_routes import router as avaliacao_router

app = FastAPI(
    title="CineReview API",
    description="API para gerenciamento de filmes e avaliações",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(filme_router)
app.include_router(avaliacao_router)


@app.get("/")
def home():
    return {"message": "API CineReview funcionando!"}