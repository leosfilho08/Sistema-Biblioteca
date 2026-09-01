import io
import unittest
from unittest.mock import MagicMock, patch

# Importa as funções do arquivo principal (supondo que o arquivo se chame main.py)
from main import exibir_menu, listar_livros, listar_usuarios, main


class TestSistemaBibliotecaMain(unittest.TestCase):

    # -------------------------------------------------------------------------
    # Testes para listar_usuarios
    # -------------------------------------------------------------------------
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_listar_usuarios_vazio(self, mock_stdout):
        usuarios = []
        listar_usuarios(usuarios)
        saida = mock_stdout.getvalue()

        self.assertIn("--- Usuários Cadastrados ---", saida)
        self.assertIn("Nenhum usuário cadastrado.", saida)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_listar_usuarios_com_dados(self, mock_stdout):
        usuarios = [
            {"nome": "Alice", "identificador": "1"},
            {"nome": "Bob", "identificador": "2"},
        ]
        listar_usuarios(usuarios)
        saida = mock_stdout.getvalue()

        self.assertIn("Nome: Alice | ID: 1", saida)
        self.assertIn("Nome: Bob | ID: 2", saida)

    # -------------------------------------------------------------------------
    # Testes para listar_livros
    # -------------------------------------------------------------------------
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_listar_livros_vazio(self, mock_stdout):
        livros = []
        listar_livros(livros)
        saida = mock_stdout.getvalue()

        self.assertIn("--- Livros Cadastrados ---", saida)
        self.assertIn("Nenhum livro cadastrado.", saida)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_listar_livros_com_dados(self, mock_stdout):
        livros = [
            {"titulo": "Dom Casmurro", "identificador": "101", "disponivel": True},
            {"titulo": "1984", "identificador": "102", "disponivel": False},
        ]
        listar_livros(livros)
        saida = mock_stdout.getvalue()

        self.assertIn("Título: Dom Casmurro | ID: 101 | Status: Disponível", saida)
        self.assertIn("Título: 1984 | ID: 102 | Status: Emprestado", saida)

    # -------------------------------------------------------------------------
    # Teste para exibir_menu
    # -------------------------------------------------------------------------
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exibir_menu(self, mock_stdout):
        exibir_menu()
        saida = mock_stdout.getvalue()

        self.assertIn("=== Sistema de Biblioteca ===", saida)
        self.assertIn("1. Cadastrar usuário", saida)
        self.assertIn("0. Sair", saida)

    # -------------------------------------------------------------------------
    # Testes de fluxo da função main()
    # -------------------------------------------------------------------------
    @patch("main.cadastrar_usuario")
    @patch("builtins.input", side_effect=["1", "0"])
    def test_main_opcao_1_cadastrar_usuario(self, mock_input, mock_cadastrar_usuario):
        main()
        mock_cadastrar_usuario.assert_called_once_with([])

    @patch("main.cadastrar_livro")
    @patch("builtins.input", side_effect=["2", "0"])
    def test_main_opcao_2_cadastrar_livro(self, mock_input, mock_cadastrar_livro):
        main()
        mock_cadastrar_livro.assert_called_once_with([])

    @patch("main.realizar_emprestimo")
    @patch("builtins.input", side_effect=["3", "0"])
    def test_main_opcao_3_realizar_emprestimo(self, mock_input, mock_realizar_emprestimo):
        main()
        mock_realizar_emprestimo.assert_called_once_with([], [])

    @patch("main.devolver_livro")
    @patch("builtins.input", side_effect=["4", "0"])
    def test_main_opcao_4_devolver_livro(self, mock_input, mock_devolver_livro):
        main()
        mock_devolver_livro.assert_called_once_with([])

    @patch("main.listar_usuarios")
    @patch("builtins.input", side_effect=["5", "0"])
    def test_main_opcao_5_listar_usuarios(self, mock_input, mock_listar_usuarios):
        main()
        mock_listar_usuarios.assert_called_once_with([])

    @patch("main.listar_livros")
    @patch("builtins.input", side_effect=["6", "0"])
    def test_main_opcao_6_listar_livros(self, mock_input, mock_listar_livros):
        main()
        mock_listar_livros.assert_called_once_with([])

    @patch("main.consultar_emprestados")
    @patch("builtins.input", side_effect=["7", "0"])
    def test_main_opcao_7_consultar_emprestados(self, mock_input, mock_consultar_emprestados):
        main()
        mock_consultar_emprestados.assert_called_once_with([])

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["99", "0"])
    def test_main_opcao_invalida(self, mock_input, mock_stdout):
        main()
        saida = mock_stdout.getvalue()
        self.assertIn("Opção inválida. Tente novamente.", saida)


if __name__ == "__main__":
    unittest.main()