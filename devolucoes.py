# Devolução de Livros (feature/devolucoes)
def devolver_livro(livros):
    print("\n--- Devolução de Livros ---")
    if not livros:
        print(" Atenção: Não há livros cadastrados.")
        return

    id_livro = input("Digite o ID do livro a ser devolvido: ").strip()

    for livro in livros:
        if livro["identificador"] == id_livro:
            if livro["disponivel"]:
                print(" Erro: Este livro não está emprestado.")
                return
            livro["disponivel"] = True
            print(f" Livro '{livro['titulo']}' devolvido com sucesso!")
            return

    print(" Erro: Livro não encontrado.")