import unittest
from unittest.mock import patch

from gilfoyle import main


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestMain(unittest.TestCase):
    @patch('gilfoyle.scapegoat.pick')
    @patch('gilfoyle.scapegoat.check')
    def test_scapegoat(self, check, pick):
        check.return_value = True

        main.on_message(Message('', ''))

        pick.assert_called_once_with()

    @patch('gilfoyle.random_values.global_result')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_random_values(self, scapegoat, check, random):
        scapegoat.return_value= False
        check.return_value = True

        main.on_message(Message('', ''))

        random.assert_called_once_with()

    @patch('gilfoyle.game.play')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_game(self, scapegoat, random, check, game):
        scapegoat.return_value= False
        random.return_value = False
        check.return_value = True
        message = Message('', '')

        main.on_message(message)

        game.assert_called_once_with(message)

    @patch('gilfoyle.quote.response')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_quote(self, scapegoat, random, game, quote):
        scapegoat.return_value= False
        random.return_value = False
        game.return_value = False
        message = Message('', '')

        main.on_message(message)

        quote.assert_called_once_with(message)
