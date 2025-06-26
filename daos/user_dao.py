from models.user import *
from sqlmodel import Session, select
from database.database import engine

class UserDao:

    @staticmethod
    def carregar_usuarios():
        try:
            with Session(engine) as session:
                statement = select(User)
                usuarios = session.exec(statement).all()
                return True, usuarios
        except Exception as e:
            return False, f"\n⚠️ Erro ao buscar usuários: {str(e)}"
        




    @staticmethod
    def cadastrar_usuario(user: User):
        try:
            with Session(engine) as session:
                session.add(user)
                session.commit()
                return True, "\n✅ Dados cadastrados no banco."
        except Exception as e:
            return False, f"\n⚠️ Erro ao cadastrar usuário: {str(e)}"
        



    @staticmethod
    def excluir_usuario(email_mensagem):
        try:
            with Session(engine) as session:
                statement = select(User).where(User.email == email_mensagem)
                usuario = session.exec(statement).first()
                session.delete(usuario)
                session.commit()
                return True, "\n✅ Usuário excluído com sucesso."
        except Exception as e:
            return False, f"\n⚠️ Erro ao excluir usuário: {str(e)}"
        



    @staticmethod
    def editar_usuario(nome, email, senha_hash, usuario_cadastrado):
        try:
            with Session(engine) as session:
                statement = select(User).where(User.id == usuario_cadastrado.id)
                usuario = session.exec(statement).first()
                usuario.nome = nome
                usuario.email = email
                usuario.senha = senha_hash
                session.add(usuario)
                session.commit()
                session.refresh(usuario)
                return True, "\n✅ Usuário editado com sucesso."
        except Exception as e:
            return False, f"\n⚠️ Erro ao editar usuário: {str(e)}"