from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        game = Game()
        assert isinstance(game.grid, list), 'the grid should be a list'
        assert len(game.grid) == 9, 'the length of the grid should be equal to 9'
        for letter in game.grid:
            assert letter in string.ascii_uppercase

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
