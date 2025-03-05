from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Annotated
from fastapi import FastAPI,Depends,Path,HTTPException
from Config.config import config
from Schemas.models import AIModel,AIResponse
from connection import engine,create_db_and_tables



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def addModels(models:list[str]):
    create_db_and_tables()
    with Session(engine) as session:
        for model in models:
            print({**model})
            m = AIModel(**model)
            session.add(m)
            session.commit()
            session.refresh(m)
    
    return {'message':'Models insertion successful'}


if __name__=='__main__':

    # The Assumption of the code is that these data are already provided by the Client
    # This Code Just inserts the Data into the Database SQLite3

    models = [
        {"model_provider":"openai","model_name":"gpt-3.5"},
        {"model_provider":"anthropic","model_name":"claude-v1"},
        {"model_provider":"gemini","model_name":"gemini-alpha"}
    ]
    
    addModels(models)




