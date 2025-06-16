from sqlmodel import SQLModel, create_engine
from models.user import *

engine = create_engine("sqlite:///database/system.db", echo=True)

def criar_banco():
    SQLModel.metadata.create_all(engine)