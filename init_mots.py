#!/usr/bin/env python
# coding: utf-8
import os
import pickle
from random import choice

def recup_mots():
    if os.path.exists("mots"):
        fichier_mots = open("mots", "rb")
        depickler = pickle.Unpickler(fichier_mots)
        mots = depickler.load()
        fichier_mots.close()
    else:
        mots = [ "erreur" ]
    return mots

def enregistrer_mots(mots):
    fichier_mots = open("mots", "wb")
    pickler = pickle.Pickler(fichier_mots)
    pickler.dump(mots)
    fichier_mots.close()

def recup_saisie():
    print("Entrer mot à ajouter, stop pour arrêter")
    mot = raw_input()
    if not mot.isalpha():
        print("Ce mot est invalide.")
        return recup_saisie()
    else:
        return mot

mot=""
mots=recup_mots()
while mot != "stop":
    mot=recup_saisie()
    if mot != "stop":
        mots.append(mot.lower())
print("Enregistrement des mots")
enregistrer_mots(mots)
