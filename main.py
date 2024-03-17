from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from routers import blog_get, blog_post, user, article, product, file
from auth import authentication
from typing import Optional
from db import models
from db.database import engine
from routers.exceptions import StoryException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get('/')
def index():
    return {'message': 'Hello World!'}


#Combine path and query params
@app.get('/info/{username}')
def get_info(username: str, is_memb: bool=True, family: Optional[str] = 'Ortega'):
    """Simulates retrieving the family of the user
    - **username** name of the user
    - **is_memb(bool)** define if is or not a member
    - **family (Optional[str])** name of the family
    """
    return {'message' : f'The user {username} is a {is_memb} member of the family {family}'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, ext: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': ext.name}
    )
'''
@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: StoryException):
    return PlainTextResponse(str(exc), status_code=400)
'''

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)



