"""
Lecture du trousseau de mots de passe Firefox, en local.

Usage accessibilite : ses propres identifiants, sur son propre poste. Rien
n'est envoye nulle part, le dechiffrement se fait avec la bibliotheque NSS
livree avec Firefox.

  python firefox_mdp.py            -> cherche "inpi"
  python firefox_mdp.py urssaf     -> cherche un autre motif
  python firefox_mdp.py --tout     -> liste seulement les sites (sans mot de passe)

Si un mot de passe principal Firefox est defini, le script le demande.
Le profil est copie dans un dossier temporaire pour ne pas se heurter aux
verrous poses par un Firefox ouvert.
"""

import ctypes
import json
import base64
import shutil
import sys
import tempfile
from getpass import getpass
from pathlib import Path

NSS_LIB = "/Applications/Firefox.app/Contents/MacOS/libnss3.dylib"
PROFILES = Path.home() / "Library/Application Support/Firefox/Profiles"


class SECItem(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("data", ctypes.c_void_p),
        ("len", ctypes.c_uint),
    ]


def find_profile():
    """Profil contenant le plus grand logins.json (le profil reellement utilise)."""
    candidates = []
    for d in PROFILES.glob("*"):
        f = d / "logins.json"
        if f.exists():
            candidates.append((f.stat().st_size, d))
    if not candidates:
        sys.exit("Aucun profil Firefox avec des mots de passe enregistres.")
    return sorted(candidates)[-1][1]


def get_logins(motif):
    """Retourne [(site, identifiant, mot_de_passe)] pour les entrees contenant motif.

    Utilisable par d'autres scripts pour ne jamais ecrire un mot de passe en clair
    dans un fichier ou une ligne de commande.
    """
    return _read(motif.lower(), list_only=False, echo=False)


def main():
    args = [a for a in sys.argv[1:]]
    list_only = "--tout" in args
    motif = next((a for a in args if not a.startswith("--")), "inpi").lower()
    _read(motif, list_only, echo=True)


def _read(motif, list_only, echo):
    profile = find_profile()
    logins = json.loads((profile / "logins.json").read_text())["logins"]

    # Copie du profil : evite les verrous SQLite si Firefox est ouvert.
    tmp = Path(tempfile.mkdtemp(prefix="ffprofile_"))
    for name in ("key4.db", "cert9.db", "logins.json", "pkcs11.txt"):
        src = profile / name
        if src.exists():
            shutil.copy2(src, tmp / name)

    # libnss3 depend de libmozglue, livree a cote : la charger d'abord en global,
    # sinon dlopen echoue en cherchant @rpath/libmozglue.dylib.
    glue = Path(NSS_LIB).parent / "libmozglue.dylib"
    if glue.exists():
        ctypes.CDLL(str(glue), mode=ctypes.RTLD_GLOBAL)
    nss = ctypes.CDLL(NSS_LIB)
    nss.NSS_Init.argtypes = [ctypes.c_char_p]
    nss.NSS_Init.restype = ctypes.c_int
    nss.PK11_GetInternalKeySlot.restype = ctypes.c_void_p
    nss.PK11_Authenticate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    nss.PK11_Authenticate.restype = ctypes.c_int
    nss.PK11SDR_Decrypt.argtypes = [
        ctypes.POINTER(SECItem), ctypes.POINTER(SECItem), ctypes.c_void_p
    ]
    nss.PK11SDR_Decrypt.restype = ctypes.c_int

    if nss.NSS_Init(f"sql:{tmp}".encode()) != 0:
        sys.exit("NSS_Init a echoue : profil illisible.")

    slot = nss.PK11_GetInternalKeySlot()
    if nss.PK11_Authenticate(slot, 1, None) != 0:
        pwd = getpass("Mot de passe principal Firefox : ")
        nss.PK11_SetPasswordFunc  # noop, on retente via l'API simple
        if nss.PK11_CheckUserPassword(slot, pwd.encode()) != 0:
            sys.exit("Mot de passe principal incorrect.")

    def decrypt(b64):
        raw = base64.b64decode(b64)
        buf = ctypes.create_string_buffer(raw, len(raw))
        inp = SECItem(0, ctypes.cast(buf, ctypes.c_void_p), len(raw))
        out = SECItem(0, None, 0)
        if nss.PK11SDR_Decrypt(ctypes.byref(inp), ctypes.byref(out), None) != 0:
            return "(dechiffrement impossible)"
        return ctypes.string_at(out.data, out.len).decode("utf-8", "replace")

    resultats = []
    for entry in logins:
        host = entry.get("hostname", "")
        if list_only:
            if echo:
                print(host)
            resultats.append((host, "", ""))
            continue
        if motif not in host.lower():
            continue
        user = decrypt(entry["encryptedUsername"])
        pwd = decrypt(entry["encryptedPassword"])
        resultats.append((host, user, pwd))
        if echo:
            print()
            print("SITE        :", host)
            print("IDENTIFIANT :", user)
            print("MOT DE PASSE:", pwd)

    if echo:
        print()
        print(f"{len(resultats)} site(s) enregistre(s)." if list_only
              else f"{len(resultats)} entree(s) pour le motif '{motif}'.")
    shutil.rmtree(tmp, ignore_errors=True)
    return resultats


if __name__ == "__main__":
    main()
