from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    email: str
    senha: str