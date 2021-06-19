import random
from typing import List
from art import logo

#Card Values
cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
        #Ace's are 11


#Functions used in program
def generate_deck(num=2):
    """This function generates the number of cards to be given in a deck. 
    Can be modified incase a user want's to increase the amount of cards in a deck.

    Args:
        num (int, optional): Number of cards to be handed out. Defaults to 2.
    """
    test_list = []
    for i in range(num):
        test_list.append(random.choice(cards))
    return test_list

def blackjack(deck: List[int]):
    """Detects if a deck has reached blackjack (21)

    Args:
        deck (List[int]): A list containing a users deck.

    Returns:
        True: If a user has blackjack.
    """
    if sum(deck) == 21:
        return True
    else:
        return False

def final_hands(deck1, deck2):
    print(f"\tYour final hand: {deck1}, final score: {sum(deck1)}")
    print(f"\tComputer's final hand: {deck2}, final score: {sum(deck2)}")

#Variable Values
keep_playing = False
inquire = input("Would you like to play blackjack? 'y' or 'n' ")
if inquire == 'y':
    keep_playing = True

#Loop while playing
while keep_playing == True:
    print(logo)
    ##This section here generates the players cards
    player_deck = generate_deck()
    ai_deck = generate_deck()

    #Determines if any of the starting deck reached blackjack.
    if blackjack(player_deck) == True and blackjack(ai_deck) == False:
        print("You have reached blackjack. You won!!")
        play_again = input("Would you like to play again? 'y' or 'n' ").lower()
        if play_again == 'n':
            keep_playing = False
    if blackjack(ai_deck) == True and blackjack(player_deck) == False:
        print("The computer has reached blackjack. You lost.")
        play_again = input("Would you like to play again? 'y' or 'n' ").lower()
        if play_again == 'n':
            keep_playing = False

    #Starts out by printing the starting decks.
    print(f"\tYour cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"\tComputer's first card: {ai_deck[0]}")
    keep_drawing = True
    lost_game = False
    if sum(player_deck) > 21:
        keep_drawing = False
        lost_game = True
    
    #Incorporates whether if to keep drawing or not.
    while keep_drawing:
        draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_a_card == 'n':
            keep_drawing = False
        else:
            generate1 = generate_deck(1)
            for i in generate1:
                player_deck.append(i)
            if sum(player_deck) > 21:
                keep_drawing = False
                lost_game = True
            if blackjack(player_deck) == True:
                final_hands(player_deck, ai_deck)
                print("You reached blackjack, meaning you won!!")
                play_again = input("Would you like to play again? 'y' or 'n' ").lower()
                if play_again == 'n':
                    keep_playing = False
            print(f"\tYour cards: {player_deck}, current score: {sum(player_deck)}")
            print(f"\tComputer's first card: {ai_deck[0]}")
    computer_drawing = True
    computer_lost = False
    if sum(ai_deck) > 21:
        computer_drawing = False
        lost_game = True

    #Determines the dealer/computer's final deck. 
    while computer_drawing:
        choice = random.choice([True, False])
        if choice == True:
            generate2 = generate_deck(1)
            for i in generate2:
                ai_deck.append(i)
            if sum(ai_deck) > 21:
                computer_drawing = False
                computer_lost = True
            if blackjack(ai_deck) == True:
                final_hands(player_deck, ai_deck)
                print("The computer has reached blackjack. You lost.")
                play_again = input("Would you like to play again? 'y' or 'n' ").lower()
                if play_again == 'n':
                    keep_playing = False
    
    #Measures for determining who wins.
    if computer_lost == True and lost_game == False:
        final_hands(player_deck, ai_deck)
        print("You stayed below. You won!")
    elif computer_lost == False and lost_game == True:
        final_hands(player_deck, ai_deck)
        print("You went over. You lost. ")
    elif computer_lost == True and lost_game == True:
        final_hands(player_deck, ai_deck)
        print("You went over and lost.")
    else:
        final_hands(player_deck, ai_deck)
        if sum(ai_deck) > sum(player_deck):
            print("You lost.")
        elif sum(ai_deck) < sum(player_deck):
            print("You won!!")
        else:
            print("It's a draw.")

    #Ask if a user want's to play the game again.
    play_again = input("Would you like to play again? 'y' or 'n' ").lower()
    if play_again == 'n':
        keep_playing = False
    if play_again == 'y':
        player_deck = []
        ai_deck = []

    


    