# Boite a outils navigateur

Piloter un site web a ma place quand le remplir au lecteur d'ecran est trop
penible : je me connecte une fois a la main, l'assistant fait le reste en
headless.

## Le principe

Un assistant en ligne de commande ne voit pas un navigateur en direct, et il
ne doit jamais taper mon mot de passe. D'ou la coupure en deux :

1. Je lance `capture_session.py`, un navigateur visible s'ouvre, je me
   connecte a la main. Le script enregistre uniquement les cookies.
2. L'assistant recharge ces cookies en headless et travaille seul :
   il explore la page, lit sa structure, appelle l'API du site.

Le mot de passe n'est jamais lu ni ecrit par les scripts.

## Installation

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium

Derriere un proxy qui reecrit le TLS (Zscaler par exemple), exporter d'abord
NODE_EXTRA_CA_CERTS vers le certificat racine, sinon le telechargement de
Chromium echoue.

## Usage

Etape 1, moi :

    python capture_session.py https://exemple.fr/login

Etape 2, l'assistant :

    python explore.py https://exemple.fr/ma-page
    python fetch_api.py https://exemple.fr/api/export sortie.json

Les sessions et les releves atterrissent dans ~/secrets, hors de ce depot.

## Les fichiers

- capture_session.py : etape 1, capture de session, seul script interactif.
- explore.py : releve champs, boutons et liens d'une ou plusieurs pages.
- fetch_api.py : appelle une URL avec la session et enregistre la reponse.
- a11y_dump.py : le JS partage qui recupere le libelle accessible reel
  (aria-label, label for, label parent, aria-labelledby).
- session.py : ou vivent les sessions, et comment les fichiers sont nommes.
- firefox_mdp.py : lit un mot de passe du trousseau Firefox en local, pour
  ne jamais l'ecrire dans un fichier ni le passer en ligne de commande.

## Ce qui fait rater

- Adresser les champs par leur libelle accessible (get_by_label,
  get_by_role, get_by_placeholder), jamais par des classes CSS generees :
  elles changent a chaque regeneration de page.
- Une session expire. Une redirection vers la page de login, ou du HTML de
  login rendu avec un statut 200, veut dire : refaire l'etape 1.
- Le bandeau cookies masque des elements. Le cliquer avant de relever.
- Si le site expose un export et un import du meme format, faire l'aller
  retour sur ce format plutot que de remplir les champs un par un.
- Un fichier de session vaut une connexion : il ne sort jamais de ~/secrets.
