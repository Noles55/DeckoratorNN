class Deck(object):
    def __init__(self, cards, rating=5):
        self.cards = cards
        self.rating = rating

    def to_dict(self):

        return dict(cards=self.cards, rating=self.rating)

    @classmethod
    def from_dict(cls, param_dict):
        cards = param_dict["cards"]
        rating = param_dict["rating"]

        return cls(cards, rating)


