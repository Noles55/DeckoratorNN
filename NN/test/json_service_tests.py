import unittest
from json_service import *


class JsonServiceTests(unittest.TestCase):
    def test_read_deck_file(self):
        deck = read_json_deck_from_file("../TestDecks/Deck-Neutral.json")
        self.assertEqual([1, 94, 17, 44, 65, 52, 42, 76, 23, 20], deck.cards)
        self.assertEqual(5, deck.rating)

    def test_read_deck_string(self):
        deck_string = '{"cards":[1, 94, 17, 44, 65, 52, 42, 76, 23, 20],"rating":5}'
        deck = read_json_deck_from_string(deck_string)
        self.assertEqual([1, 94, 17, 44, 65, 52, 42, 76, 23, 20], deck.cards)
        self.assertEqual(5, deck.rating)

    def test_write_deck_to_json(self):
        deck = Deck([1, 94, 17, 44, 65, 52, 42, 76, 23, 20], 5)
        write_deck_to_json_file(deck, "../TestDecks/Write-Test-Deck.json")
        f = open("../TestDecks/Write-Test-Deck.json", 'r')
        self.assertEqual('{"cards":[1,94,17,44,65,52,42,76,23,20],"rating":5}', ''.join(f.read().split()))

if __name__ == '__main__':
    unittest.main()
