import random
import unittest

from gilfoyle import scapegoat, constants


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author


class TestScapegoat(unittest.TestCase):
    def test_random_scapegoat(self):
        self.assertIn(scapegoat.pick(), constants.SCAPEGOAT_TARGETS)

    def test_check_passes(self):
        self.assertTrue(scapegoat.check(
            Message(constants.GILFOYLE_ALIAS + ' ' + random.choice(constants.SCAPEGOAT_WORDS), 'Me')
        ))

    def test_check_fails(self):
        self.assertFalse(scapegoat.check(
            Message(constants.GILFOYLE_ALIAS, 'Me')
        ))
        self.assertFalse(scapegoat.check(
            Message(random.choice(constants.SCAPEGOAT_WORDS), 'Me')
        ))
