"""
Поиск и просмотр аниме без необходимости бродить по миллиону сайтов? Теперь возможно!\n
В этом модуле происходит импорт и настройка зависимостей проекта.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/hello/{name}")
async def hello(request: Request, name: str) -> HTMLResponse:
    return templates.TemplateResponse(
            request=request, name="hello.html", context={"name": name}
    )

