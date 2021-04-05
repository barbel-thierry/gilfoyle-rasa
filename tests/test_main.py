import asyncio
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

        asyncio.run(main.on_message(Message('', '')))

        pick.assert_called_once_with()

    @patch('gilfoyle.random_values.global_result')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_random_values(self, scapegoat, check, random):
        scapegoat.return_value = False
        check.return_value = True

        asyncio.run(main.on_message(Message('', '')))

        random.assert_called_once_with()

    @patch('gilfoyle.game.play')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_game(self, scapegoat, random, check, game):
        scapegoat.return_value = False
        random.return_value = False
        check.return_value = True
        message = Message('', '')

        asyncio.run(main.on_message(message))

        game.assert_called_once_with(message)

    @patch('gilfoyle.score.display')
    @patch('gilfoyle.score.check')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_score(self, scapegoat, random, game, check, score):
        scapegoat.return_value = False
        random.return_value = False
        game.return_value = False
        check.return_value = True

        asyncio.run(main.on_message(Message('', '')))

        score.assert_called_once_with()

    @patch('gilfoyle.quote.response')
    @patch('gilfoyle.score.check')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_quote(self, scapegoat, random, game, score, quote):
        scapegoat.return_value = False
        random.return_value = False
        game.return_value = False
        score.return_value = False
        message = Message('', '')

        asyncio.run(main.on_message(message))

        quote.assert_called_once_with(message)
