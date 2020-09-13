import os
import unittest
from src.json_service import *


class JsonServiceTests(unittest.TestCase):
    def test_read_deck_file(self):
        deck = read_json_deck("../TestDecks/Deck-Neutral.json")
        self.assertEqual([1, 94, 17, 44, 65, 52, 42, 76, 23, 20], deck.cards)
        self.assertEqual(5, deck.rating)


if __name__ == '__main__':
    unittest.main()
