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
    
class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

class Chip():
    type = 'dollar'
    amount = 1
    def give_player_chip():
        global player_chip
        global player_bat

        dealer_chip = 100
        player_chip = {}
        player_bat = {}
        for player in player_names:
            player_chip[player] = 10
            player_bat[player] = 0
        return player_chip, player_bat

    def get_player_names():
        global player_names
        num_players = int(input("How many players? (1~7): "))
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

def BJ_Game():
    players = {}
    dealer = {}
    print("Welcome to the world's simplest game!")
    player_names = Chip.get_player_names()

    for name in player_names:
        players[name] = []

    deal_initial_cards(players, dealer)
    Chip.give_player_chip()

    for player, hand in players.items():
        player_bat[player] = input(f"{player}, How much will you bat($)? : ")
    for player, hand in players.items():
        hand_value = calculate_hand_value(hand)
        print(f"{player}: {' '.join([str(card) for card in hand])}\t({hand_value})\t total $ = {player_chip[player]}, bat($) = {player_bat[player]}")

    dealer_hand = dealer[0]

    print(f"dealer: {' '.join(['XX' if not card.is_face_up else str(card) for card in dealer_hand])}")


    #구현 전
    for player,hand in players.items():
        Y = input(f"{player}, do you want a hit? (Y/N): ")
    # for player in players.items():

if __name__ == "__main__":
    BJ_Game()
