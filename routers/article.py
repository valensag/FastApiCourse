from fastapi import APIRouter, Depends
from db.database import  get_db
from db.models import DbArticle
from schemas import ArticleBase, ArticleDisplay, UserBase
from sqlalchemy.orm import Session
from db import db_article
from typing import List
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(
    prefix= '/article',
    tags=['article']
)

#Create article
@router.post('/', response_model= ArticleDisplay)
def create_article(request:ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)

#Get specific article (Authentication depending on the token)
@router.post('/token/{id}', response_model= ArticleDisplay)
def get_article_token(id: int, db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)):
    return db_article.get_article_token(db, id)

#Get specific article (Authentication depending on the user)
@router.get('/{id}')
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, id),
        "current_user": current_user
    }