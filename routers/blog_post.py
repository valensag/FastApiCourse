from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel 
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
    )

#Create a custom Model class
class Image(BaseModel):
    url: str
    alias: str

#Body request model
class BlogModel(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool]
    #Complex Validators List, Dict, Set, Tuple
    tags: List[str]= []
    metadata: Dict[str, str]= {'key1': 'value1'}
    image: Optional[Image] = None

#Body model + path and query params
@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
        } 

#Add metadata with description
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
        blog: BlogModel,
        id: int, 
        comment_title: int = Query(
            None,
            title= 'Title of the comment',
            description= 'Description of the comment title',
            alias= 'commentTitle',
            #This deprecated is useful fon diff versions of api
            deprecated=True
        ),
        #Validator optional body
        content: str = Body('This is a validator default'),
        #Validator mandatory body with min_length constrain and regex
        content_mandatory : str = Body(..., 
                                       min_length=10,
                                       regex='^[a-z\s]*$'),
        #Multiple values
        v: Optional[List[str]] = Query(['1', '2', '3']),
        #Validators of data
        #gt, ge, lt, le
        comment_id: int = Path(gt=5, le=10)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'comment_content': content,
        'content_mandatory': content_mandatory,
        'version': v,
        'comment_id': comment_id
    }

#Dependencies
def required_functionality():
    return{'message': 'Learning FastAPI framework'}





