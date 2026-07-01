"""Gestion des scores via Supabase."""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

_client: Client | None = None


def _get_client() -> Client:
    global _client
    if _client is None:
        url = os.environ["SUPABASE_URL"]
        key = os.environ["SUPABASE_KEY"]
        _client = create_client(url, key)
    return _client


def sauvegarder_score(joueur: str, mot: str, victoire: bool, nb_erreurs: int) -> None:
    """Envoie le résultat d'une partie à Supabase."""
    _get_client().table("scores").insert({
        "joueur": joueur,
        "mot": mot,
        "victoire": victoire,
        "nb_erreurs": nb_erreurs,
    }).execute()


def get_classement(limite: int = 10) -> list[dict]:
    """
    Retourne le classement : joueurs triés par victoires décroissantes,
    puis par moyenne d'erreurs croissante.
    """
    response = (
        _get_client()
        .table("scores")
        .select("joueur, victoire, nb_erreurs")
        .execute()
    )

    # Agréger par joueur
    stats: dict[str, dict] = {}
    for row in response.data:
        nom = row["joueur"]
        if nom not in stats:
            stats[nom] = {"joueur": nom, "victoires": 0, "parties": 0, "total_erreurs": 0}
        stats[nom]["parties"] += 1
        stats[nom]["total_erreurs"] += row["nb_erreurs"]
        if row["victoire"]:
            stats[nom]["victoires"] += 1

    classement = []
    for s in stats.values():
        s["moy_erreurs"] = round(s["total_erreurs"] / s["parties"], 1)
        classement.append(s)

    classement.sort(key=lambda x: (-x["victoires"], x["moy_erreurs"]))
    return classement[:limite]


def afficher_classement() -> None:
    """Affiche le classement dans le terminal."""
    classement = get_classement()
    if not classement:
        print("\nAucun score enregistré pour l'instant.")
        return

    print("\n" + "=" * 45)
    print(f"{'#':<4} {'Joueur':<15} {'Victoires':<12} {'Parties':<10} {'Moy. erreurs'}")
    print("=" * 45)
    for i, s in enumerate(classement, 1):
        print(f"{i:<4} {s['joueur']:<15} {s['victoires']:<12} {s['parties']:<10} {s['moy_erreurs']}")
    print("=" * 45)