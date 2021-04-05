import os
import unittest
from unittest.mock import patch, mock_open

from gilfoyle import game, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestGame(unittest.TestCase):
    def test_initial_response(self):
        launch_response = 'Toi. Toi.'

        self.assertEqual(
            launch_response,
            game.launch(
                Message('Tu y vas, toi ?', 'moi')
            )
        )

        del os.environ['GAME']
        self.assertEqual(
            launch_response,
            game.play(
                Message('Tu y vas, toi ?', 'moi')
            )
        )

    def test_winning_answer(self):
        with patch('builtins.open', mock_open(read_data='{"riri": 5, "fifi": 0, "loulou": -3}')):
            match_response = 'Bravo, fifi, tu as désormais 1 pt(s) !'

            os.environ['GAME'] = 'on'
            self.assertEqual(
                match_response,
                game.match(
                    Message('Mon toit.', 'fifi')
                )
            )

            os.environ['GAME'] = 'on'
            self.assertEqual(
                match_response,
                game.play(
                    Message('Mon toit.', 'fifi')
                )
            )

    def test_losing_answer(self):
        self.assertIsNone(game.match(
            Message('Autre chose', 'moi')
        ))

    def test_check_passes(self):
        self.assertTrue(game.check(
            Message(constants.GAME_TRIGGER, 'moi')
        ))
        self.assertTrue(game.check(
            Message(constants.GAME_WINNING_ANSWER, 'moi')
        ))

    def test_check_fails(self):
        self.assertFalse(game.check(
            Message('test', 'moi')
        ))
