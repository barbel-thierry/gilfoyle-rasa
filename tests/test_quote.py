import unittest
from gilfoyle import quote


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestQuote(unittest.TestCase):
    def test_quote(self):
        self.assertEqual(
            'Leeloo Dallas, multipass. Muultiipaass. - Milla Jovovich, Le cinquième élément (Luc Besson)',
            quote.response(
                Message('Il faut que je retrouve mon pass', 'moi')
            )
        )

    def test_no_quote(self):
        self.assertIsNone(
            quote.response(
                Message("j'ai envie de manger un morceau", 'moi')
            )
        )
