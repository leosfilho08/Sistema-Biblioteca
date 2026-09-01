def realizar_emprestimo(usuarios, livros):
    print("\n--- Empréstimo de Livros ---")
    if not usuarios or not livros:
        print(" Atenção: É necessário ter usuários e livros cadastrados.")
        return

    id_usuario = input("Digite o ID do usuário: ").strip()
    if not any(u["identificador"] == id_usuario for u in usuarios):
        print(" Erro: Usuário não encontrado.")
        return

    id_livro = input("Digite o ID do livro: ").strip()
    for livro in livros:
        if livro["identificador"] == id_livro:
            if livro["disponivel"]:
                livro["disponivel"] = False
                print(f" Livro '{livro['titulo']}' emprestado com sucesso!")
                return
            print(" Erro: Este livro já está emprestado.")
            return
            
    print(" Erro: Livro não encontrado.")
