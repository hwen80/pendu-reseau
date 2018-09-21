#!/usr/bin/env python
# coding: utf-8
import os
import pickle
from random import choice

def get_words():
    if os.path.exists("mots"):
        words_file = open("mots", "rb")
        depickler = pickle.Unpickler(words_file)
        words = depickler.load()
        words_file.close()
    else:
        words = [ "erreur" ]
    return words

def set_words(words):
    words_file = open("mots", "wb")
    pickler = pickle.Pickler(words_file)
    pickler.dump(words)
    words_file.close()

def get_input():
    print("Entrez le mot à ajouter, stop pour arrêter")
    word = raw_input()
    if not word.isalpha():
        print("Ce mot est invalide.")
        return get_input()
    else:
        return word

word=""
words=get_words()
while word != "stop":
    word=get_input()
    if word in words:
        print("Ce mot est déjà présent.")
    if word != "stop" and word not in words:
        words.append(word.lower())
print("Enregistrement des mots")
set_words(words)
