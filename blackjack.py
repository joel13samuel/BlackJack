# imports the random number generator
from p1_random import P1Random

rng = P1Random()

# game num tracks number of games played
game_num = 0
# continues the game loop
game_continue = True
# number of player wins
player_wins = 0
# number of dealer wins
dealer_wins = 0
# number of ties
tie_wins = 0


# the loop for the game
while game_continue:
    game_num += 1
    print(f"START GAME #{game_num}")
    print()
    player_hand = 0
    # generates the random card
    card = rng.next_int(13) + 1
    # adds the cards value to the players hand
    if card == 1:
        print(f"Your card is a ACE!")
        player_hand += card
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
        player_hand += card
    elif card == 11:
        print("Your card is a JACK!")
        player_hand += 10
    elif card == 12:
        print("Your card is a QUEEN!")
        player_hand += 10
    else:
        print("Your card is a KING!")
        player_hand += 10

    print(f"Your hand is: {player_hand}")
    print()

    # loops the menu that allows the player chooses what the want to happen next
    no_winner = True
    while no_winner:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()
        option = int(input("Choose an option: "))
        print()

        # if statements for the option that the player chooses
        if option == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print(f"Your card is a ACE!")
                player_hand += card
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
                player_hand += card
            elif card == 11:
                print("Your card is a JACK!")
                player_hand += 10
            elif card == 12:
                print("Your card is a QUEEN!")
                player_hand += 10
            else:
                print("Your card is a KING!")
                player_hand += 10
        # checks if player wins by hitting 21 or loses by going over it
            if player_hand == 21:
                print(f"Your hand is: {player_hand}")
                print()
                print("BLACKJACK! You win!")
                print()
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print(f"Your hand is: {player_hand}")
                print()
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                no_winner = False
            else:
                print(f"Your hand is: {player_hand}")
                print()
        # checks if the dealer wins by getting more than the player, or if the dealer loses
        elif option == 2:
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()

            if dealer_hand > 21:
                print("You win!")
                player_wins += 1
                no_winner = False
            elif dealer_hand > player_hand:
                print("Dealer wins!")
                dealer_wins += 1
                no_winner = False
            elif dealer_hand < player_hand:
                print("You win!")
                player_wins += 1
                no_winner = False
            # if they have the same score then it's a tie
            else:
                print("It's a tie! No one wins!")
                tie_wins += 1
                no_winner = False

            print()
        # prints the stats of the game
        elif option == 3:
            game_num -= 1
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_wins}")
            print(f"Total #  of games played is: {game_num}")
            print(f"Percentage of Player wins: {player_wins/game_num * 100}% ")
        # exits the program
        elif option == 4:
            game_continue = False
            no_winner = False
        # if invalid input allows the user to enter a proper number
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            print()
            continue











