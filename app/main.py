from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Any
from app.connection.query import query
from app.connection.mydb import conn

mydb = conn()
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


# main view on site address, ask for word
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request) -> Any:
    return templates.TemplateResponse("form.html", {"request": request})


# show results
@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, words: str = Form(None)) -> Any:  # noqa: B008
    if words is None:
        return templates.TemplateResponse("form.html", {"request": request})
        # formating the results
    queryy = query(words)
    results_list = []
    for que in queryy:
        word = que[0]
        results_list.append(word)
    result = ", ".join(results_list)
    if len(result) > 0:
        return templates.TemplateResponse(
            "result.html", {"request": request, "result": result}
        )
    return templates.TemplateResponse(
        "unkown_word.html", {"request": request, "result": result}
    )
