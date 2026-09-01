

# Sistema de Gerenciamento de Biblioteca

Sistema em Python via terminal para automação e controle de cadastro de usuários, acervo de livros, empréstimos, devoluções e consulta de status.

Desenvolvido como parte da atividade prática de **Criação e Gerenciamento de uma Baseline**, aplicando práticas de **Git Flow** e **Gerência de Configuração de Software (GCS)**.

---

## Funcionalidades

* **Cadastro de Usuários:** Registro com verificação de ID único.
* **Cadastro de Livros:** Controle de acervo com identificador (ID/ISBN) e status de disponibilidade.
* **Empréstimo de Livros:** Associação de usuários a livros disponíveis, impedindo a locação de itens indisponíveis.
* **Devolução de Livros:** Atualização imediata do status do acervo.
* **Consulta e Relatórios:** Listagem de livros emprestados e relatório geral de acervo e usuários cadastrados.

---

## Organização das Branches e Responsabilidades

| Funcionalidade | Branch | Responsável | Status |
| --- | --- | --- | --- |
| **Cadastro de Usuários** | `feature/cadastro_usuarios` | Emerson | Concluído |
| **Cadastro de Livros** | `feature/cadastro_livros` | Leonardo | Concluído |
| **Empréstimos** | `feature/emprestimos` | Vinicius | Concluído |
| **Devoluções** | `feature/devolucoes` | Hallana | Concluído |

---

## Execução do Projeto

### Pré-requisitos

* Python 3.10 ou superior.
* Nenhuma dependência externa adicional necessária.

### Passo a Passo

1. **Clonar o repositório:**
```bash
git clone https://gitlab.com/leosfilho08/sistema-biblioteca.git
cd sistema-biblioteca

```


2. **Executar o sistema Windows:**
```bash
python main.py

```

**Executar o sistema Linux/MacOS:**
```bash
python3 ./main.py

```



### Interface de Uso

Ao executar, o menu interativo será exibido no terminal:

```text
=== Sistema de Biblioteca ===
1. Cadastrar usuário
2. Cadastrar livro
3. Emprestar livro
4. Devolver livro
5. Listar usuários
6. Listar livros
7. Consultar livros emprestados
8. Sair

```

---

## Estrutura do Projeto

```text
sistema-biblioteca/
├── main.py               # Ponto de entrada — integração dos módulos
├── cadastro.py           # Gestão e consulta de usuários
├── cadastro_livros.py   # Gestão do acervo de livros
├── emprestimos.py       # Regras de empréstimo de livros
├── devolucoes.py         # Regras de devolução de livros
├── docs/
│   └── baseline-v1.0.0.md # Documentação formal da baseline oficial
└── README.md             # Documentação do repositório

```

---

## Baseline (v1.0.0)

A release **v1.0.0** representa a primeira **baseline oficial**, estável e aprovada do sistema, integrando as cinco funcionalidades principais testadas.

Os detalhes sobre os Itens de Configuração (ICs), ambiente de execução e histórico de controle encontram-se em [`docs/baseline-v1.0.0.md`]
A tag `v1.0.0` no Git marca o commit correspondente a esse estado aprovado.

---

## Limitações Conhecidas

* **Persistência de Dados:** Os dados são mantidos em memória durante a execução; ao fechar o programa, as informações são redefinidas.
* **Autenticação:** Não há controle de acesso ou logins diferenciados.
* **Gestão de Cadastros:** O sistema não possui recursos de edição ou exclusão de usuários e livros já registrados.

---

## Autores

* Emerson Carlos
* Leonardo Souza
* Vinicius
* Hallana