from pydantic import BaseModel,Field



class Completions(BaseModel):
    provider:str
    model:str

class ChatCompletions(Completions):
    request:str

class Redirects(BaseModel):
    regex:str = Field(default = '^$',index = True)
    model:str = Field(index = True)
    redirect_model:str


