from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.predictor import Predictor

# Initializing the application
app = FastAPI()

# setting the path for static files (for css files)
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# setting the path for templates (for html files)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_caption(request: Request):
    data = ""
    return templates.TemplateResponse("page.html", {"request": request, "data": "Hello word"})


@app.post("/")
async def get_caption(request: Request):
    p = Predictor()
    d = p.predict("test")

