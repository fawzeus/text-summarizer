from fastapi import FastAPI,Request
import shutil
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.middleware.cors import CORSMiddleware

import io
import spacy
from summerizer import calculate_sentences_score,calculate_word_frequency,summerize,normalize,readingTime,reduced_by


from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    text: str

app = FastAPI()
nlp = spacy.load("en_core_web_sm")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def read_root(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@app.post("/")
async def root(message:Message):
    docx=nlp(message.text)
    words_freaquency=calculate_word_frequency(docx)
    normalize(words_freaquency)
    sentences_score=calculate_sentences_score(docx,words_freaquency)
    #print("reading time befor sum",readingTime(docx))
    summary=summerize(sentences_score)
    docy=nlp(summary)
    #print("reading time befor sum",readingTime(docy))

    return({"result":summary,"before":readingTime(docx),"after":readingTime(docy)})
