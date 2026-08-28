"""Etape 1 : capture de session. C'est TOI qui lances ce script.

  python capture_session.py https://exemple.fr/login

Un navigateur VISIBLE s'ouvre sur l'URL. Tu te connectes a la main, puis tu
reviens dans le terminal et tu tapes Entree. Le script enregistre alors tes
cookies dans ~/secrets/<site>_state.json et releve la structure de la page
ou tu t'es arretee.

Ton mot de passe n'est jamais lu ni stocke : tu le tapes dans le navigateur,
seuls les cookies sont sauves. A partir de la, l'assistant peut piloter le
site en headless avec explore.py et fetch_api.py, sans toi.

Pourquoi c'est toi qui lances : l'attente par input() bloquerait un appel
lance par l'assistant, et le mot de passe doit venir de toi seule.
"""

import sys
from playwright.sync_api import sync_playwright

from a11y_dump import DUMP_JS, format_dump
from session import SECRETS_DIR, state_path, out_path


def capture(url):
    SECRETS_DIR.mkdir(parents=True, exist_ok=True)
    state = state_path(url)
    dump = out_path(url, "form.txt")

    with sync_playwright() as p:
        # slow_mo : laisse le temps a VoiceOver de suivre les changements de page.
        browser = p.chromium.launch(headless=False, slow_mo=80)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        print("\n" + "=" * 60)
        print("Dans le navigateur qui vient de s'ouvrir :")
        print("  1) connecte-toi,")
        print("  2) va jusqu'a la page qui t'interesse.")
        print("Quand tu y es, reviens ici et appuie sur Entree.")
        print("=" * 60)
        input("\n>>> Entree quand tu es sur la bonne page... ")

        # storage_state prend les cookies de TOUT le contexte : peu importe
        # l'onglet ou le sous-domaine ou tu as fini, l'auth est capturee.
        context.storage_state(path=str(state))
        print(f"Session sauvegardee : {state}")

        d = page.evaluate(DUMP_JS)
        dump.write_text(format_dump(d), encoding="utf-8")
        print(f"Structure relevee : {dump} ({len(d['fields'])} champs)")
        print("\nC'est bon, tu peux prevenir l'assistant : il lit ces deux fichiers.")

        input("\n>>> Entree pour fermer le navigateur... ")
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage : python capture_session.py <url de connexion>")
    capture(sys.argv[1])
