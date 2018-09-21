# coding: utf-8
import os
import pickle
from random import choice

from donnees import *

def recup_scores():
    if os.path.exists(nom_fichier_scores):
        fichier_scores = open(nom_fichier_scores, "rb")
        depickler = pickle.Unpickler(fichier_scores)
        scores = depickler.load()
        fichier_scores.close()
    else:
        scores = {}
    return scores

def recup_mots():
    if os.path.exists(nom_fichier_mots):
        fichier_mots = open(nom_fichier_mots, "rb")
        depickler = pickle.Unpickler(fichier_mots)
        liste_mots = depickler.load()
        fichier_mots.close()
    else:
        liste_mots = [ "erreur" ]
    return liste_mots

def enregistrer_scores(scores):
    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

def recup_nom_utilisateur():
    nom_utilisateur = raw_input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    lettre = raw_input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recup_lettre()
    else:
        return lettre

def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque
