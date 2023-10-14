from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import openai

app = FastAPI()

app.include_router(openai.router)


@app.get('/', include_in_schema=False)
def home():
    return RedirectResponse('/docs')
