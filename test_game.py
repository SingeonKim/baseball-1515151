from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_exception_when_input_is_none(self):
        self.game = Game()
        with self.assertRaises(TypeError):
            self.game.guess(None)