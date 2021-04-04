import random
import unittest
from unittest.mock import patch, mock_open

from gilfoyle import score, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestScore(unittest.TestCase):
    def test_display(self):
        with patch('builtins.open', mock_open(read_data='{"riri": 5, "fifi": 0, "loulou": -3}')):
            self.assertEqual(
                'Riri : 5 pt(s)\nFifi : 0 pt(s)\nLoulou : -3 pt(s)',
                score.display()
            )

    @patch('gilfoyle.score.update')
    def test_update_before_displaying(self, update):
        with patch('builtins.open', mock_open(read_data='{}')) as file:
            with open(file):
                score.display()

        update.assert_called_once_with({})

    @patch('json.dump')
    def test_update(self, json):
        with patch('builtins.open', mock_open()):
            with open('./score.json', 'w') as f:
                score.update({'Toto': 2})

        json.assert_called_once_with({'Riri': 0, 'Fifi': 0, 'Loulou': 0}, f)

    def test_check_passes(self):
        self.assertTrue(score.check(
            Message(constants.GILFOYLE_ALIAS + ' ' + random.choice(constants.SCORE_WORDS), 'moi')
        ))

    def test_check_fails(self):
        self.assertFalse(score.check(
            Message(constants.GILFOYLE_ALIAS, 'moi')
        ))
        self.assertFalse(score.check(
            Message(random.choice(constants.SCORE_WORDS), 'moi')
        ))
