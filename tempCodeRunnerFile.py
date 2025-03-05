from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Annotated
from fastapi import FastAPI,Depends,Path,HTTPException
from Config.config import config
from Schemas.models import Redirection
from connection import engine,create_db_and_tables



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def addRedirects(redirects:list[str]):
    create_db_and_tables()
    with Session(engine) as session:
        for redirect in redirects:
            
            m = Redirection(**redirect)
            session.add(m)
            session.commit()
            session.refresh(m)
    
    return {'message':'Models insertion successful'}


if __name__=='__main__':

    # The Assumption of the code is that these data are already provided by the Client
    # This Code Just inserts the Data into the Database SQLite3

    models = [
        {"regex": r"(?i)(credit card)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(loan|mortgage)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(insurance claim)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(crypto|bitcoin|ethereum)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(stock market|shares|investment)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(legal advice|lawyer)", "model": "gemini-pro", "redirect_model": "claude-3"},
        {"regex": r"(?i)(medical advice|doctor|prescription)", "model": "gpt-4o", "redirect_model": "med-gpt"},
        {"regex": r"(?i)(AI ethics|bias|privacy)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(travel booking|flight|hotel)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(shopping|ecommerce|buy online)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(car loan|auto loan)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(student loan|education loan)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(cybersecurity|hacking|phishing)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(fitness|workout|exercise)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(gaming|video games|esports)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(music production|songwriting|studio)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(video editing|filmmaking|cinematography)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(weather forecast|climate change)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(coding|programming|software development)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(math problem|calculus|algebra)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(science experiment|physics|chemistry)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(resume writing|job search|interview tips)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(dating advice|relationships|marriage)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(pet care|dog training|cat behavior)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(mental health|therapy|counseling)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(cooking recipe|baking|food preparation)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(home improvement|DIY projects|interior design)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(parenting tips|baby care|child development)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(celebrity news|gossip|entertainment)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(history|historical events|archaeology)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(philosophy|ethics|morality)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(artistic techniques|painting|drawing)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(automobile news|car reviews|bike specifications)", "model": "gpt-4o", "redirect_model": "gemini-alpha"},
        {"regex": r"(?i)(government policies|politics|elections)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(business strategy|entrepreneurship|startups)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(real estate|housing market|buying property)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(foreign exchange|currency trading|forex)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(space exploration|NASA|astronomy)", "model": "gemini-pro", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(AI research|deep learning|machine learning)", "model": "gpt-4o", "redirect_model": "claude-3"},
        {"regex": r"(?i)(health insurance|medical policy|hospital bills)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(tax filing|income tax|financial planning)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
        {"regex": r"(?i)(home security|smart home|surveillance)", "model": "gemini-alpha", "redirect_model": "gpt-4o"},
        {"regex": r"(?i)(electric vehicles|EV charging|battery technology)", "model": "gpt-4o", "redirect_model": "gemini-pro"},
    ]
    
    addRedirects(models)




