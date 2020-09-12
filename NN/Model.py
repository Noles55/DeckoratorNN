import tensorflow as tf
from ModelUtils import *


class DeckoratorModel(object):
    def __init__(self, num_input_nodes):
        self.model = build_model(num_input_nodes)
        self.num_input_nodes = num_input_nodes

    def train(self, decks, epochs=10):
        training_input = format_input_for_training(decks)
        self.model.fit(training_input[0], training_input[1], epochs)

    def predict(self, deck):
        return self.model.predict([create_model_input(deck)])


def build_model(num_input_nodes):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(num_input_nodes, activation='relu', input_shape=(num_input_nodes,)),
        tf.keras.layers.Dense(num_input_nodes, activation="relu"),
        tf.keras.layers.Dense(1)
    ])

    model.compile(loss='mse', optimizer=tf.keras.optimizers.RMSprop(.001), metrics=['mae', 'mse'])

    return model
