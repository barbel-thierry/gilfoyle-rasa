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
        self.assertEqual(
            os.environ.get('GAME_RESPONSE'),
            game.launch(
                Message('Are you up?', 'Me')
            )
        )

        del os.environ['GAME']
        self.assertEqual(
            os.environ.get('GAME_RESPONSE'),
            game.play(
                Message('Are you up?', 'Me')
            )
        )

    def test_winning_answer(self):
        with patch('builtins.open', mock_open(read_data='{"You": 5, "Me": 0, "She": -3}')):
            match_response = 'Well done, She, your score is now -2!'

            os.environ['GAME'] = 'on'
            self.assertEqual(
                match_response,
                game.match(
                    Message(os.environ.get('GAME_WINNING_ANSWER'), 'She')
                )
            )

            os.environ['GAME'] = 'on'
            self.assertEqual(
                match_response,
                game.play(
                    Message(os.environ.get('GAME_WINNING_ANSWER'), 'She')
                )
            )

    def test_losing_answer(self):
        self.assertIsNone(game.match(
            Message('Some other line', 'Me')
        ))

    def test_check_passes(self):
        self.assertTrue(game.check(
            Message(constants.GAME_TRIGGER, 'Me')
        ))
        self.assertTrue(game.check(
            Message(constants.GAME_WINNING_ANSWER, 'Me')
        ))

    def test_check_fails(self):
        self.assertFalse(game.check(
            Message('Test', 'Me')
        ))
