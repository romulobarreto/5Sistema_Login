from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from models.endereco import Endereco

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(index= True, unique= True)
    senha: str
    enderecos: list['Endereco'] = Relationship(back_populates="user")