import json
import os
import sys

from gilfoyle import constants


def display():
    with open(os.path.join(sys.path[0], 'score.json')) as file:
        values = json.load(file)

        if len(values.items()) != len(constants.SCAPEGOAT_TARGETS):
            update(values)

        return '\n'.join(
            [str(name).capitalize() + ' : ' + str(score) + ' pt(s)' for name, score in values.items()]
        )


def update(entries):
    for player in constants.SCAPEGOAT_TARGETS:
        if player not in entries:
            entries[player] = 0

    for key in [key for key in entries if key not in constants.SCAPEGOAT_TARGETS]:
        del entries[key]

    with open(os.path.join(sys.path[0], 'score.json'), 'w') as outfile:
        json.dump(entries, outfile)


def check(message):
    gilfoyle = constants.GILFOYLE_ID in message.content
    word = any(keyword in str(message.content).lower() for keyword in constants.SCORE_WORDS)

    return gilfoyle and word
