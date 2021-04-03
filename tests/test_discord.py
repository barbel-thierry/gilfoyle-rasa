import unittest
from gilfoyle import discord


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestDiscord(unittest.TestCase):
    def test_quote(self):
        self.assertEqual(
            'Leeloo Dallas, multipass. Muultiipaass. - Milla Jovovich, Le cinquième élément (Luc Besson)',
            discord.on_message(
                Message('Il faut que je retrouve mon pass', 'moi')
            )
        )

    def test_no_quote(self):
        self.assertIsNone(
            discord.on_message(
                Message("j'ai envie de manger un morceau", 'moi')
            )
        )
