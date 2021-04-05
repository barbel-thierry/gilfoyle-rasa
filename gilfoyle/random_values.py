import random
import string

from gilfoyle import constants


def number():
    return random.randint(0, 100)


def letter():
    return random.choice(string.ascii_uppercase)


def boolean():
    return random.choice(['Vrai', 'Faux'])


def answer():
    return random.choice(['Oui', 'Non'])


def heads_or_tails():
    return random.choice(['Pile', 'Face'])


def direction():
    return random.choice(['Droite', 'Gauche'])


def chifoumi():
    return random.choice(['Pierre', 'Feuille', 'Ciseaux'])


def global_result():
    return (
            'Chiffre : ' + str(number()) + '\n'
            + 'Lettre : ' + str(letter()) + '\n'
            + 'Vrai/Faux : ' + str(boolean()) + '\n'
            + 'Oui/Non : ' + str(answer()) + '\n'
            + 'Pile/Face : ' + str(heads_or_tails()) + '\n'
            + 'Direction : ' + str(direction()) + '\n'
            + 'Chifoumi : ' + str(chifoumi())
    )


def check(message):
    gilfoyle = constants.GILFOYLE_ID in message.content
    word = any(keyword in str(message.content).lower() for keyword in constants.RANDOM_WORDS)

    return gilfoyle and word
