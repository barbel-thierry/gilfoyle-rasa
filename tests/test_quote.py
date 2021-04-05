import unittest
from unittest.mock import patch

from gilfoyle import quote


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestQuote(unittest.TestCase):
    @patch('requests.post')
    def test_quote(self, request):
        request.return_value.json.return_value = [{
            'text': 'Leeloo Dallas, multipass. Muultiipaass. - Milla Jovovich, Le cinquième élément (Luc Besson)'
        }]

        self.assertEqual(
            '```yaml\nLeeloo Dallas, multipass. Muultiipaass. - Milla Jovovich, Le cinquième élément (Luc Besson)\n```',
            quote.response(
                Message('Il faut que je retrouve mon pass', 'moi')
            )
        )

    @patch('requests.post')
    def test_no_quote(self, request):
        request.return_value.json.return_value = []

        self.assertIsNone(
            quote.response(
                Message("j'ai envie de manger un morceau", 'moi')
            )
        )
