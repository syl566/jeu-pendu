# Jeu du Pendu CLI

## Contexte

Créer un jeu du pendu jouable dans le terminal.

Le joueur doit deviner un mot secret en proposant une lettre à chaque tour.

Le jeu se termine lorsque :

* le mot est entièrement découvert ;
* le nombre maximal d'erreurs est atteint.

## Fonctionnalités

### Obligatoires

* Sélectionner un mot aléatoire dans une liste prédéfinie
* Afficher le mot masqué avec des "_"
* Demander une lettre au joueur
* Révéler les lettres trouvées
* Afficher les lettres déjà proposées
* Compter les erreurs
* Détecter la victoire
* Détecter la défaite
* Proposer de rejouer

### Bonus

* Affichage ASCII du pendu
* Plusieurs niveaux de difficulté
* Chargement des mots depuis un fichier texte
* Statistiques des parties

## Contraintes techniques

* Python 3
* Interface CLI uniquement
* Aucune dépendance externe
* Code lisible et maintenable
* Tests unitaires

## Architecture souhaitée

* responsabilité unique
* noms explicites
* code simple avant code abstrait
* commentaires uniquement si nécessaire

## Critères d'acceptation

* Le jeu démarre sans erreur
* Les entrées utilisateur sont validées
* Le joueur ne peut pas saisir deux fois la même lettre
* Les conditions de victoire et défaite sont correctement détectées
* Les tests passent

## Hors périmètre

* Interface graphique
* Base de données
* Multijoueur réseau

