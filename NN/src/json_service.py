import json
from src.Deck import Deck


def read_json_deck(filename):
    f = open(filename, "r")

    param_dict = json.load(f)
    deck = Deck.from_dict(param_dict)

    return deck
