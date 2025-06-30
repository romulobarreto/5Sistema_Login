from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from models.user import User


class Endereco(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    endereco: str
    complemento: Optional[str]
    cidade: str = Field(index=True)
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="enderecos")