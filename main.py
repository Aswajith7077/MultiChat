from fastapi import FastAPI,Query,Path,status,Body,Header,Cookie,Form,File,UploadFile,Depends,HTTPException
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional,Annotated
from fastapi.security import OAuth2PasswordBearer
from connection import Session,getSession,create_db_and_tables
from Schemas.models import AIModel,AIResponse, Redirection,FileRedirection
from RequestSchema.chatCompletions import ChatCompletions as CC,Completions,Redirects
from sqlmodel import select,text
import re


app = FastAPI()


regexData = None



origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

template_content = ""
sample_list = [i for i in range(99)]


@app.on_event("startup")
def startup():
    create_db_and_tables()




# Static Routes



@app.get("/models")
async def auth_route(session:Annotated[Session,Depends(getSession)]) -> list[str]:
    models = session.exec(select(AIModel)).all()
    response = []
    for model in models:
        response.append(model.model_provider + "/" + model.model_name)
    return response


@app.post("/v1/file/completions")
async def FileCompletions(
    file: Annotated[UploadFile, File(...)],
    provider: Annotated[str, Form(...)],
    model: Annotated[str, Form(...)],
    session: Annotated[Session, Depends(getSession)]
):
    result = session.exec(select(AIResponse).where(AIResponse.model_provider == provider and AIResponse.model_name == model)).all()
    
    if not result:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail = "The Given model is not in the database")

    required = list(result)[-1]
    print(file.filename.split('.')[-1])
    

    response_model = model
    response = {
        "provider":provider,
        "model":model,
        "response":required.model_response + " File: Has Parsed",
        "origin":response_model
    }
    

    return response



@app.post("/admin/file")
async def FileCompletions(
    file: Annotated[UploadFile, File(...)],
    session: Annotated[Session, Depends(getSession)]
):
    
    
    file_type = file.filename.split('.')[-1]


    file_redirects = session.exec(select(FileRedirection).where(FileRedirection.file_type == file_type)).first()

    
    if file_redirects:
        provider = file_redirects.redirect_provider
        model = file_redirects.redirect_model
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

    result = session.exec(select(AIResponse).where(AIResponse.model_provider == provider and AIResponse.model_name == model)).all()
    
    if not result:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail = "The Given model is not in the database")

    required = list(result)[-1]

    response_model = model
    response = {
        "provider":provider,
        "model":model,
        "response":required.model_response + " File: Has Parsed",
        "origin":response_model
    }
    

    return response

@app.post("/v1/chat/completions")
async def ChatCompletions(form_data:Annotated[CC,Body()],session:Annotated[Session,Depends(getSession)]):
    global regexData


    print(form_data)
    result = session.exec(select(AIResponse).where(AIResponse.model_provider == form_data.provider and AIResponse.model_name == form_data.model)).all()
    
    if not result:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail = "The Given model is not in the database")

    required = list(result)[-1]
    print(required)

    response_model = form_data.model

    if not regexData:
        regexData = session.exec(select(Redirection)).all()
    for data in regexData:
        pattern = re.compile(data.regex)
        r = pattern.match(form_data.request)
        if r:
            response_model = data.redirect_model



    response = {
        "provider":form_data.provider,
        "model":form_data.model,
        "response":required.model_response,
        "origin":response_model
    }
    
    return response



@app.get('/admin/get_redirects')
async def get_redirects(session:Annotated[Session,Depends(getSession)]):
    result = session.exec(select(Redirection)).all()
    return result


@app.post('/admin/overwrite')
async def over_write(items:Annotated[list[Redirects],Body()],session:Annotated[Session,Depends(getSession)]):

    session.execute(text('DELETE FROM redirection;'))

    for item in items:
        it = Redirection(**item.dict())
        session.add(it)
        session.commit()
        session.refresh(it)

    return {'message':'Overwritten Successfully'}