import json
from Deck import Deck


def read_json_deck():
    f = open("dummydeck.json", "r")

    param_dict = json.load(f)
    deck = Deck.from_dict(param_dict)

    return deck
