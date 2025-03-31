import random

print("Welcome to Blackjack Game")
to_play = True
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 0]

while to_play:
    def blackjack():
        dealer_hand = []
        first_random_card_for_dealer = random.choice(cards)
        second_random_card_for_dealer = random.choice(cards)
        dealer_hand.append(first_random_card_for_dealer)
        dealer_hand.append(second_random_card_for_dealer)

        def ace_handler_dealer(total, hand):
            for i, card in enumerate(hand):
                if card == 0:
                    if total + 11 <= 21:
                        hand[i] = 11
                        total += 11
                    else:
                        hand[i] = 1
                        total += 1
            return total

        ace_handler_dealer(sum(dealer_hand),dealer_hand)

        while sum(dealer_hand) < 17:
            add_card_to_dealer = random.choice(cards)
            dealer_hand.append(add_card_to_dealer)
            ace_handler_dealer(sum(dealer_hand),dealer_hand)

        player_hand = []
        first_random_card_for_player = random.choice(cards)
        second_random_card_for_player = random.choice(cards)
        player_hand.append(first_random_card_for_player)
        player_hand.append(second_random_card_for_player)

        def ace_handler_player(total, hand):
            for i, card in enumerate(hand):
                if card == 0:
                    if total + 11 <= 21:
                        hand[i] = 11
                        total += 11
                    else:
                        hand[i] = 1
                        total += 1
            return total

        ace_handler_player(sum(player_hand),player_hand)

        print(f"Player's hand: {player_hand}")

        add_card = input("Do you want to add a card? (y/n): ").lower()
        if add_card == "y":
            wants_to_add = True
        else:
            wants_to_add = False

        while wants_to_add:
            add_card_to_player = random.choice(cards)
            player_hand.append(add_card_to_player)
            ace_handler_player(sum(player_hand),player_hand)
            print(f"Player's hand: {player_hand}")
            still_add_card = input("Do you want to add another card? (y/n): ").lower()
            if still_add_card == "n":
                wants_to_add = False

        if sum(dealer_hand) > 21:
            print(f"Dealer's hand: {dealer_hand}")
            print("Player wins the game!")
            return
        if sum(player_hand) > 21:
            print(f"Dealer's hand: {dealer_hand}")
            print("Dealer wins the game!")
            return
        if sum(player_hand) > sum(dealer_hand):
            print(f"Dealer's hand: {dealer_hand}")
            print("Player wins the game!")
            return
        if sum(dealer_hand) > sum(player_hand):
            print(f"Dealer's hand: {dealer_hand}")
            print("Dealer wins the game!")
            return
        if sum(dealer_hand) == sum(player_hand):
            print(f"Dealer's hand: {dealer_hand}")
            print("It's a Draw!")
            return

    blackjack()
    play = input("Do you want to play again? (y/n): ").lower()
    if play == "n":
        to_play = False
