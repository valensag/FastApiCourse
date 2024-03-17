from typing import List, Optional
from fastapi import APIRouter, Cookie, Depends, Form, Header, Response

router = APIRouter(
    prefix= '/product',
    tags=['product']
)

#Dummy data
products = ['watch', 'camare', 'phone']

@router.get('/all')
def get_all_products():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    #Generate a cookie
    response.set_cookie(key="test_cookie",value="test_cookie_value")
    return response

@router.get('/withheader')
def get_products(
        response: Response, 
        custom_header: Optional[List[str]] = Header(None),
        test_cookie: Optional[str] = Cookie(None)
    ):
    #Generate a custom header
    if custom_header:
        response.headers['custom_response_header'] = ", ".join(custom_header)
    return {
        'data': products,
        'custom_header': custom_header,
        'cookie': test_cookie 
    }

#User forms html
@router.post('/new') 
def create_product(name:str = Form(...)):
    products.append(name)
    return products