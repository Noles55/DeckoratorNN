class Deck(object):
    def __init__(self, cards, rating):
        self.cards = cards
        self.rating = rating

    @classmethod
    def from_dict(cls, peram_dict):
        cards = peram_dict["cards"]
        rating = peram_dict["rating"]

        return cls(cards,rating)