from database.database import criar_banco
from views.user_view import *
from views.endereco_view import *

def menu():
    # Exibe o menu no terminal
    criar_banco()
    while True:
        print("\n🖥️ Sistema de Usuários")
        print("\n📄 Menu:")
        print("1️⃣ - Login")
        print("2️⃣ - Registre-se")
        print("3️⃣ - Sair")

        opcao = input("\nEscolha uma das opções: ").strip()

        match opcao:
            case "1":
                while True:
                    sucesso, email_mensagem = UserView.login()
                    if sucesso:
                        while True:
                            UserView.detalhar_usuario(email_mensagem)
                            print("\n📑 Opções de cadastro:")
                            print("1️⃣ - Editar Cadastro")
                            print("2️⃣ - Excluir Conta")
                            print("3️⃣ - Endereços")
                            print("4️⃣ - Sair")

                            opcao_login = input("\nDigite a opção desejada: ").strip()

                            match opcao_login:
                                case "1":
                                    email_mensagem = UserView.editar_usuario(email_mensagem)
                                case "2":
                                    while True:
                                        print("\n❓ Deseja realmente excluir sua conta?")
                                        print("1️⃣ - Sim")
                                        print("2️⃣ - Não")

                                        opcao_excluir = input("\nDigite a opção desejada: ").strip()

                                        match opcao_excluir:
                                            case "1":
                                                UserView.excluir_conta(email_mensagem)
                                                voltar_menu = True
                                                break
                                            case "2":
                                                voltar_menu = False
                                                break
                                            case _:
                                                print("\n⚠️ Opção inválida! Tente novamente.")
                                    
                                    if voltar_menu:
                                        break

                                case "3":
                                    while True:
                                        EnderecoView.detalhar_enderecos(email_mensagem)
                                        print("\n📑 Opções de cadastro:")
                                        print("1️⃣ - Cadastrar Endereço")
                                        print("2️⃣ - Excluir Endereço")
                                        print("3️⃣ - Voltar")

                                        opcao_endereco = input("\nDigite a opção desejada: ").strip()
                                        match opcao_endereco:
                                            case "1":
                                                EnderecoView.cadastrar_endereco(email_mensagem)
                                            case "2":
                                                EnderecoView.excluir_endereco(email_mensagem)
                                            case "3":
                                                break
                                            case _:
                                                print("\n⚠️ Opção inválida! Tente novamente.")
                                case "4":
                                    voltar_menu = True
                                    break
                                case _:
                                    print("\n⚠️ Opção inválida! Tente novamente.")

                        if voltar_menu:
                            break
                    else:
                        while True:
                            print("1️⃣ - Tentar Novamente")
                            print("2️⃣ - Voltar")

                            opcao_login = input("\nDigite a opção desejada: ").strip()
                            match opcao_login:
                                case "1":
                                    voltar_menu = False
                                    break
                                case "2":
                                    voltar_menu = True
                                    break
                                case _:
                                    print("\n⚠️ Opção inválida! Tente novamente.")
                        
                        if voltar_menu:
                            break
            case "2":
                UserView.cadastrar_usuario()
            case "3":
                print("🚪 Saindo do programa...")
                break
            case _:
                print("⚠️ Opção inválida! Tente novamente.\n")

                    




if __name__ == "__main__":
    menu()