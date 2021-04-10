import os


def pytest_configure(config):
    os.environ['DISCORD_TOKEN'] = 'discord_token'
    os.environ['GILFOYLE_ID'] = 'gilfoyle'

    os.environ['SCAPEGOAT_WORDS'] = 'fall guy, victim, goat'
    os.environ['SCAPEGOAT_TARGETS'] = 'You, Me, She'

    os.environ['RANDOM_WORDS'] = 'random, luck'

    os.environ['GAME_TRIGGER'] = 'up'
    os.environ['GAME_RESPONSE'] = "we're up all night"
    os.environ['GAME_WINNING_ANSWER'] = "we're up all night to get lucky"

    os.environ['SCORE_WORDS'] = 'score, results'

    return config
