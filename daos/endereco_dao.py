from models.endereco import *
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from database.database import engine
from models.user import User

class EnderecoDao:

    @staticmethod
    def carregar_dados(email_mensagem: str):
        try:
            with Session(engine) as session:
                statement = select(User).where(User.email == email_mensagem).options(selectinload(User.enderecos))
                usuario = session.exec(statement).first()
                return True, usuario
        except Exception as e:
            return False, f"\n⚠️ Erro ao buscar dados: {str(e)}"
        




    @staticmethod
    def cadastrar_endereco(endereco: Endereco):
        try:
            with Session(engine) as session:
                session.add(endereco)
                session.commit()
                return True, "\n✅ Dados cadastrados no banco."
        except Exception as e:
            return False, f"\n⚠️ Erro ao cadastrar endereço: {str(e)}"
        




    @staticmethod
    def excluir_endereco(id):
        try:
            with Session(engine) as session:
                statement = select(Endereco).where(Endereco.id == id)
                endereco = session.exec(statement).first()
                session.delete(endereco)
                session.commit()
                session.refresh(endereco)
                return True, "\n✅ Endereço excluído com sucesso."
        except Exception as e:
            return False, f"\n⚠️ Erro ao excluir endereço: {str(e)}"
        
