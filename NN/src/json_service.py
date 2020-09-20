import json
from Deck import Deck


def read_json_deck_from_file(filename):
    f = open(filename, "r")

    param_dict = json.load(f)
    deck = Deck.from_dict(param_dict)

    return deck


def read_json_deck_from_string(string):
    param_dict = json.loads(string)
    deck = Deck.from_dict(param_dict)

    return deck


def write_deck_to_json_file(deck, destination):
    f = open(destination, 'w')
    json.dump(deck.to_dict(), f)
