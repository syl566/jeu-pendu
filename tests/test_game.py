"""Tests pour HangmanGame."""

import pytest
from hangman.game import HangmanGame


class TestHangmanGame:
    """Tests de la logique du jeu."""

    def setup_method(self) -> None:
        self.game = HangmanGame("python", erreurs_max=6)

    def test_initialisation(self) -> None:
        assert self.game.mot_secret == "python"
        assert self.game.erreurs_max == 6
        assert self.game.lettres_proposees == set()
        assert self.game.lettres_trouvees == set()
        assert self.game.nombre_erreurs == 0
        assert self.game.mot_masque == "_ _ _ _ _ _"
        assert not self.game.victoire
        assert not self.game.defaite
        assert not self.game.partie_terminee

    def test_proposer_lettre_dans_mot(self) -> None:
        resultat = self.game.proposer_lettre("p")
        assert resultat is True
        assert "p" in self.game.lettres_proposees
        assert self.game.lettres_trouvees == {"p"}
        assert self.game.mot_masque == "p _ _ _ _ _"
        assert self.game.nombre_erreurs == 0

    def test_proposer_lettre_pas_dans_mot(self) -> None:
        resultat = self.game.proposer_lettre("z")
        assert resultat is False
        assert "z" in self.game.lettres_proposees
        assert self.game.lettres_trouvees == set()
        assert self.game.lettres_manquees == {"z"}
        assert self.game.nombre_erreurs == 1
        assert self.game.mot_masque == "_ _ _ _ _ _"

    def test_proposer_plusieurs_lettres(self) -> None:
        self.game.proposer_lettre("p")
        self.game.proposer_lettre("y")
        self.game.proposer_lettre("z")
        assert self.game.lettres_trouvees == {"p", "y"}
        assert self.game.lettres_manquees == {"z"}
        assert self.game.nombre_erreurs == 1
        assert self.game.mot_masque == "p y _ _ _ _"

    def test_victoire_toutes_lettres_trouvees(self) -> None:
        for lettre in "python":
            self.game.proposer_lettre(lettre)
        assert self.game.victoire is True
        assert self.game.partie_terminee is True
        assert self.game.defaite is False

    def test_defaite_erreurs_max_atteint(self) -> None:
        for lettre in "abcdef":  # 6 lettres fausses
            self.game.proposer_lettre(lettre)
        assert self.game.defaite is True
        assert self.game.partie_terminee is True
        assert self.game.victoire is False
        assert self.game.nombre_erreurs == 6

    def test_defaite_avant_toutes_lettres_fausses(self) -> None:
        game = HangmanGame("python", erreurs_max=3)
        for lettre in "abc":
            game.proposer_lettre(lettre)
        assert game.defaite is True
        assert game.nombre_erreurs == 3

    def test_reset_gardeme_mot(self) -> None:
        self.game.proposer_lettre("p")
        self.game.proposer_lettre("z")
        self.game.reset()
        assert self.game.lettres_proposees == set()
        assert self.game.mot_secret == "python"
        assert self.game.mot_masque == "_ _ _ _ _ _"

    def test_reset_nouveau_mot(self) -> None:
        self.game.proposer_lettre("p")
        self.game.reset("java")
        assert self.game.mot_secret == "java"
        assert self.game.mot_masque == "_ _ _ _"
        assert self.game.lettres_proposees == set()

    def test_lettres_proposees_est_copie(self) -> None:
        lettres = self.game.lettres_proposees
        lettres.add("x")
        assert "x" not in self.game.lettres_proposees

    def test_insensible_casse(self) -> None:
        self.game.proposer_lettre("P")
        self.game.proposer_lettre("Y")
        assert self.game.lettres_trouvees == {"p", "y"}
        assert self.game.mot_masque == "p y _ _ _ _"

    def test_mot_avec_lettres_dupliquees(self) -> None:
        game = HangmanGame("lettre")
        game.proposer_lettre("t")
        assert game.mot_masque == "_ _ t t _ _"
        game.proposer_lettre("e")
        assert game.mot_masque == "_ e t t _ e"