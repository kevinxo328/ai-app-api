from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers import openai, redis, sql, users

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
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

app.include_router(openai.router, prefix="/api")
app.include_router(redis.router, prefix="/api")
app.include_router(sql.router, prefix="/api")
app.include_router(users.router, prefix="/api")


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")
