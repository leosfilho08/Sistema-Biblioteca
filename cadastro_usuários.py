# Cadastro de Usuários (feature/cadastro-usuarios)
def cadastrar_usuario(usuarios):
    print("\n--- Cadastro de Usuários ---")
    nome = input("Digite o nome do usuário: ").strip()
    identificador = input("Digite o identificador (ID): ").strip()
    
    if any(u["identificador"] == identificador for u in usuarios):
        print(" Erro: Já existe um usuário cadastrado com este identificador.")
        return
        
    usuarios.append({"nome": nome, "identificador": identificador})
    print(f" Usuário '{nome}' cadastrado com sucesso!")


# Consulta de Livros Emprestados (feature/consultas)
def consultar_emprestados(livros):
    print("\n--- Livros Emprestados ---")
    emprestados = [l for l in livros if not l["disponivel"]]
    
    if not emprestados:
        print("Nenhum livro emprestado no momento.")
        return
        
    for l in emprestados:
        print(f" Título: {l['titulo']} | ID: {l['identificador']}")