class Deck(object):
    def __init__(self, cards, rating):
        self.cards = cards
        self.rating = rating

    @classmethod
    def from_dict(cls, param_dict):
        cards = param_dict["cards"]
        rating = param_dict["rating"]

        return cls(cards, rating)
