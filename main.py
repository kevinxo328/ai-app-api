from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers import openai

origins = [
    "http://localhost:5173",
    "https://ai-app-web-git-dev-kevinxo328.vercel.app",
    "https://ai-app-web-git-main-kevinxo328.vercel.app",
    "https://ai-app-web-service.vercel.app",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(openai.router)


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")
