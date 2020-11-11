from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
site = 'https://tzfrontend.herokuapp.com'
app.mount("/static", StaticFiles(directory="static", html=True ), name="static")

@app.get("/images/")
def get_images():
    return [
        {"image_id":1,'src':f'{site}/static/1_small.jpg'},
        {"image_id":2,'src':f'{site}/static/2_small.jpg'},
        {"image_id":3,'src':f'{site}/static/3_small.jpg'},
        {"image_id":4,'src':f'{site}/static/4_small.jpg'},
        {"image_id":5,'src':f'{site}/static/5_small.jpg'},
        {"image_id":6,'src':f'{site}/static/6_small.jpg'}
    ]

@app.get("/")
def read_root():
    return "hello world"

@app.get("/images/{image_id}/")
def get_image(image_id: int):
    if image_id<7 and image_id>0:
        return {"src": f'{site}/static/{image_id}.jpg'}
    return HTTPException(status_code=404, detail="Image not found")

@app.post("/comments/add/")
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@app.get("/comments/{image_id}/")
def get_comments(image_id: int,db: Session = Depends(get_db)):
    comments = crud.get_comments(db, image_id)
    if image_id < 1 or image_id > 6:
        raise HTTPException(status_code=404, detail="Image not found")
    if comments:
        return comments
    raise HTTPException(status_code=207,detail="This image is without comments")
