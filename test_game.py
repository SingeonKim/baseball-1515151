from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self) -> None:
        self.game = Game()
        super().setUp()

    def test_exception_when_input_is_none(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass
