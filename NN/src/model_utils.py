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
