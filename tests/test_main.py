import asyncio
import unittest
from unittest.mock import patch

from gilfoyle import main


class TestMain(unittest.TestCase):
    @unittest.skip("TypeError: object MagicMock can't be used in 'await' expression")
    @patch('discord.Message')
    @patch('gilfoyle.scapegoat.pick')
    @patch('gilfoyle.scapegoat.check')
    def test_scapegoat(self, check, pick, message):
        check.return_value = True

        asyncio.run(main.on_message(message))

        pick.assert_called_once_with()

    @unittest.skip("TypeError: object MagicMock can't be used in 'await' expression")
    @patch('discord.Message')
    @patch('gilfoyle.random_values.global_result')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_random_values(self, scapegoat, check, random, message):
        scapegoat.return_value = False
        check.return_value = True

        asyncio.run(main.on_message(message))

        random.assert_called_once_with()

    @unittest.skip("TypeError: object MagicMock can't be used in 'await' expression")
    @patch('discord.Message')
    @patch('gilfoyle.game.play')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_game(self, scapegoat, random, check, game, message):
        scapegoat.return_value = False
        random.return_value = False
        check.return_value = True

        asyncio.run(main.on_message(message))

        game.assert_called_once_with(message)

    @unittest.skip("TypeError: object MagicMock can't be used in 'await' expression")
    @patch('discord.Message')
    @patch('gilfoyle.score.display')
    @patch('gilfoyle.score.check')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_score(self, scapegoat, random, game, check, score, message):
        scapegoat.return_value = False
        random.return_value = False
        game.return_value = False
        check.return_value = True

        asyncio.run(main.on_message(message))

        score.assert_called_once_with()

    @unittest.skip("TypeError: object MagicMock can't be used in 'await' expression")
    @patch('discord.Message')
    @patch('gilfoyle.quote.response')
    @patch('gilfoyle.score.check')
    @patch('gilfoyle.game.check')
    @patch('gilfoyle.random_values.check')
    @patch('gilfoyle.scapegoat.check')
    def test_quote(self, scapegoat, random, game, score, quote, message):
        scapegoat.return_value = False
        random.return_value = False
        game.return_value = False
        score.return_value = False

        asyncio.run(main.on_message(message))

        quote.assert_called_once_with(message)
