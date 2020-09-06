import json
from Deck import Deck


def read_json_deck():
    f = open("dummydeck.json", "r")

    peram_dict = json.load(f)
    deck = Deck.from_dict(peram_dict)

    return deck
