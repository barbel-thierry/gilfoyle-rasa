from gilfoyle import scapegoat, random_values, game, score, quote


def on_message(message):
    if scapegoat.check(message):
        return scapegoat.pick()
    elif random_values.check(message):
        return random_values.global_result()
    elif game.check(message):
        return game.play(message)
    elif score.check(message):
        return score.display()
    else:
        return quote.response(message)
