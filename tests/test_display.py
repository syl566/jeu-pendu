"""Tests pour Display."""

import io
import sys
from contextlib import redirect_stdout
from hangman.display import Display, PENDU_ASCII


class TestDisplay:
    """Tests d'affichage."""

    def setup_method(self) -> None:
        self.display = Display()

    def _capture_output(self, func, *args, **kwargs) -> str:
        """Capture la sortie stdout d'une fonction."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            func(*args, **kwargs)
        return buffer.getvalue()

    def test_afficher_pendu_indices_valides(self) -> None:
        for i in range(7):
            output = self._capture_output(self.display.afficher_pendu, i)
            assert "=========" in output
            assert "+---+" in output

    def test_afficher_pendu_index_superieur_max(self) -> None:
        output = self._capture_output(self.display.afficher_pendu, 10)
        assert "=========" in output

    def test_afficher_mot_masque_tout_masque(self) -> None:
        output = self._capture_output(self.display.afficher_mot_masque, "python", set())
        assert "Mot : _ _ _ _ _ _" in output

    def test_afficher_mot_masque_lettres_trouvees(self) -> None:
        output = self._capture_output(
            self.display.afficher_mot_masque, "python", {"p", "t", "h", "o", "n"}
        )
        assert "Mot : p _ t h o n" in output

    def test_afficher_mot_masque_tout_trouve(self) -> None:
        output = self._capture_output(
            self.display.afficher_mot_masque, "python", {"p", "y", "t", "h", "o", "n"}
        )
        assert "Mot : p y t h o n" in output

    def test_afficher_lettres_proposees_vide(self) -> None:
        output = self._capture_output(self.display.afficher_lettres_proposees, set())
        assert "Lettres proposées : aucune" in output

    def test_afficher_lettres_proposees_plusieurs(self) -> None:
        output = self._capture_output(
            self.display.afficher_lettres_proposees, {"e", "a", "z"}
        )
        assert "Lettres proposées : a, e, z" in output

    def test_afficher_erreur(self) -> None:
        output = self._capture_output(self.display.afficher_erreur, "Test erreur")
        assert "Erreur : Test erreur" in output

    def test_afficher_victoire(self) -> None:
        output = self._capture_output(self.display.afficher_victoire, "python")
        assert "Bravo" in output
        assert "python" in output

    def test_afficher_defaite(self) -> None:
        output = self._capture_output(self.display.afficher_defaite, "python")
        assert "Perdu" in output
        assert "python" in output

    def test_afficher_nouvelle_partie(self) -> None:
        output = self._capture_output(self.display.afficher_nouvelle_partie)
        assert "NOUVELLE PARTIE" in output
        assert "Jeu du Pendu" in output

    def test_pendu_ascii_complet(self) -> None:
        assert len(PENDU_ASCII) == 7
        for art in PENDU_ASCII:
            assert "+---+" in art
            assert "=========" in art