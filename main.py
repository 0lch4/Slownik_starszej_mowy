from fastapi import FastAPI, Form
from mydb import conn
from zapytania import query
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

mydb = conn()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, name: str = Form(...)):
    queryy = query(name)
    results_list = []
    for q in queryy:
        word = q[0]
        results_list.append(word)
    print(results_list)
    result = ', '.join(results_list)
    return templates.TemplateResponse("result.html", {"request": request, "result": result})
