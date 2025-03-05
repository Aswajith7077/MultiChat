from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Annotated
from fastapi import FastAPI,Depends,Path,HTTPException
from Config.config import config


# def connection():

sqlite_url = config['DB_URL']


connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url,connect_args = connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def getSession():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session,Depends(getSession)]