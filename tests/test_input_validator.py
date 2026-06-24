"""Tests pour InputValidator."""

import pytest
from hangman.input_validator import InputValidator


class TestInputValidator:
    """Tests de validation de saisie."""

    def setup_method(self) -> None:
        self.validator = InputValidator()

    def test_valider_lettre_valide(self) -> None:
        assert self.validator.valider("a") == "a"
        assert self.validator.valider("Z") == "z"
        assert self.validator.valider(" e ") == "e"

    def test_valider_saisie_vide(self) -> None:
        with pytest.raises(ValueError, match="Saisie vide"):
            self.validator.valider("")
        with pytest.raises(ValueError, match="Saisie vide"):
            self.validator.valider("   ")

    def test_valider_plusieurs_caracteres(self) -> None:
        with pytest.raises(ValueError, match="une seule lettre"):
            self.validator.valider("ab")
        with pytest.raises(ValueError, match="une seule lettre"):
            self.validator.valider("abc")

    def test_valider_non_alphabetique(self) -> None:
        with pytest.raises(ValueError, match="alphabet"):
            self.validator.valider("1")
        with pytest.raises(ValueError, match="alphabet"):
            self.validator.valider("@")
        with pytest.raises(ValueError, match="alphabet"):
            self.validator.valider("!")

    def test_valider_lettre_deja_proposee(self) -> None:
        self.validator.valider("a")
        with pytest.raises(ValueError, match="déjà été proposée"):
            self.validator.valider("a")
        with pytest.raises(ValueError, match="déjà été proposée"):
            self.validator.valider("A")

    def test_reset(self) -> None:
        self.validator.valider("a")
        self.validator.valider("b")
        self.validator.reset()
        assert self.validator.valider("a") == "a"

    def test_lettres_proposees(self) -> None:
        self.validator.valider("a")
        self.validator.valider("b")
        assert self.validator.lettres_proposees() == {"a", "b"}