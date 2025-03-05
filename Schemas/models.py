from sqlmodel import Field,Session,SQLModel,create_engine,select
import uuid



class AIModel(SQLModel,table = True):
    __tablename__ = 'aimodel'
    id:uuid.UUID = Field(default_factory = uuid.uuid4,primary_key = True)
    model_provider:str = Field(index = True)
    model_name:str


class AIResponse(SQLModel,table = True):
    __tablename__ = 'airesponse'
    id:uuid.UUID = Field(default_factory = uuid.uuid4,primary_key = True)
    model_provider:str = Field(foreign_key = "aimodel.model_provider")
    model_name:str = Field(foreign_key = "aimodel.model_name")
    model_response:str
    



class Redirection(SQLModel,table = True):

    __tablename__ = 'redirection'
    id:uuid.UUID = Field(default_factory = uuid.uuid4,primary_key = True)
    regex:str = Field(default = '^$',index = True)
    model:str = Field(index = True)
    redirect_model:str
    

class FileRedirection(SQLModel,table = True):

    __tablename__ = 'fileredirection'
    id:uuid.UUID = Field(default_factory = uuid.uuid4,primary_key = True)
    file_type:str = Field(default = '',index = True)
    redirect_provider:str = Field(index = True)
    redirect_model:str
    
