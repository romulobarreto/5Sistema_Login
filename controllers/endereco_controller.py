from models.endereco import *
from daos.endereco_dao import *
from utils.validacao import validar_endereco

class EnderecoController:

    @staticmethod
    def _validar_dados(endereco, cidade):
        # Valida o endereco recebido
        valida_endereco = validar_endereco(endereco)
        if not valida_endereco:
            return False, f"\n⚠️ O endereço: {endereco} não está no padrão válido."
        
        if not cidade:
            return False, f"\n⚠️ A cidade precisa ser preenchida."
        
        return True, "✅ Dados validados."
    






    @staticmethod
    def cadastrar_endereco(endereco, complemento, cidade, email_mensagem):
        # Valida os dados recebidos
        sucesso, mensagem = EnderecoController._validar_dados(endereco, cidade)

        if not sucesso:
            return False, mensagem
        
        # Carrega os dados do usuário
        sucesso, usuario = EnderecoDao.carregar_dados(email_mensagem)

        # Cria uma instância de endereço
        adress = Endereco(id=None, endereco=endereco, complemento=complemento, cidade=cidade, user_id=usuario.id)

        # Chama a DAO para cadastro de endereço
        sucesso, mensagem = EnderecoDao.cadastrar_endereco(adress)

        if not sucesso:
            return False, mensagem
        else:
            return True, mensagem
        





    @staticmethod
    def detalhar_enderecos(email_mensagem):
        # Carrega a lista de dados 
        sucesso, usuario = EnderecoDao.carregar_dados(email_mensagem)

        if not sucesso:
            return False, usuario

        if not usuario.enderecos:
            return False, f"\n⚠️ Nenhum endereço cadastrado."
        
        lista_formatada = f"\n🏠 Detalhes dos endereços cadastrados:"
        for endereco in usuario.enderecos:
            lista_formatada += (
                f"\nID: {endereco.id}"
                f"\nLogradouro: {endereco.endereco.title()}"
                f"\nComplemento: {endereco.complemento.upper()}"
                f"\nCidade: {endereco.cidade.title()}"
                f"\n------------------------------"
            )

        return True, lista_formatada
    




    @staticmethod
    def excluir_endereco(email_mensagem, id_endereco):
        # Carrega a lista de dados
        sucesso, usuario = EnderecoDao.carregar_dados(email_mensagem)

        verifica_id = next((endereco for endereco in usuario.enderecos if endereco.id == id_endereco), None)

        if not verifica_id:
            return False, f"\n❌ O ID: {id_endereco} não faz parte da sua lista de endereços."
        
        # Chama a DAO
        sucesso, mensagem = EnderecoDao.excluir_endereco(id_endereco)

        if not sucesso:
            return False, mensagem
        else: 
            return True, mensagem