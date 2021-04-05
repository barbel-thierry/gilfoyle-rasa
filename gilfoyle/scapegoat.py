import random

from gilfoyle import constants


def pick():
    return random.choice(constants.SCAPEGOAT_TARGETS)


def check(message):
    gilfoyle = constants.GILFOYLE_ID in message.content
    word = any(keyword in str(message.content).lower() for keyword in constants.SCAPEGOAT_WORDS)

    return gilfoyle and word
