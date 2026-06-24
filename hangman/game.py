"""Logique principale du jeu du Pendu."""


class HangmanGame:
    """Gère l'état et la logique d'une partie de Pendu."""

    def __init__(self, mot_secret: str, erreurs_max: int = 6) -> None:
        """
        Initialise une nouvelle partie.

        Args:
            mot_secret: Le mot à deviner.
            erreurs_max: Nombre maximal d'erreurs autorisées (défaut: 6).
        """
        self._mot_secret = mot_secret.lower()
        self._lettres_proposees: set[str] = set()
        self._erreurs_max = erreurs_max

    @property
    def mot_secret(self) -> str:
        return self._mot_secret

    @property
    def erreurs_max(self) -> int:
        return self._erreurs_max

    @property
    def lettres_proposees(self) -> set[str]:
        return self._lettres_proposees.copy()

    @property
    def lettres_trouvees(self) -> set[str]:
        return self._lettres_proposees & set(self._mot_secret)

    @property
    def lettres_manquees(self) -> set[str]:
        return self._lettres_proposees - set(self._mot_secret)

    @property
    def nombre_erreurs(self) -> int:
        return len(self.lettres_manquees)

    @property
    def mot_masque(self) -> str:
        return " ".join(
            lettre if lettre in self.lettres_trouvees else "_"
            for lettre in self._mot_secret
        )

    @property
    def victoire(self) -> bool:
        return set(self._mot_secret).issubset(self._lettres_proposees)

    @property
    def defaite(self) -> bool:
        return self.nombre_erreurs >= self._erreurs_max

    @property
    def partie_terminee(self) -> bool:
        return self.victoire or self.defaite

    def proposer_lettre(self, lettre: str) -> bool:
        """
        Propose une lettre et met à jour l'état du jeu.

        Args:
            lettre: La lettre proposée (déjà validée).

        Returns:
            True si la lettre est dans le mot, False sinon.
        """
        lettre = lettre.lower()
        self._lettres_proposees.add(lettre)
        return lettre in self._mot_secret

    def reset(self, mot_secret: str | None = None) -> None:
        """
        Réinitialise la partie pour un nouveau mot.

        Args:
            mot_secret: Nouveau mot secret (optionnel, garde l'actuel si None).
        """
        self._lettres_proposees.clear()
        if mot_secret is not None:
            self._mot_secret = mot_secret.lower()