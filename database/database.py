from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database/system.db")

def criar_banco():
    SQLModel.metadata.create_all(engine)