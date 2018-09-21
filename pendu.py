#!/usr/bin/env python
# coding: utf-8
from donnees import *
from functions import *

scores = get_scores()
words = get_words()
socket = create_socket()

c, addr = socket.accept()
user = get_user(c)

if user not in scores.keys():
    scores[user] = 0

continue_game = 'o'

while continue_game != 'n':
    print 'Connection reçue depuis', addr
    message = "Joueur {0}: {1} point(s)".format(user, scores[user])
    print message
    data = pickle.loads(message)
    msg_send(c, data)
    word = choice(words)
    found_letters = []
    found_word = get_masked_word(word, found_letters)
    now_chances = chances
    while word != found_word and now_chances > 0:
        data = pickle.loads("Mot à trouver {0} (encore {1} chance(s))".format(found_word, now_chances))
        msg_send(c, data)
        char = get_char(c)
        if char in found_letters:
            data = pickle.loads("Vous avez déjà choisi cette lettre.")
            msg_send(c, data)
        elif char in word:
            found_letters.append(char)
            data = pickle.loads("Bien joué.")
            msg_send(c, data)
        else:
            now_chances -= 1
            data = pickle.loads("Raté, cette lettre ne se trouve pas dans le mot.")
            msg_send(c, data)
        found_word = get_masked_word(word, found_letters)

    if word == found_word:
        data = pickle.loads("Félicitations ! Vous avez trouvé le mot {0}.".format(word))
        msg_send(c, data)
    else:
        data = pickle.loads("PERDU")
        msg_send(c, data)
        print("PERDU")

    scores[user] += now_chances

    continue_game = get_input()

set_scores(scores)

data = pickle.loads("Vous finissez la partie avec {0} points.".format(scores[user]))
msg_send(c, data)
