# 🔐 Projeto Sistema de Login - Documentação

## 📌 Visão Geral
Este projeto é um sistema simples de login e gerenciamento de usuários.  
Foi desenvolvido com o objetivo de aplicar conceitos de programação orientada a objetos, padrão arquitetural MVC e integração com banco de dados SQLite.

---

## 📂 Entidades e Estruturas de Dados

### 👤 User
Representa um usuário do sistema.

- **Atributos:**
  - `id`: Identificador único do usuário
  - `nome`: Nome completo
  - `email`: Email do usuário
  - `senha`: Senha criptografada

- **Regras de Negócio:**
  - O email deve ser único.
  - A senha deve ser armazenada de forma segura (criptografada).

### 🏠 Endereco
Representa um endereço vinculado a um usuário.

- **Atributos:**
  - `id`: Identificador único do endereço
  - `endereco`: Nome da rua com número
  - `complemento`: Complemento do endereço (Opcional)
  - `cidade`: Cidade do endereço
  - `usuario_id`: ID do usuário associado (chave estrangeira)

- **Relacionamento:**
  - Um usuário pode ter múltiplos endereços (One-to-Many)

---

## 📁 Estrutura do Projeto (Padrão MVC)

### 📂 DataBase
- `database.py`: Função que cria o banco de dados `system.db`.
- `system.db`: Banco de dados do projeto.

### 📂 Models
- `user.py`: Classe que define a entidade `User`.
- `endereco.py`: Classe que define a entidade `Endereco`.

### 📂 Views
- `user_view.py`: Responsável pela interação com o usuário via terminal.
- `endereco_view.py`: Interação com o usuário para operações de endereços.

### 📂 Controllers
- `user_controller.py`: Regras e lógica de manipulação de usuários.
- `endereco_controller.py`: Lógica de negócios para endereços.

### 📂 DAOs
- `user_dao.py`: Acesso ao banco de dados SQLite.
- `endereco_dao.py`: Acesso ao banco de dados para endereços.

### 📂 Utils
- `validacao.py`: Funções auxiliares de validação de dados.

### 📂 Main
- `main.py`: Arquivo principal para execução do sistema.

---

## ⚙️ Funcionalidades

- Cadastrar novos usuários
- Editar dados de usuários
- Excluir usuários
- Efetuar login
- Efetuar logout
- Cadastrar, listar e excluir endereços de um usuário logado

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem**: Python
- **Banco de Dados**: SQLite
- **Arquitetura**: MVC
- **Interface**: Terminal
- **Bibliotecas**:
  - `sqlmodel`: ORM para manipulação do banco de dados SQLite
  - `re`: Validações com expressões regulares
  - `hashlib`: Para criptografia de senhas

---

## 🔄 Fluxo de Uso

1. Usuário abre o sistema via terminal
2. Escolhe entre: login, cadastro ou sair
3. Se logado, pode editar ou excluir seu usuário
4. Usuário logado pode gerenciar seus endereços
5. Todas as ações afetam diretamente o banco de dados SQLite