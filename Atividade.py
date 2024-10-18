import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Banco de dados
DADOS = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=DADOS)
Base = declarative_base()

# Definindo a tabela Funcionário
class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(String)
    cpf = Column(String, unique=True)  # CPF deve ser único
    setor = Column(String)
    funcao = Column(String)
    salario = Column(String)
    telefone = Column(String)

Base.metadata.create_all(bind=DADOS)

def salvar_funcionario(funcionario):
    session = Session()
    session.add(funcionario)
    session.commit()
    session.close()

def listar_todos_funcionarios():
    session = Session()
    funcionarios = session.query(Funcionario).all()
    session.close()
    return funcionarios

def pesquisar_um_funcionario(cpf):
    session = Session()
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    session.close()
    return funcionario

def atualizar_funcionario(funcionario):
    session = Session()
    session.commit()  # Supondo que o funcionário já está atualizado
    session.close()

def excluir_funcionario(funcionario):
    session = Session()
    session.delete(funcionario)
    session.commit()
    session.close()

while True:
    # Menu
    print("""
        === RH System ===
    1 - Adicionar funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do sistema.
    """)

    codigo = int(input("Digite o código: "))

    match codigo:
        case 1:
            os.system("cls || clear")
            # Solicitar dados para o usuário
            inf_nome = input("Digite seu nome: ")
            inf_idade = input("Digite sua idade: ")
            inf_cpf = input("Digite seu CPF: ")
            inf_setor = input("Digite seu setor: ")
            inf_funcao = input("Digite sua função: ")
            inf_salario = input("Digite seu salário: ")
            inf_telefone = input("Digite seu telefone: ")

            novo_funcionario = Funcionario(
                nome=inf_nome,
                idade=inf_idade,
                cpf=inf_cpf,
                setor=inf_setor,
                funcao=inf_funcao,
                salario=inf_salario,
                telefone=inf_telefone
            )
            salvar_funcionario(novo_funcionario)
            print("Funcionário adicionado com sucesso!")

        case 2:
            os.system("cls || clear")
            # Buscando o funcionario
            cpf = input("Digite o CPF do funcionário que deseja consultar: ")
            funcionario = pesquisar_um_funcionario(cpf)

            if funcionario:
                print(f"Nome: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
            else:
                print("Funcionário não encontrado.")

        case 3:
            os.system("cls || clear")
            # Atualizando o funcionario
            cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
            funcionario = pesquisar_um_funcionario(cpf)

            if funcionario:
                funcionario.nome = input("Digite o novo nome: ") 
                funcionario.idade = input("Digite a nova idade: ") 
                funcionario.setor = input("Digite o novo setor: ") 
                funcionario.funcao = input("Digite a nova função: ") 
                funcionario.salario = input("Digite o novo salário: ") 
                funcionario.telefone = input("Digite o novo telefone: ") 

                atualizar_funcionario(funcionario)
                print("Dados do funcionário atualizados com sucesso!")
            else:
                print("Funcionário não encontrado.")

        case 4:
            os.system("cls || clear")
            # Excluindo o funcionario
            cpf = input("Digite o CPF do funcionário que deseja excluir: ")
            funcionario = pesquisar_um_funcionario(cpf)

            if funcionario:
                excluir_funcionario(funcionario)
                print(f"{funcionario.nome} excluído com sucesso.")
            else:
                print("Funcionário não encontrado.")

        case 5:
            os.system("cls || clear")
            # Listando o funcionario
            funcionarios = listar_todos_funcionarios()

            if funcionarios:
                for f in funcionarios:
                    print(f"ID: {f.id}, Nome: {f.nome}, CPF: {f.cpf}, Setor: {f.setor}, Função: {f.funcao}, Salário: {f.salario}, Telefone: {f.telefone}")
            else:
                print("Nenhum funcionário cadastrado.")

        case 0:
            # Saindo
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida, tente novamente.")
