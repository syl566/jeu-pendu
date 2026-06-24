"""Point d'entrée principal du jeu du Pendu."""

from hangman.words import WordLoader


def main() -> None:
    """Fonction principale - à implémenter plus tard."""
    loader = WordLoader()
    word = loader.get_random_word()
    print(f"Mot sélectionné pour test: {word}")


if __name__ == "__main__":
    main()