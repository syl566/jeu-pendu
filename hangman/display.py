"""Affichage du jeu du Pendu."""

from hangman.input_validator import InputValidator


PENDU_ASCII = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
]


class Display:
    """Gère l'affichage du jeu dans le terminal."""

    def __init__(self) -> None:
        pass

    def afficher_pendu(self, erreurs: int) -> None:
        """Affiche le pendu selon le nombre d'erreurs (0-6)."""
        index = min(erreurs, len(PENDU_ASCII) - 1)
        print(PENDU_ASCII[index])

    def afficher_mot_masque(self, mot_secret: str, lettres_trouvees: set[str]) -> None:
        """Affiche le mot avec lettres trouvées révélées et autres masquées."""
        masque = " ".join(
            lettre if lettre in lettres_trouvees else "_"
            for lettre in mot_secret
        )
        print(f"Mot : {masque}")

    def afficher_lettres_proposees(self, lettres_proposees: set[str]) -> None:
        """Affiche les lettres déjà proposées, triées."""
        if lettres_proposees:
            lettres_triees = sorted(lettres_proposees)
            print(f"Lettres proposées : {', '.join(lettres_triees)}")
        else:
            print("Lettres proposées : aucune")

    def afficher_erreur(self, message: str) -> None:
        """Affiche un message d'erreur."""
        print(f"Erreur : {message}")

    def afficher_victoire(self, mot_secret: str) -> None:
        """Affiche le message de victoire."""
        print(f"\nBravo ! Vous avez trouvé le mot : {mot_secret}")

    def afficher_defaite(self, mot_secret: str) -> None:
        """Affiche le message de défaite."""
        print(f"\nPerdu ! Le mot était : {mot_secret}")

    def afficher_nouvelle_partie(self) -> None:
        """Affiche l'en-tête d'une nouvelle partie."""
        print("\n" + "=" * 40)
        print("NOUVELLE PARTIE - Jeu du Pendu")
        print("=" * 40)

    def demander_rejouer(self) -> bool:
        """Demande si le joueur veut rejouer. Retourne True pour oui."""
        while True:
            reponse = input("\nVoulez-vous rejouer ? (o/n) : ").strip().lower()
            if reponse in ("o", "oui", "y", "yes"):
                return True
            if reponse in ("n", "non", "no"):
                return False
            print("Réponse invalide. Entrez 'o' pour oui ou 'n' pour non.")