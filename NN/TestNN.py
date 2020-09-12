import os
import random
from src.Deck import Deck
from src import json_service
from src.Model import DeckoratorModel


def build_and_train_model(num_input_nodes, num_training_decks):
    model = DeckoratorModel(num_input_nodes)
    decks = generate_decks(num_training_decks, list(range(100)))
    model.train(decks)
    return model


def rate_test_decks(model):
    for filename in os.listdir("TestDecks"):
        read_and_rate_json_deck("TestDecks\\" + filename, model)


def read_and_rate_json_deck(filename, model):
    deck = json_service.read_json_deck(filename)
    rating = model.predict(deck)
    deck.rating = rating
    print(str(deck.rating) + " " + filename)


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
