from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Annotated
from fastapi import FastAPI,Depends,Path,HTTPException
from Config.config import config
from Schemas.models import FileRedirection
from connection import engine,create_db_and_tables



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def addRedirects(redirects:list[str]):
    create_db_and_tables()
    with Session(engine) as session:
        for redirect in redirects:
            
            m = FileRedirection(**redirect)
            session.add(m)
            session.commit()
            session.refresh(m)
    
    return {'message':'Models insertion successful'}


if __name__=='__main__':

    # The Assumption of the code is that these data are already provided by the Client
    # This Code Just inserts the Data into the Database SQLite3

    models = [
        {"file_type": "pdf", "redirect_provider": "anthropic", "redirect_model": "claude-v1"},

    ]
    
    addRedirects(models)




