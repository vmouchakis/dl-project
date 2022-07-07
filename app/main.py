from ast import Str
from fastapi import FastAPI, File, Request, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from pathlib import Path
from app.predictor import Predictor
from io import BytesIO
from PIL import Image
import numpy as np

# Initializing the application
app = FastAPI()

# setting the path for static files (for css files)
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

app.mount(
    "/flickr8k",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "flickr8k/Images"),
    name="Images"
)

# setting the path for templates (for html files)
templates = Jinja2Templates(directory="templates", autoescape=False)



@app.get("/")
async def get_caption(request: Request):
    data = ""
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.post("/")
async def get_caption(request: Request, image: str = Form(default="")):
    p = Predictor()

    if image == "":
        response = "No image given."
        return templates.TemplateResponse("page.html", {"request": request, "data": response})
    else:
        caption, img = p.predict(image)
        print(img)
        image_path = "/images/"+img
        # image_path = f"{{ url_for(static, path=/images/{img}) }}"
        # image_path = image_path.encode("Latin-1").decode("utf-8")
        print(image_path)
        return templates.TemplateResponse("page.html", {"request": request, "data": caption, "image": image_path})

