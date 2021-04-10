import random
import string

from gilfoyle import constants


def number():
    return random.randint(0, 100)


def letter():
    return random.choice(string.ascii_uppercase)


def boolean():
    return random.choice(['True', 'False'])


def answer():
    return random.choice(['Yes', 'No'])


def heads_or_tails():
    return random.choice(['Heads', 'Tails'])


def direction():
    return random.choice(['Right', 'Left'])


def chifumi():
    return random.choice(['Rock', 'Paper', 'Scissors'])


def global_result():
    return (
            'Number : ' + str(number()) + '\n'
            + 'Letter : ' + str(letter()) + '\n'
            + 'True/False : ' + str(boolean()) + '\n'
            + 'Yes/No : ' + str(answer()) + '\n'
            + 'Heads/Tails : ' + str(heads_or_tails()) + '\n'
            + 'Direction : ' + str(direction()) + '\n'
            + 'Chifumi : ' + str(chifumi())
    )


def check(message):
    gilfoyle = constants.GILFOYLE_ID in message.content
    word = any(keyword in str(message.content).lower() for keyword in constants.RANDOM_WORDS)

    return gilfoyle and word
