**Documento de Baseline: Sistema de Biblioteca**

* **Versão:** 1.0.0
* **Data:** 01/09/2026
* **Responsáveis:** Grupo 02 — Equipe de Desenvolvimento
* **Status:** Aprovado

---

**1. Identificação**
Este documento estabelece a baseline formal da versão 1.0.0 do Sistema de Biblioteca, consolidando o código-fonte, a suíte de testes unitários automatizados e os pipelines de CI/CD configurados para GitHub Actions e GitLab CI.

---

**2. Itens de Configuração (ICs)**

| Nome do IC | Tipo | Estado / Versão | Justificativa |
| --- | --- | --- | --- |
| `main.py` | Código Fonte | 1.0.0 | Ponto de entrada do sistema e menu interativo no terminal. |
| `cadastro_usuarios.py` | Código Fonte | 1.0.0 | Módulo para cadastro e consulta de usuários. |
| `cadastro_livros.py` | Código Fonte | 1.0.0 | Módulo para gerenciamento e cadastro do acervo. |
| `emprestimos.py` | Código Fonte | 1.0.0 | Módulo de fluxo e regras de empréstimo. |
| `devolucoes.py` | Código Fonte | 1.0.0 | Módulo de controle e processo de devolução. |
| `tests/test_main.py` | Teste | 1.0.0 | Suíte de testes unitários com *mocks* de I/O. |
| `tests/__init__.py` | Configuração | 1.0.0 | Identificador de pacote para descoberta automática de testes. |
| `.github/workflows/main.yml` | CI/CD | 1.0.0 | Automação de build, testes e deploy no GitHub. |
| `.gitlab-ci.yml` | CI/CD | 1.0.0 | Automação de build, testes e deploy no GitLab. |
| `README.md` | Documentação | Atual | Guia de execução e estrutura do repositório. |

---

**3. Funcionalidades Incluídas**

* Cadastro de usuários e listagem de cadastrados.
* Cadastro de livros e consulta do status de disponibilidade.
* Fluxo de empréstimo e devolução de obras.
* Consulta consolidada de livros atualmente emprestados.
* Validação automática de testes unitários integrada ao fluxo de integração contínua (CI).

---

**4. Ambiente**

* **Linguagem:** Python 3.13
* **Framework de Testes:** `unittest` (nativo)
* **Ferramentas de CI/CD:** GitHub Actions e GitLab CI/CD
* **Dependências Externas:** Nenhuma (utiliza apenas a biblioteca padrão do Python)

---

**5. Limitações Conhecidas**

* Armazenamento temporário de dados em memória (sem persistência em banco de dados ou arquivos).
* Interface de usuário exclusivamente em linha de comando (CLI).
