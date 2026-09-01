"""
Sistema de Biblioteca — Ponto de entrada.

Une as funcionalidades de cadastro de usuários, cadastro de livros,
empréstimo, devolução e consulta em um único menu de terminal.
"""

from cadastro_usuarios import cadastrar_usuario, consultar_emprestados
from cadastro_livros import cadastrar_livro
from emprestimos import realizar_emprestimo
from devolucoes import devolver_livro


def listar_usuarios(usuarios):
    print("\n--- Usuários Cadastrados ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for u in usuarios:
        print(f"Nome: {u['nome']} | ID: {u['identificador']}")


def listar_livros(livros):
    print("\n--- Livros Cadastrados ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for l in livros:
        status = "Disponível" if l["disponivel"] else "Emprestado"
        print(f"Título: {l['titulo']} | ID: {l['identificador']} | Status: {status}")


def exibir_menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Cadastrar usuário")
    print("2. Cadastrar livro")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Listar usuários")
    print("6. Listar livros")
    print("7. Consultar livros emprestados")
    print("0. Sair")


def main():
    usuarios = []
    livros = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            cadastrar_livro(livros)
        elif opcao == "3":
            realizar_emprestimo(usuarios, livros)
        elif opcao == "4":
            devolver_livro(livros)
        elif opcao == "5":
            listar_usuarios(usuarios)
        elif opcao == "6":
            listar_livros(livros)
        elif opcao == "7":
            consultar_emprestados(livros)
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()