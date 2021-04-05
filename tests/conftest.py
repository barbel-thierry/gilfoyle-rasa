import os


def pytest_configure(config):
    os.environ['DISCORD_TOKEN'] = 'discord_token'
    os.environ['GILFOYLE_ID'] = 'gilfoyle'

    os.environ['SCAPEGOAT_WORDS'] = 'maudit, réprouvé, victime'
    os.environ['SCAPEGOAT_TARGETS'] = 'Riri, Fifi, Loulou'

    os.environ['RANDOM_WORDS'] = 'hasard, aléatoire, random'

    os.environ['GAME_TRIGGER'] = 'toi'
    os.environ['GAME_RESPONSE'] = 'Toi. Toi.'
    os.environ['GAME_WINNING_ANSWER'] = 'Mon toit.'

    os.environ['SCORE_WORDS'] = 'score, résultats'

    return config
