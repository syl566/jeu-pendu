# Jeu du Pendu - CLI

Jeu du Pendu jouable dans le terminal, développé en Python 3 sans dépendances externes.

## Fonctionnalités

### Obligatoires (SPEC.md)
- Sélection d'un mot aléatoire depuis une liste prédéfinie (`words.txt`)
- Affichage du mot masqué avec `_`
- Saisie d'une lettre par le joueur
- Révélation des lettres trouvées
- Affichage des lettres déjà proposées (triées)
- Comptage des erreurs
- Détection de la victoire (toutes lettres trouvées)
- Détection de la défaite (6 erreurs max)
- Proposition de rejouer

### Bonus implémentés
- Affichage ASCII du pendu (7 états progressifs)
- Chargement des mots depuis un fichier texte externe
- Code modulaire, lisible et maintenable
- Tests unitaires complets (35 tests)

## Architecture

```
jeu-pendu/
├── main.py                    # Point d'entrée, boucle de jeu + replay
├── words.txt                  # Liste de mots (~150 mots tech/programmation)
├── hangman/
│   ├── __init__.py            # Exports publics
│   ├── game.py                # HangmanGame - logique métier
│   ├── words.py               # WordLoader - chargement mots
│   ├── display.py             # Display - affichage terminal
│   └── input_validator.py     # InputValidator - validation saisie
└── tests/
    ├── test_game.py           # Tests logique (12)
    ├── test_display.py        # Tests affichage (12)
    ├── test_input_validator.py # Tests validation (7)
    └── test_main.py           # Tests intégration (4)
```

### Principes de conception
- **Responsabilité unique** : chaque module a un rôle précis
- **Noms explicites** : variables, fonctions, classes auto-documentées
- **Données métier stockées** : `mot_secret`, `lettres_proposees`, `erreurs_max`
- **Données dérivées calculées** : propriétés `@property` (pas de duplication)
- **Code simple avant code abstrait** : pas de sur-ingénierie

## Installation & Lancement

```bash
# Prérequis : Python 3
python3 main.py
```

## Tests

```bash
# Tous les tests
python3 -m pytest tests/ -v

# Par module
python3 -m pytest tests/test_game.py -v
python3 -m pytest tests/test_display.py -v
python3 -m pytest tests/test_input_validator.py -v
python3 -m pytest tests/test_main.py -v
```

**Résultat : 35 tests passent**

## Modèle de données (HangmanGame)

**État stocké (source de vérité) :**
- `_mot_secret: str` - mot à deviner
- `_lettres_proposees: set[str]` - lettres jouées
- `_erreurs_max: int` - nombre max d'erreurs (défaut: 6)

**Propriétés calculées :**
- `lettres_trouvees` = `_lettres_proposees ∩ set(_mot_secret)`
- `lettres_manquees` = `_lettres_proposees - set(_mot_secret)`
- `nombre_erreurs` = `len(lettres_manquees)`
- `mot_masque` = lettres trouvées révélées, autres en `_`
- `victoire` = `set(_mot_secret) ⊆ _lettres_proposees`
- `defaite` = `nombre_erreurs >= _erreurs_max`
- `partie_terminee` = `victoire or defaite`

## Exemple de partie

```
========================================
NOUVELLE PARTIE - Jeu du Pendu
========================================

  +---+
  |   |
      |
      |
      |
      |
=========

Mot : _ _ _ _ _ _
Lettres proposées : aucune

Proposez une lettre : p
Bien joué ! La lettre 'p' est dans le mot.

  +---+
  |   |
      |
      |
      |
      |
=========

Mot : p _ _ _ _ _
Lettres proposées : p
...
```

## Auteur

Projet développé selon la spécification SPEC.md avec architecture validée étape par étape.