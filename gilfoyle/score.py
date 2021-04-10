import json
import os
import sys

from gilfoyle import constants


def display():
    overhaul()

    with open(os.path.join(sys.path[0], 'score.json')) as file:
        values = json.load(file)

    return '\n'.join(
        [str(name).capitalize() + ': ' + str(score) + ' pt(s)' for name, score in values.items()]
    )


def increment(player):
    overhaul()

    with open(os.path.join(sys.path[0], 'score.json')) as file:
        values = json.load(file)
        values[player] = values[player] + 1

    with open(os.path.join(sys.path[0], 'score.json'), 'w') as outfile:
        json.dump(values, outfile)

    return values[player]


def overhaul():
    with open(os.path.join(sys.path[0], 'score.json')) as file:
        entries = json.load(file)

    for player in constants.SCAPEGOAT_TARGETS:
        if player not in entries:
            entries[str(player).capitalize()] = 0

    for key in [key for key in entries if key not in constants.SCAPEGOAT_TARGETS]:
        del entries[key]

    with open(os.path.join(sys.path[0], 'score.json'), 'w') as outfile:
        json.dump(entries, outfile)


def check(message):
    gilfoyle = constants.GILFOYLE_ID in message.content
    word = any(keyword in str(message.content).lower() for keyword in constants.SCORE_WORDS)

    return gilfoyle and word
