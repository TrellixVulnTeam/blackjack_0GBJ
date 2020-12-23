from random import randint


globals()["face card"] = []
drawn_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"]

print("\nPLAYER'S TURN\n")


def card_count(dealer=False, show=True):
    ace_count = 0
    temp_cards = []
    for card in globals()["face card"]:
        if card == "a":
            ace_count += 1
        else:
            temp_cards.append(card)
    temp_cards += ["a"] * ace_count
    current_value = 0
    for card in globals()["face card"]:
        if type(card) == str:
            if card in ["j", "q", "k"]:
                card = 10
            else:
                card = 11
                if current_value + card > 21:
                    card = 1
        current_value += card
    if show:
        print("Card(s) showing: " + " ".join([str(elem) for elem in globals()["face card"]]))
        print("value is: " + str(current_value))
    still_playing(current_value, dealer)
    return current_value


def draw_card():
    position = randint(0, 12)
    new_card = drawn_card[position]
    globals()["face card"].append(new_card)
    print("new card: " + str(new_card))


def still_playing(total, dealer):
    if total >= 22:
        if dealer:
            print("i mean, i guess you win ")
        else:
            print("you're really bad at this")
        exit()


def blackjack(dealer=False):
    if card_count(show=False) == 21:
        if dealer:
            print("get wrekt scrub ")
        else:
            print("BLACKJACK! Congrats ")
        exit()


first = drawn_card[randint(0, 12)]
globals()["dealers first card"] = first
print("Dealer is showing: " + str(first))
draw_card()
draw_card()
blackjack()
current_player_value = card_count()


def dealer_plays(player_value):
    print("\nDEALER PLAYS\n")
    globals()["face card"] = [globals()["dealers first card"]]
    draw_card()
    blackjack(dealer=True)
    dealer_value = card_count(dealer=True)
    while dealer_value <= 16:
        draw_card()
        dealer_value = card_count(dealer=True)
    if player_value > dealer_value:
        print("you win, i mean, i guess ")
    elif player_value == dealer_value:
        print("Push " + str(player_value))
    else:
        print("The House Wins, You suck ")
    exit()


while True:
    answer = input("\t\t hit? (y/n) ")
    if answer == "y":
        draw_card()
        current_player_value = card_count()
    elif answer == "n":
        dealer_plays(current_player_value)
    else:
        print("invalid input, try again")
