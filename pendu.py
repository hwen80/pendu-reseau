#!/usr/bin/env python
# coding: utf-8
from donnees import *
from functions import *

scores = get_scores()
user = get_user()
words = get_words()

if user not in scores.keys():
    scores[user] = 0

continue_game = 'o'

while continue_game != 'n':
    print("Joueur {0}: {1} point(s)".format(user, scores[user]))
    word = choice(words)
    found_letters = []
    found_word = get_masked_word(word, found_letters)
    now_chances = chances
    while word != found_word and now_chances > 0:
        print("Mot à trouver {0} (encore {1} chances)".format(found_word, now_chances))
        char = get_char()
        if char in found_letters:
            print("Vous avez déjà choisi cette lettre.")
        elif char in word:
            found_letters.append(char)
            print("Bien joué.")
        else:
            now_chances -= 1
            print("Raté, cette lettre ne se trouve pas dans le mot.")
        found_word = get_masked_word(word, found_letters)

    if word == found_word:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(word))
    else:
        print("PERDU")

    scores[user] += now_chances

    continue_game = get_input()

set_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[user]))
