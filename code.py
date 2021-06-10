import json
import random


# Custom errors
class RoundWinError(Exception):
    pass


class GameWinError(Exception):
    pass


def get_top_five():
    data2 = []
    with open("highscore.json") as f:
        data = json.load(f)
        for i in range(1, 6):
            data2.append(data[len(data) - i])
    return data2[0], data2[1], data2[2], data2[3], data2[4]


def highscore(score):
    with open("highscore.json") as f:
        data = json.load(f)
    inp = input("\nWhat name would you like to be put on the leaderboard? ")
    data.append([inp, score])
    x = 0
    for i in range(len(data) - 1):
        if x == len(data):
            break
        for a in range(len(data) - 1 - i):
            if data[a][1] > data[a + 1][1]:
                data[a], data[a + 1] = data[a + 1], data[a]
    with open("highscore.json", "w+") as f:
        json.dump(data, f)
    print(f"\nLeaderboard:\n{get_top_five()}")


def authentication():
    end = 0
    with open(f"users.json") as f:
        data = json.load(f)
    while True:
        username = input("What is your username?\n\nInput:\t")
        password = input("\nWhat is your password?\n\nInput:\t")
        for i in range(len(data)):
            if username in data[i]:
                if password in data[i]:
                    print("\nACCESS GRANTED")
                    end = 1
                    break
        if end == 1:
            break
        print("\nIncorrect username or password, please try again\n")


class Cards:

    def __init__(self, cards, p1_current, p2_current, p1_deck, p2_deck):
        self.cards = cards
        self.p1_current = p1_current
        self.p2_current = p2_current
        self.p1_deck = p1_deck
        self.p2_deck = p2_deck

    def card_shuffle(self, cards):
        random.shuffle(self.cards)
        return self.cards

    def card_gen(self, cards, p1_current, p2_current):
        self.p1_current.append(self.cards[0])
        self.cards.remove(self.cards[0])
        self.p2_current.append(self.cards[0])
        self.cards.remove(self.cards[0])
        return self.p1_current, self.p2_current


class Rounds(Cards):

    def __init__(self, cards, p1_current, p2_current, p1_deck, p2_deck):
        super().__init__(cards, p1_current, p2_current, p1_deck, p2_deck)

    @staticmethod
    def round_win(self, p1_current, p2_current, p1_deck, p2_deck):
        if ("Yellow" in p1_current[0] and "Yellow" in p2_current[0]) or (
                "Red" in p1_current[0] and "Red" in p2_current[0]) or (
                "Black" in p1_current[0] and "Black" in p2_current[0]):
            x = p1_current[0].split()
            y = p2_current[0].split()
            if int(x[1]) > int(y[1]):
                p1_deck.append(p1_current[0])
                p1_deck.append(p2_current[0])
                p1_current.remove(p1_current[0])
                p2_current.remove(p2_current[0])
            elif int(x[1]) < int(y[1]):
                p2_deck.append(p1_current[0])
                p2_deck.append(p2_current[0])
                p1_current.remove(p1_current[0])
                p2_current.remove(p2_current[0])
        elif ("Yellow" in p1_current[0] and "Red" in p2_current[0]) or (
                "Red" in p1_current[0] and "Black" in p2_current[0]) or (
                "Black" in p1_current[0] and "Yellow" in p2_current[0]):
            p1_deck.append(p1_current[0])
            p1_deck.append(p2_current[0])
            p1_current.remove(p1_current[0])
            p2_current.remove(p2_current[0])
        elif ("Yellow" in p2_current[0] and "Red" in p1_current[0]) or (
                "Red" in p2_current[0] and "Black" in p1_current[0]) or (
                "Black" in p2_current[0] and "Yellow" in p1_current[0]):
            p2_deck.append(p1_current[0])
            p2_deck.append(p2_current[0])
            p1_current.remove(p1_current[0])
            p2_current.remove(p2_current[0])
        else:
            raise RoundWinError
        return p1_current, p2_current, p1_deck, p2_deck
