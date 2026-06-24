"""Validation de la saisie utilisateur."""


class InputValidator:
    """Valide la saisie d'une lettre par le joueur."""

    def __init__(self) -> None:
        self._lettres_proposees: set[str] = set()

    def valider(self, saisie: str) -> str:
        """
        Valide la saisie utilisateur.

        Args:
            saisie: Chaîne saisie par l'utilisateur.

        Returns:
            La lettre validée en minuscule.

        Raises:
            ValueError: Si la saisie est invalide.
        """
        lettre = saisie.strip().lower()

        if not lettre:
            raise ValueError("Saisie vide. Entrez une lettre.")

        if len(lettre) != 1:
            raise ValueError("Entrez une seule lettre.")

        if not lettre.isalpha():
            raise ValueError("Entrez une lettre de l'alphabet (a-z).")

        if lettre in self._lettres_proposees:
            raise ValueError(f"La lettre '{lettre}' a déjà été proposée.")

        self._lettres_proposees.add(lettre)
        return lettre

    def reset(self) -> None:
        """Réinitialise l'historique pour une nouvelle partie."""
        self._lettres_proposees.clear()

    def lettres_proposees(self) -> set[str]:
        """Retourne l'ensemble des lettres déjà proposées."""
        return self._lettres_proposees.copy()