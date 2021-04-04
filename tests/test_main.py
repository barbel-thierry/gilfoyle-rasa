import unittest
from unittest.mock import patch

from gilfoyle import main


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestMain(unittest.TestCase):
    @patch('gilfoyle.random_values.global_result')
    @patch('gilfoyle.random_values.check')
    def test_random_values(self, check, random):
        check.return_value = True

        main.on_message(Message('', ''))

        random.assert_called_once_with()

    @patch('gilfoyle.quote.response')
    @patch('gilfoyle.random_values.check')
    def test_quote(self, random, quote):
        random.return_value = False
        message = Message('', '')

        main.on_message(message)

        quote.assert_called_once_with(message)
