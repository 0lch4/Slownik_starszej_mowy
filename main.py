from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from mydb import conn
from query import query

#polaczenie z baza
mydb = conn()
#utworzenie aplikacji
app = FastAPI()

#polaczenie z katalogiem z widokami
templates = Jinja2Templates(directory="templates")

#polaczenie ze stylami
app.mount("/static", StaticFiles(directory="static"), name="static")

#widok glowny ktory wyswietla sie pod adresem strony
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


#widok wyswietlajacy odpowiedz na zapytanie, po otrzymaniu odpowiedzi mozna cofnac sie do widoku glownego
@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, words: str = Form(None)):
    if words is None:
            #jesli uzytkownik nic nie poda zwraca strone glowna
        return templates.TemplateResponse("form.html", {"request": request})
    else:
        #rodziela wynik tak aby wyswietlone byly tylko przetlumaczone slowa
        queryy = query(words)
        results_list = []
        for q in queryy:
            word = q[0]
            results_list.append(word)
        result = ', '.join(results_list)
        if len(result)>0:
            #w przypadku odnalezienia danych pokazuje tlumaczenie
            return templates.TemplateResponse("result.html", {"request": request, "result": result})
        else:
            #w przypadku nie odnalezienia danych pokazuje komunikat o ich braku
            return templates.TemplateResponse("unkown_word.html", {"request": request, "result": result})
