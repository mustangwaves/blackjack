import random

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(hand):
    score = 0
    for card in hand:
        if card in 'JQK':
            score += 10
        elif card == 'A':
            score += 11 if score + 11 <= 21 else 1
        else:
            score += int(card)
    return score

print("Welcome to Blackjack!")

balance = input("How much would you like to start with? $")
balance = int(balance)

print("You have $" + str(balance) + ". Good luck!")

while True:
    bet = input("How much would you like to bet? $")
    bet = int(bet)
    if bet > balance:
        print("Sorry, you don't have enough balance.")
        continue

    player_hand = []
    split_hands = []
    dealer_hand = []

    # Deal initial cards
    player_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))
    player_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))

    # Check if player has two cards of the same rank
    if player_hand[0] == player_hand[1]:
        choice = input("Do you want to split your hand? (y/n) ")
        if choice.lower() == 'y':
            split_hands.append([player_hand.pop(1)])
            split_hands[0].append(draw_card(deck))
            player_hand.append(draw_card(deck))
            split_bet = input("How much would you like to bet for the split hand? $")
            split_bet = int(split_bet)
            if split_bet > balance:
                print("Sorry, you don't have enough balance for the split bet.")
                continue

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\nYour cards:", ' '.join(player_hand))
    print("Your score:", player_score)
    print("Dealer's card:", dealer_hand[0])

    # Check if player or dealer has exactly 21
    if player_score == 21 and dealer_score != 21:
        print("Congratulations! You have Blackjack!")
        balance += bet * 2.5
        print("You win 2.5 times your bet. Your new balance:", balance)
    elif dealer_score == 21 and player_score != 21:
        print("Dealer has Blackjack! You lose.")
        balance -= bet
        print("Your new balance:", balance)
    elif player_score == 21 and dealer_score == 21:
        print("Both you and the dealer have Blackjack. It's a tie.")
    elif player_score == 21:
        print("You have 21! Let's see the result.")
        if dealer_score == 21:
            print("Dealer also has 21. It's a tie.")
        else:
            print("You win!")
            balance += bet
        print("Your new balance:", balance)
        continue

    # Player's turn
    while True:
        choice = input("Do you want to draw another card? (y/n) ")
        if choice.lower() == 'y':
            player_hand.append(draw_card(deck))
            player_score = calculate_score(player_hand)
            print("\nYour cards:", ' '.join(player_hand))
            print("Your score:", player_score)
            if player_score > 21:
                print("Bust! You lose.")
                balance -= bet
                break
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if player_score <= 21:
        # Dealer's turn
        while dealer_score < 17:
            dealer_hand.append(draw_card(deck))
            dealer_score = calculate_score(dealer_hand)

        print("\nDealer's cards:", ' '.join(dealer_hand))
        print("Dealer's score:", dealer_score)

        if dealer_score > 21:
            print("Dealer busts! You win.")
            balance += bet
        elif dealer_score > player_score:
            print("Dealer wins.")
            balance -= bet
        elif dealer_score < player_score:
            print("You win.")
            balance += bet
        else:
            print("It's a tie.")

    # Handle split hand
    for split_hand in split_hands:
        split_score = calculate_score(split_hand)
        print("\nSplit hand:", ' '.join(split_hand))
        print("Split hand score:", split_score)

        # Player's turn for split hand
        while True:
            choice = input("Do you want to draw another card for the split hand? (y/n) ")
            if choice.lower() == 'y':
                split_hand.append(draw_card(deck))
                split_score = calculate_score(split_hand)
                print("\nSplit hand:", ' '.join(split_hand))
                print("Split hand score:", split_score)
                if split_score > 21:
                    print("Bust! You lose for the split hand.")
                    balance -= split_bet
                    break
            elif choice.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if split_score <= 21:
            # Dealer's turn for split hand
            while dealer_score < 17:
                dealer_hand.append(draw_card(deck))
                dealer_score = calculate_score(dealer_hand)

            print("\nDealer's cards:", ' '.join(dealer_hand))
            print("Dealer's score:", dealer_score)

            if dealer_score > 21:
                print("Dealer busts! You win for the split hand.")
                balance += split_bet
            elif dealer_score > split_score:
                print("Dealer wins for the split hand.")
                balance -= split_bet
            elif dealer_score < split_score:
                print("You win for the split hand.")
                balance += split_bet
            else:
                print("It's a tie for the split hand.")

    print("\nYour balance:", balance)

    if balance <= 0:
        print("Game over. You ran out of balance.")
        break

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        break

    if balance == bet:
        print("\nGoing all in! Good luck!")
    elif balance < bet:
        print("\nYou're going all in with your remaining balance! Good luck!")

print("\nThank you for playing!")