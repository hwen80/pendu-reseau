Jeu du pendu en Python
======================

HOW TO
------

Le jeu du pendu peut être utilisé avec `./pendu.py` ou `python pendu.py`

Le jeu va vous demander votre nom d'utilisateur, et enregistrer les scores dans un fichier score (si le fichier n'est pas présent ou est vide, les scores sont nuls).

La liste des mots est stockée dans un fichier mots. Si ce fichier n'existe pas ou est vide, seul le mot "pendu" existe.

Pour initialiser la liste des mots, un script `init_mots.py` est donné. Il peut être exécuté en mode interactif (ajout des mots un par un, entrer le mot stop pour arrêter le script) ou directement en argument de la ligne de commande.

Exemple : `./init_mots.py ceci est un exemple` ajoutera les mots ceci, est, un et exemple dans la liste des mots utilisée par pendu.py.
