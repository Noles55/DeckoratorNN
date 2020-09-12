import random
import unittest

from src.Deck import Deck
from src.Model import DeckoratorModel


class ModelTests(unittest.TestCase):
    def test_cold3_less_than_cold2(self):
        cold3 = Deck([4, 94, 19, 64, 65, 52, 43, 78, 37, 20])
        cold2 = Deck([4, 94, 17, 64, 65, 52, 43, 78, 23, 20])

        self.assertLess(self.model.predict(cold3), self.model.predict(cold2))

    def test_cold2_less_than_cold1(self):
        cold2 = Deck([4, 94, 17, 64, 65, 52, 43, 78, 23, 20])
        cold1 = Deck([4, 94, 17, 44, 65, 52, 42, 78, 23, 20])

        self.assertLess(self.model.predict(cold2), self.model.predict(cold1))

    def test_cold1_less_than_neutral(self):
        cold1 = Deck([4, 94, 17, 44, 65, 52, 42, 78, 23, 20])
        neutral = Deck([1, 94, 17, 44, 65, 52, 42, 76, 23, 20])

        self.assertLess(self.model.predict(cold1), self.model.predict(neutral))

    def test_neutral_less_than_hot1(self):
        neutral = Deck([1, 94, 17, 44, 65, 52, 42, 76, 23, 20])
        hot1 = Deck([1, 94, 16, 43, 65, 67, 42, 62, 24, 20])
        self.assertLess(self.model.predict(neutral), self.model.predict(hot1))

    def test_hot1_less_than_hot2(self):
        hot1 = Deck([1, 94, 16, 43, 65, 67, 42, 62, 24, 20])
        hot2 = Deck([53, 99, 16, 43, 65, 67, 42, 62, 24, 20])

        self.assertLess(self.model.predict(hot1), self.model.predict(hot2))

    def test_hot2_less_than_hot3(self):
        hot2 = Deck([53, 99, 16, 43, 65, 67, 42, 62, 24, 20])
        hot3 = Deck([53, 99, 16, 43, 61, 67, 42, 62, 24, 20])

        self.assertLess(self.model.predict(hot2), self.model.predict(hot3))

    @classmethod
    def setUpClass(cls):
        super(ModelTests, cls).setUpClass()
        cls.model = DeckoratorModel(100)
        cls.model.train(generate_decks(10000, list(range(100))))


if __name__ == '__main__':
    unittest.main()


def generate_decks(num_decks, sample_range):
    hot = [[24, 67], [11, 83], [53, 99], [16, 61]]
    cold = [[4, 78], [19, 37], [43, 64], [7, 48]]

    training_set = list()

    for x in range(num_decks):
        rating = 5
        training_deck = random.sample(sample_range, 10)
        rating = min(rating + get_training_rate_offset(training_deck, hot), 10)
        rating = max(rating - get_training_rate_offset(training_deck, cold), 0)
        training_set.append(Deck(training_deck, rating))

    return training_set


def get_training_rate_offset(training_deck, pairs):
    offset = 0
    for pair in pairs:
        if pair[0] in training_deck and pair[1] in training_deck:
            offset = offset + 2

    return offset
