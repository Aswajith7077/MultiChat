from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Annotated
from fastapi import FastAPI,Depends,Path,HTTPException
from Config.config import config
from Schemas.models import AIModel,AIResponse
from connection import engine,create_db_and_tables



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def addResponses(responses:list[str]):
    create_db_and_tables()
    with Session(engine) as session:
        for response in responses:

            m = AIResponse(**response)
            session.add(m)
            session.commit()
            session.refresh(m)
    
    return {'message':'Models insertion successful'}


if __name__=='__main__':

    # The Assumption of the code is that these data are already provided by the Client
    # This Code Just inserts the Data into the Database SQLite3

    responses = [
        {"model_provider":"openai","model_name":"gpt-3.5","model_response":"OpenAI: Processed your prompt with advanced language understanding. Response ID: openai_response_001"},
        {"model_provider":"anthropic","model_name":"claude-v1","model_response":"Anthropic: Your prompt has been interpreted with ethical AI principles. Response ID: anthropic_response_002"},
    ]
    
    addResponses(responses = responses)




