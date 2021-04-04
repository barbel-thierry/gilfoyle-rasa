import unittest

from gilfoyle import game, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestGame(unittest.TestCase):
    def test_initial_response(self):
        self.assertEqual(
            'Toi. Toi.',
            game.launch(
                Message('Tu y vas, toi ?', 'moi')
            )
        )

    def test_winning_answer(self):
        self.assertEqual(
            'Bravo, moi, tu as donné la bonne réponse !',
            game.match(
                Message('Mon toit.', 'moi')
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
