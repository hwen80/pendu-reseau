# coding: utf-8
import os
import pickle
from random import choice

from donnees import *

def get_scores():
    if os.path.exists(scores_file_name):
        scores_file = open(scores_file_name, "rb")
        depickler = pickle.Unpickler(scores_file)
        scores = depickler.load()
        scores_file.close()
    else:
        scores = {}
    return scores

def get_words():
    if os.path.exists(words_file_name):
        words_file = open(words_file_name, "rb")
        depickler = pickle.Unpickler(words_file)
        words = depickler.load()
        words_file.close()
    else:
        words = [ "erreur" ]
    return words

def set_scores(scores):
    scores_file = open(scores_file_name, "wb")
    pickler = pickle.Pickler(scores_file)
    pickler.dump(scores)
    scores_file.close()

def get_user():
    user = raw_input("Tapez votre nom: ")
    user = user.capitalize()
    if not user.isalnum() or len(user)<4:
        print("Ce nom est invalide.")
        return get_user()
    else:
        return user

def get_char():
    char = raw_input("Tapez une lettre: ")
    char = char.lower()
    if len(char)>1 or not char.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return get_char()
    else:
        return char

def get_masked_word(word, found_letters):
    masked_word = ""
    for char in word:
        if char in found_letters:
            masked_word += char
        else:
            masked_word += "*"
    return masked_word
