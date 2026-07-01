"""Point d'entrée principal du jeu du Pendu."""

from hangman import Display, HangmanGame, InputValidator, WordLoader, sauvegarder_score, afficher_classement


def demander_pseudo() -> str:
    """Demande et retourne le pseudo du joueur (non vide)."""
    while True:
        pseudo = input("Entrez votre pseudo : ").strip()
        if pseudo:
            return pseudo
        print("Le pseudo ne peut pas être vide.")


def jouer_partie(
    game: HangmanGame,
    display: Display,
    validator: InputValidator,
) -> None:
    """Joue une partie complète jusqu'à victoire ou défaite."""
    display.afficher_nouvelle_partie()

    while not game.partie_terminee:
        display.afficher_pendu(game.nombre_erreurs)
        display.afficher_mot_masque(game.mot_secret, game.lettres_trouvees)
        display.afficher_lettres_proposees(game.lettres_proposees)

        while True:
            try:
                saisie = input("\nProposez une lettre : ")
                lettre = validator.valider(saisie)
                break
            except ValueError as e:
                display.afficher_erreur(str(e))

        if game.proposer_lettre(lettre):
            print(f"Bien joué ! La lettre '{lettre}' est dans le mot.")
        else:
            print(f"Dommage ! La lettre '{lettre}' n'est pas dans le mot.")

    # Afficher le résultat final
    display.afficher_pendu(game.nombre_erreurs)
    display.afficher_mot_masque(game.mot_secret, game.lettres_trouvees)

    if game.victoire:
        display.afficher_victoire(game.mot_secret)
    else:
        display.afficher_defaite(game.mot_secret)


def main() -> None:
    """Fonction principale - boucle de jeu avec replay."""
    word_loader = WordLoader()
    display = Display()
    validator = InputValidator()

    print("\n=== JEU DU PENDU ===")
    joueur = demander_pseudo()

    mot_secret = word_loader.get_random_word()
    game = HangmanGame(mot_secret, erreurs_max=6)

    while True:
        jouer_partie(game, display, validator)

        # Sauvegarder le score dans Supabase
        try:
            sauvegarder_score(joueur, game.mot_secret, game.victoire, game.nombre_erreurs)
            print("Score enregistré !")
        except Exception as e:
            print(f"(Score non enregistré : {e})")

        # Afficher le classement
        afficher_classement()

        if display.demander_rejouer():
            validator.reset()
            mot_secret = word_loader.get_random_word()
            game.reset(mot_secret)
        else:
            print(f"\nMerci d'avoir joué, {joueur} ! Au revoir.")
            break


if __name__ == "__main__":
    main()