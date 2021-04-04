import os


def pytest_configure(config):
    os.environ['GILFOYLE_ID'] = 'gilfoyle'

    os.environ['GAME_TRIGGER'] = 'toi'
    os.environ['GAME_RESPONSE'] = 'Toi. Toi.'
    os.environ['GAME_WINNING_ANSWER'] = 'Mon toit.'

    os.environ['SCAPEGOAT_TARGETS'] = 'Riri, Fifi, Loulou'

    return config
