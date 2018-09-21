#!/usr/bin/env python
# coding: utf-8
from donnees import *
from functions import *

scores = get_scores()
words = get_words()
socket = create_socket()

c, addr = socket.accept()
print "Connection depuis", addr
user = get_user(c)

if user not in scores.keys():
    scores[user] = 0

continue_game = 'o'

while continue_game != 'n':
    message = "Joueur {0}: {1} point(s)".format(user, scores[user])
    data = pickle.dumps([message, ""])
    msg_send(c, data)
    word = choice(words)
    found_letters = []
    found_word = get_masked_word(word, found_letters)
    now_chances = chances
    while word != found_word and now_chances > 0:
        message = "Mot à trouver {0} (encore {1} chance(s))".format(found_word, now_chances)
        data = pickle.dumps([message, ""])
        msg_send(c, data)
        char = get_char(c)
        if char in found_letters:
            message = "Vous avez déjà choisi cette lettre."
            data = pickle.dumps([message, ""])
            msg_send(c, data)
        elif char in word:
            found_letters.append(char)
            message = "Bien joué."
            data = pickle.dumps([message, ""])
            msg_send(c, data)
        else:
            now_chances -= 1
            message = "Raté, cette lettre ne se trouve pas dans le mot."
            data = pickle.dumps([message, ""])
            msg_send(c, data)
        found_word = get_masked_word(word, found_letters)

    if word == found_word:
        message = "Félicitations ! Vous avez trouvé le mot {0}.".format(word)
        data = pickle.dumps([message, ""])
        msg_send(c, data)
    else:
        message = "PERDU"
        data = pickle.dumps([message, ""])
        msg_send(c, data)

    scores[user] += now_chances

    continue_game = get_input(c)

set_scores(scores)
message = "Vous finissez la partie avec {0} point(s).".format(scores[user])
data = pickle.dumps([message, "exit"])
msg_send(c, data)
c.close()
print("Fin de partie.")
socket.close()
