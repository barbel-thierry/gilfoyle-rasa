import os

from gilfoyle import constants, score


def launch(message):
    if constants.GAME_TRIGGER.lower() in str(message.content).lower() and os.environ.get('GAME') is None:
        os.environ['GAME'] = 'on'

        return constants.GAME_RESPONSE


def match(message):
    if message.content == constants.GAME_WINNING_ANSWER and os.environ.get('GAME') == 'on':
        new_value = score.increment(message.author)
        del os.environ['GAME']

        return 'Bravo, ' + str(message.author) + ', tu as désormais ' + str(new_value) + ' pt(s) !'


def play(message):
    return match(message) or launch(message)


def check(message):
    triggered = constants.GAME_TRIGGER.lower() in str(message.content).lower()
    won = constants.GAME_WINNING_ANSWER.lower() in str(message.content).lower()
    is_a_player = message.author in constants.SCAPEGOAT_TARGETS

    return triggered or (won and is_a_player)
