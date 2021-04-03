import unittest
from unittest.mock import patch

from gilfoyle import random_values, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestRandomValues(unittest.TestCase):
    @patch('random.randint')
    def test_random_number(self, random):
        random.return_value = 6

        self.assertEqual(6, random_values.number())

    @patch('random.choice')
    def test_random_letter(self, random):
        random.return_value = 'Q'

        self.assertEqual('Q', random_values.letter())

    @patch('random.choice')
    def test_random_bool(self, random):
        random.return_value = 'Faux'

        self.assertEqual('Faux', random_values.boolean())

    @patch('random.choice')
    def test_random_answer(self, random):
        random.return_value = 'Non'

        self.assertEqual('Non', random_values.answer())

    @patch('random.choice')
    def test_random_heads_or_tails(self, random):
        random.return_value = 'Face'

        self.assertEqual('Face', random_values.heads_or_tails())

    @patch('random.choice')
    def test_random_direction(self, random):
        random.return_value = 'Gauche'

        self.assertEqual('Gauche', random_values.direction())

    @patch('random.choice')
    def test_random_chifoumi(self, random):
        random.return_value = 'Ciseaux'

        self.assertEqual('Ciseaux', random_values.chifoumi())

    @patch('gilfoyle.random_values.chifoumi')
    @patch('gilfoyle.random_values.direction')
    @patch('gilfoyle.random_values.heads_or_tails')
    @patch('gilfoyle.random_values.answer')
    @patch('gilfoyle.random_values.boolean')
    @patch('gilfoyle.random_values.letter')
    @patch('gilfoyle.random_values.number')
    def test_random_values(self, number, letter, boolean, answer, heads_or_tails, direction, chifoumi):
        number.return_value = 6
        letter.return_value = 'Q'
        boolean.return_value = 'Faux'
        answer.return_value = 'Non'
        heads_or_tails.return_value = 'Face'
        direction.return_value = 'Gauche'
        chifoumi.return_value = 'Ciseaux'

        self.assertEqual(
            'Chiffre : 6\n'
            + 'Lettre : Q\n'
            + 'Vrai/Faux : Faux\n'
            + 'Oui/Non : Non\n'
            + 'Pile/Face : Face\n'
            + 'Direction : Gauche\n'
            + 'Chifoumi : Ciseaux',
            random_values.global_result()
        )

    def test_check_passes(self):
        self.assertTrue(random_values.check(
            Message(constants.GILFOYLE_ALIAS + ' hasard', 'moi')
        ))

    def test_check_fails(self):
        self.assertFalse(random_values.check(
            Message(constants.GILFOYLE_ALIAS, 'moi')
        ))
        self.assertFalse(random_values.check(
            Message('hasard', 'moi')
        ))
