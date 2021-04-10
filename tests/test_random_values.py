import random
import unittest
from unittest.mock import patch

from gilfoyle import random_values, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestRandomValues(unittest.TestCase):
    @patch('random.randint')
    def test_random_number(self, choice):
        choice.return_value = 6

        self.assertEqual(6, random_values.number())

    @patch('random.choice')
    def test_random_letter(self, choice):
        choice.return_value = 'Q'

        self.assertEqual('Q', random_values.letter())

    @patch('random.choice')
    def test_random_bool(self, choice):
        choice.return_value = 'False'

        self.assertEqual('False', random_values.boolean())

    @patch('random.choice')
    def test_random_answer(self, choice):
        choice.return_value = 'No'

        self.assertEqual('No', random_values.answer())

    @patch('random.choice')
    def test_random_heads_or_tails(self, choice):
        choice.return_value = 'Tails'

        self.assertEqual('Tails', random_values.heads_or_tails())

    @patch('random.choice')
    def test_random_direction(self, choice):
        choice.return_value = 'Left'

        self.assertEqual('Left', random_values.direction())

    @patch('random.choice')
    def test_random_chifumi(self, choice):
        choice.return_value = 'Scissors'

        self.assertEqual('Scissors', random_values.chifumi())

    @patch('gilfoyle.random_values.chifumi')
    @patch('gilfoyle.random_values.direction')
    @patch('gilfoyle.random_values.heads_or_tails')
    @patch('gilfoyle.random_values.answer')
    @patch('gilfoyle.random_values.boolean')
    @patch('gilfoyle.random_values.letter')
    @patch('gilfoyle.random_values.number')
    def test_random_values(self, number, letter, boolean, answer, heads_or_tails, direction, chifumi):
        number.return_value = 6
        letter.return_value = 'Q'
        boolean.return_value = 'False'
        answer.return_value = 'No'
        heads_or_tails.return_value = 'Tails'
        direction.return_value = 'Left'
        chifumi.return_value = 'Scissors'

        self.assertEqual(
            'Number : 6\n'
            + 'Letter : Q\n'
            + 'True/False : False\n'
            + 'Yes/No : No\n'
            + 'Heads/Tails : Tails\n'
            + 'Direction : Left\n'
            + 'Chifumi : Scissors',
            random_values.global_result()
        )

    def test_check_passes(self):
        self.assertTrue(random_values.check(
            Message(constants.GILFOYLE_ALIAS + ' ' + random.choice(constants.RANDOM_WORDS), 'Me')
        ))

    def test_check_fails(self):
        self.assertFalse(random_values.check(
            Message(constants.GILFOYLE_ALIAS, 'Me')
        ))
        self.assertFalse(random_values.check(
            Message(random.choice(constants.RANDOM_WORDS), 'Me')
        ))
