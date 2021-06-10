from code import Cards, Rounds, RoundWinError, GameWinError, authentication, highscore, get_top_five
import time

p1_current = []
p2_current = []
p1_deck = []
p2_deck = []

authentication()

time.sleep(1)

cards_ = ["Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9", "Red 10", "Yellow 1",
          "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7", "Yellow 8", "Yellow 9", "Yellow 10",
          "Black 1", "Black 2", "Black 3", "Black 4", "Black 5", "Black 6", "Black 7", "Black 8", "Black 9", "Black 10"]

cd = Cards(cards_, p1_current, p2_current, p1_deck, p2_deck)

cd.card_shuffle(cards_)

print(f"\nLeaderboard:\n{get_top_five()}")

try:
    for i in range(15):
        input(f"\n\nRound {i + 1}:\nPress enter when you want to continue...")
        cd.card_gen(cards_, p1_current, p2_current)
        print(f"Player 1's card is {p1_current}\nPlayer 2's card is {p2_current}\n")

        Rounds.round_win(cards_, p1_current, p2_current, p1_deck, p2_deck)
        print(
            f"\nPlayer 1:\nPoints: {len(p1_deck)}\nCards: {p1_deck}\n\nPLayer 2:\nPoints: {len(p2_deck)}\nCards: {p2_deck}")

    if len(p1_deck) > len(p2_deck):
        print(f"\n\nPlayer 1 wins!\n\nPlayer 1: {len(p1_deck)} points.\nPlayer 2: {len(p2_deck)} points.")
        x = len(p1_deck)
        highscore(x)
    elif len(p2_deck) > len(p1_deck):
        print(f"\n\nPlayer 2 wins!\n\nPlayer 1: {len(p1_deck)} points.\nPlayer 2: {len(p2_deck)} points.")
        x = len(p2_deck)
        highscore(x)
    else:
        raise GameWinError("The game failed to dedicate a game winner") from None
except RoundWinError:
    raise RoundWinError("The round failed to dedicate a round winner") from None
