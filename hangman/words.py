"""Gestion du chargement et de la sélection des mots."""

import random
from pathlib import Path


class WordLoader:
    """Charge une liste de mots depuis un fichier et sélectionne un mot aléatoire."""

    def __init__(self, filepath: str = "words.txt") -> None:
        self.filepath = Path(filepath)
        self._words: list[str] = []
        self._load()

    def _load(self) -> None:
        """Charge les mots depuis le fichier."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Fichier de mots introuvable: {self.filepath}")
        
        with self.filepath.open("r", encoding="utf-8") as f:
            self._words = [line.strip().lower() for line in f if line.strip()]

        if not self._words:
            raise ValueError("Aucun mot valide dans le fichier")

    def get_random_word(self) -> str:
        """Retourne un mot aléatoire depuis la liste chargée."""
        return random.choice(self._words)

    def get_words(self) -> list[str]:
        """Retourne la liste complète des mots chargés."""
        return self._words.copy()