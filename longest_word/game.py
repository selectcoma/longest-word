import random
import string

class Game:
    def __init__(self):
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        grid_copy = list(self.grid)
        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False
        return True
