"""Etape 2b : appeler l'API du site avec la session, sans passer par l'ecran.

  python fetch_api.py https://exemple.fr/api/mon-contenu/export [fichier-sortie]

context.request reutilise les cookies de la session : on recupere donc du
JSON ou du CSV directement, en une requete.

C'est la voie a privilegier quand le site expose un export et un import du
meme format : recuperer l'export, le modifier, le reimporter est bien plus
fiable que de cliquer champ par champ dans une interface qui se regenere.
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

from session import state_path, out_path


def fetch(url, dest=None):
    state = state_path(url)
    if not state.exists():
        sys.exit(f"Pas de session : {state}\nLance d'abord capture_session.py")
    dest = Path(dest) if dest else out_path(url, "fetch.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=str(state))
        r = context.request.get(url)
        body = r.body()
        dest.write_bytes(body)
        print(f"status={r.status} taille={len(body)} octets -> {dest}")
        # Un 200 qui rend du HTML de login = session expiree, pas un succes.
        if r.status != 200:
            print("ATTENTION : statut inattendu, verifie le contenu du fichier.")
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage : python fetch_api.py <url> [fichier-sortie]")
    fetch(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
