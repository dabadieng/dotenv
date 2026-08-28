"""Etape 2a : exploration headless. L'assistant lance ce script.

  python explore.py https://exemple.fr/page [autre-url ...]

Recharge la session capturee a l'etape 1, visite chaque URL et ecrit le
releve (champs, boutons, liens avec leurs libelles accessibles) dans
~/secrets/<site>_explore.txt, que l'assistant lit ensuite.

On passe par un fichier plutot que par la sortie standard parce qu'un releve
de page fait vite plusieurs centaines de lignes.
"""

import sys
from playwright.sync_api import sync_playwright

from a11y_dump import DUMP_JS, format_dump
from session import state_path, out_path


def explore(urls):
    state = state_path(urls[0])
    if not state.exists():
        sys.exit(f"Pas de session : {state}\nLance d'abord capture_session.py")
    out = out_path(urls[0], "explore.txt")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=str(state))
        page = context.new_page()
        blocks = []
        for url in urls:
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
            except Exception as e:
                blocks.append(f"\n==== {url}\n  ERREUR : {e}")
                continue
            d = page.evaluate(DUMP_JS)
            # page.url et non url : une redirection vers le login trahit une
            # session expiree, il faut refaire l'etape 1.
            blocks.append(f"\n==== demande : {url}\n{format_dump(d)}")
        out.write_text("\n".join(blocks), encoding="utf-8")
        print(f"ecrit dans {out}")
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage : python explore.py <url> [url ...]")
    explore(sys.argv[1:])
