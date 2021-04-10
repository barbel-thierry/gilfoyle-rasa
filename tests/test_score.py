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
        with patch('builtins.open', mock_open(read_data='{"You": 5, "Me": 0, "She": -3}')):
            self.assertEqual(
                'You: 5 pt(s)\nMe: 0 pt(s)\nShe: -3 pt(s)',
                score.display()
            )

    @patch('gilfoyle.score.overhaul')
    def test_update_before_displaying(self, overhaul):
        with patch('builtins.open', mock_open(read_data='{}')) as file:
            with open(file):
                score.display()

        overhaul.assert_called_once_with()

    @patch('json.dump')
    def test_overhaul(self, json):
        with patch('builtins.open', mock_open(read_data='{}')):
            with open('./score.json', 'w') as f:
                score.overhaul()

        json.assert_called_once_with({'You': 0, 'Me': 0, 'She': 0}, f)

    def test_check_passes(self):
        self.assertTrue(score.check(
            Message(constants.GILFOYLE_ALIAS + ' ' + random.choice(constants.SCORE_WORDS), 'Me')
        ))

    def test_check_fails(self):
        self.assertFalse(score.check(
            Message(constants.GILFOYLE_ALIAS, 'Me')
        ))
        self.assertFalse(score.check(
            Message(random.choice(constants.SCORE_WORDS), 'Me')
        ))
