import json
import random

from Deck import Deck


def create_model_input(deck):
    cards = [0] * 100
    for num in deck.cards:
        cards[num] = 1

    return cards


def format_input_for_training(decks):
    card_set = list()
    rating_set = list()
    for deck in decks:
        card_set.append(create_model_input(deck))
        rating_set.append(deck.rating)

    return [card_set, rating_set]


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


def write_decks_to_file(decks):
    f = open("../Generated-small-training-decks.json", 'w')
    json_list = [deck.to_dict() for deck in decks]
    json.dump(json_list, f)
