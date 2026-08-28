"""Emplacement des sessions capturees.

Une session = les cookies d'un site apres connexion. C'est un secret vivant :
qui l'a est connecte a ta place. Donc ces fichiers vivent dans ~/secrets,
jamais dans un depot Git (le .gitignore de ce depot les refuse aussi).
"""

import re
from pathlib import Path
from urllib.parse import urlparse

SECRETS_DIR = Path.home() / "secrets"


def slug(url_or_name):
    """doyoubuzz.com/fr -> doyoubuzz_com ; sert a nommer les fichiers."""
    host = urlparse(url_or_name).netloc or url_or_name
    return re.sub(r"[^a-z0-9]+", "_", host.lower()).strip("_") or "site"


def state_path(site):
    """Chemin du fichier de session pour un site."""
    return SECRETS_DIR / f"{slug(site)}_state.json"


def out_path(site, suffix):
    """Chemin d'un relevé (dump) pour un site : ..._explore.txt, _form.txt, etc."""
    return SECRETS_DIR / f"{slug(site)}_{suffix}"
