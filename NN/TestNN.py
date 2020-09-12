import random
from Deck import Deck
import JSONService
from ModelUtils import *
from Model import DeckoratorModel


def build_and_train_model(num_input_nodes, num_training_decks):
    model = DeckoratorModel(num_input_nodes)
    model.train(generate_decks(num_training_decks, list(range(99))))

    # print(model.predict([create_model_input([24, 1, 6, 67, 99, 84, 53, 17, 63, 95]),
    #                      create_model_input([4, 78, 5, 10, 11, 43, 64, 12, 82, 96]),
    #                      create_model_input([24, 67, 11, 83, 53, 99, 16, 61, 7, 48]),
    #                      create_model_input([25, 13, 6, 14, 55, 84, 98, 65, 21, 1])]))

    deck = JSONService.read_json_deck()
    print(deck.rating)
    rating = model.predict(deck)
    deck.rating = rating
    print(deck.rating)


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
