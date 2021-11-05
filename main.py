from fastapi import FastAPI,UploadFile,File,Request,Body
import shutil
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse
import io


app = FastAPI()
"""
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

"""
@app.post("/")
async def root(text):
    return "hello world"