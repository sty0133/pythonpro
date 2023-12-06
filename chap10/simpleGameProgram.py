import random

class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply

class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

def get_player_names():
    num_players = int(input("How many players? (2~5): "))
    player_names = []
    for i in range(num_players):
        name = input("Enter player name: ")
        player_names.append(name)
    return player_names

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card.rank == "A":
            value += 11
            num_aces += 1
        elif card.rank in ["K", "Q", "J"]:
            value += 10
        else:
            value += int(card.rank)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def deal_initial_cards(players, dealer):
    for player in players:
        player_hand = [Positionable_Card(random.choice(Card.RANKS), random.choice(Card.SUITS)) for _ in range(2)]
        players[player] = player_hand

    dealer_hand = [Positionable_Card(random.choice(Card.RANKS), random.choice(Card.SUITS)) for _ in range(2)]
    dealer_hand[0].is_face_up = False
    dealer[0] = dealer_hand

def main():
    players = {}
    dealer = {}
    print("Welcome to the world's simplest game!")
    player_names = get_player_names()

    for name in player_names:
        players[name] = []

    deal_initial_cards(players, dealer)

    for player, hand in players.items():
        hand_value = calculate_hand_value(hand)
        print(f"{player}: {' '.join([str(card) for card in hand])}\t<{hand_value}>")

    dealer_hand = dealer[0]

    print(f"dealer: {' '.join(['XX' if not card.is_face_up else str(card) for card in dealer_hand])}")

if __name__ == "__main__":
    main()
