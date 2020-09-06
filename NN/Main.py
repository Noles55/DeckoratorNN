import tensorflow as tf
import random


def build_and_train_model(size):
    model = build_model()
    input = get_training_input(size)
    model.fit(input[0], input[1], epochs=10)
    print(model.predict([create_model_input([24, 1, 6, 67, 99, 84, 53, 17, 63, 95]),
                         create_model_input([4, 78, 5, 10, 11, 43, 64, 12, 82, 96]),
                         create_model_input([24, 67, 11, 83, 53, 99, 16, 61, 7, 48])]))


def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(100, activation='relu', input_shape=(100,)),
        tf.keras.layers.Dense(1)
    ])

    model.compile(loss='mse', optimizer=tf.keras.optimizers.RMSprop(.001), metrics=['mae', 'mse'])

    return model


def get_training_input(size):
    decks = generate_decks(size, list(range(99)))
    return format_input_for_training(decks)


def format_input_for_training(decks):
    card_set = list()
    rating_set = list()
    for deck in decks:
        card_set.append(create_model_input(deck.cards))
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
        rating = max(rating - get_training_rate_offset(training_deck, cold), 1)
        training_set.append(RatedDeck(training_deck, rating))

    return training_set


def create_model_input(deck):
    cards = [0] * 100
    for num in deck:
        cards[num] = 1

    return cards


def get_training_rate_offset(training_deck, pairs):
    offset = 0
    for pair in pairs:
        if pair[0] in training_deck and pair[1] in training_deck:
            offset = offset + 2

    return offset


class RatedDeck:
    def __init__(self, cards, rating):
        self.cards = cards
        self.rating = rating
