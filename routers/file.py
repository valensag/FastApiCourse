from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix = '/file',
    tags=['file'])

@router.post('/')
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split('\n')
    return {'lines': lines}

@router.post('/uploadfile')
def get_uploadfile(uploadfile: UploadFile = File(...)):
    return {
        'filename': uploadfile.filename
    }
