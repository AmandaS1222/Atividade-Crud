# Atividade-Crud

## Objetivo:
Em dupla, usando funções implemente um CRUD com os dados informados abaixo.
Exemplo:
```
def salvar_funcionario(funcionario):
    pass

def listar_todos_funcionarios():
    pass

def pesquisar_um_funcionario(funcionario):
    pass

def atualizar_funcionario(funcionario):
    pass

def excluir_funcionario(funcionario):
    pass

```

Atributos da classe.

```
class Funcionario:
    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
```

## Tecnologias:
Será necessário utilizar as tecnologias abaixo:
- ORM: SQLAlchemy
- Banco de dados: SQLite
- Versionamento: Git

## Resultado esperado:
Um sistema onde o usuário veja um menu e escolher dentre as opções disponíveis.

```
        === RH System ===
    1 - Adicionar funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do sistema.
```

O menu será exibido após realizar as ações do menu.
