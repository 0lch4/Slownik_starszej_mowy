from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mydb import conn
from query import query

mydb = conn()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, words: str = Form(...)):
    queryy = query(words)
    results_list = []
    for q in queryy:
        word = q[0]
        results_list.append(word)
    result = ', '.join(results_list)
    if len(result)>0:
        return templates.TemplateResponse("result.html", {"request": request, "result": result})
    else:
        return templates.TemplateResponse("unkown_word.html", {"request": request, "result": result})
