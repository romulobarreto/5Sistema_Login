from controllers.endereco_controller import *

class EnderecoView:
    @staticmethod
    def detalhar_enderecos(email_mensagem):
        # Chama o controller
        sucesso, mensagem = EnderecoController.detalhar_enderecos(email_mensagem)

        if not sucesso:
            print(mensagem)
            return
        else:
            print(mensagem)
            return



    
    @staticmethod
    def cadastrar_endereco(email_mensagem):
        # Solicita o input de endereco, complemento e cidade
        print("\n🗂️ Informe os seus dados de endereço para cadastro:")
        endereco = input("\nDigite o endereço (Logradouro + N°): ").lower().strip()
        complemento = input("Digite o complemento caso haja: ").lower().strip()
        cidade = input("Digite o nome da cidade (sem o Estado): ").lower().strip()

        # Chama o controller
        sucesso, mensagem = EnderecoController.cadastrar_endereco(endereco, complemento, cidade, email_mensagem)

        if not sucesso:
            print(mensagem)
            return
        else:
            print(mensagem)
            return
        



    @staticmethod
    def excluir_endereco(email_mensagem):
        # Solicita o input do id de endereço para excluir
        try:
            id_endereco = int(input("\nDigite o ID do endereço que deseja excluir: "))
        except ValueError:
            print("\n✅ Todos endereços foram mantidos.")

        # Chama o controller