"""Tests d'intégration pour le jeu complet."""

import io
from contextlib import redirect_stdout
from unittest.mock import patch

from hangman import Display, HangmanGame, InputValidator
from main import jouer_partie


class TestIntegration:
    """Tests d'intégration du jeu complet."""

    def setup_method(self) -> None:
        self.display = Display()
        self.validator = InputValidator()

    def test_partie_complete_victoire(self) -> None:
        """Test une partie complète gagnée."""
        game = HangmanGame("python", erreurs_max=6)
        inputs = iter(["p", "y", "t", "h", "o", "n"])

        with patch("builtins.input", side_effect=inputs):
            with io.StringIO() as buf, redirect_stdout(buf):
                jouer_partie(game, self.display, self.validator)
                output = buf.getvalue()

        assert "Bravo" in output
        assert "python" in output

    def test_partie_complete_defaite(self) -> None:
        """Test une partie complète perdue."""
        game = HangmanGame("python", erreurs_max=3)
        inputs = iter(["a", "b", "c"])

        with patch("builtins.input", side_effect=inputs):
            with io.StringIO() as buf, redirect_stdout(buf):
                jouer_partie(game, self.display, self.validator)
                output = buf.getvalue()

        assert "Perdu" in output
        assert "python" in output

    def test_validation_saisie_invalide_puis_valide(self) -> None:
        """Test que les saisies invalides sont rejetées puis une valide acceptée."""
        game = HangmanGame("python", erreurs_max=6)
        inputs = iter(["12", "ab", "!", "p", "y", "t", "h", "o", "n"])

        with patch("builtins.input", side_effect=inputs):
            with io.StringIO() as buf, redirect_stdout(buf):
                jouer_partie(game, self.display, self.validator)
                output = buf.getvalue()

        assert "Erreur" in output
        assert "Bien joué" in output
        assert "Bravo" in output

    def test_reset_nouvelle_partie(self) -> None:
        """Test le reset pour une nouvelle partie."""
        game = HangmanGame("test", erreurs_max=6)
        game.proposer_lettre("t")
        game.reset("nouveau")
        assert game.mot_secret == "nouveau"
        assert game.lettres_proposees == set()