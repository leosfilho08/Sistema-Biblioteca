# Cadastro de Livros (feature/cadastro-livros)
def cadastrar_livro(livros):
    print("\n--- Cadastro de Livros ---")
    titulo = input("Digite o título do livro: ").strip()
    identificador = input("Digite o identificador (ID/ISBN): ").strip()
    
    if any(l["identificador"] == identificador for l in livros):
        print(" Erro: Já existe um livro cadastrado com este identificador.")
        return
            
    livros.append({"titulo": titulo, "identificador": identificador, "disponivel": True})
    print(f" Livro '{titulo}' cadastrado com sucesso!")
