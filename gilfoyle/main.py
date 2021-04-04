from gilfoyle import quote, random_values, game, scapegoat


def on_message(message):
    if scapegoat.check(message):
        return scapegoat.pick()
    elif random_values.check(message):
        return random_values.global_result()
    elif game.check(message):
        return game.play(message)
    else:
        return quote.response(message)
