from fastapi import APIRouter, status, Response, Query, Depends
from enum import Enum
from typing import Optional, List
from routers.blog_post import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
    )

#Path Parameters
#Summary & Description
@router.get(
        '/all',
        summary='Retrieves all Blogs',
        description='This api call simulate fetching all blogs',
        response_description='Description of the response'
        )
def get_all_blogs():
    return {'message': f'All is returned'}

#Predefined path: Enum
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get(
        '/type/{type}',
        tags=['type']
        )
def get_blog_type(type = BlogType):
    return {'message': f'Blog type {type}'}

#Query parameters: page and page_size with default value
@router.get('/size')
def get_blog_page_size(page = 0, page_size=1000,
        #Import a function from other router
        req_parameter: dict = Depends(required_functionality)):
    return {'message' : f'We have {page_size} blogs on page {page}',
            'req_parameter': req_parameter}
 
#Query parameters: page and page_size with Optional value
@router.get('/peque_size')
def get_blog_peque_size(page = 0, page_size : Optional[int] = None):
    return {'message' : f'We have {page_size} blogs on page {page}'}

#Operation description with custom Status Code status
@router.get('/{id}')
def get_blog_status(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'message': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'This is the Blog id {id}'}


