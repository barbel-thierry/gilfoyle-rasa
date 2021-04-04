from gilfoyle import constants


def launch(message):
    if constants.GAME_TRIGGER.lower() in str(message.content).lower():
        return constants.GAME_RESPONSE


def match(message):
    if message.content == constants.GAME_WINNING_ANSWER:
        return 'Bravo, ' + str(message.author) + ', tu as donné la bonne réponse !'


def check(message):
    triggered = constants.GAME_TRIGGER.lower() in str(message.content).lower()
    won = constants.GAME_WINNING_ANSWER.lower() in str(message.content).lower()

    return triggered or won


def play(message):
    return match(message) or launch(message)
