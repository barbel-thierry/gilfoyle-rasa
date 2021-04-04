import os

from dotenv import load_dotenv

load_dotenv()

# Discord Id
GILFOYLE_ID = os.getenv('GILFOYLE_ID', '')
GILFOYLE_ALIAS = "<@" + GILFOYLE_ID + ">"

# Trigerring words to get random values
RANDOM_WORDS = ['hasard', 'aléatoire', 'random']

# Trigerring words and potential scapegoats
SCAPEGOAT_WORDS = ['maudit', 'réprouvé', 'souffre-douleur', 'victime']
SCAPEGOAT_TARGETS = os.getenv('SCAPEGOAT_TARGETS', '').split(', ')

# Triggers for the game
GAME_TRIGGER = os.getenv('GAME_TRIGGER')
GAME_RESPONSE = os.getenv('GAME_RESPONSE')
GAME_WINNING_ANSWER = os.getenv('GAME_WINNING_ANSWER')
