import random

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3','4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
        'King']

''' Initialize the deck with size 52 to ensure no index errors since I choose
to not use the append function '''
deck = []

''' Create an ordered deck of cards from only the suits and ranks array
without having to type out all 52 cards by using a nested for loop'''
for i in range(len(suits)):
    for j in range(len(ranks)):
        deck.append(ranks[j] + " of " + suits[i])

def shuffleDeck():
    ''' Shuffles the unshuffled deck using the shuffle function from random '''
    random.shuffle(deck)


def dealCards(num):
    ''' Deals a given number of cards(num) to a player '''
    for i in range(num):
        print(deck.pop(i))

def getCardNumber(card):
    '''Replaces special ranks with numbers to work in integers '''
    card = card.replace('Ace', "1")
    card = card.replace('Jack', "10")
    card = card.replace('Queen', "10")
    card = card.replace('King', "10")
    card = int(card)
    return card

def whoseTurn(turn):
    '''Checks whose turn it is based on the remainder of a turn counter'''
    if turn % 2 == 0:
        return True
    elif turn % 2 == 1:
        return False
    else:
        return "Error"


def startGame():
    '''Starts the game in which the player's objective is to reach a
    sum of 21 using the cards they have drawn. Players are given the choice
    to either use the card they have drawn or to pass it up '''

    print("Welcome to sum 21! Press enter at any time to quit the game.\n\n\n")
    sum1 = 0 # Player 1's sum counter
    sum2 = 0 # Player 2's sum counter
    turn = 0 # Flag variable to figure out which player's turn it is

    while sum1 < 21 or sum2 < 21:

        if sum1 == 21 or sum2 > 21:
            ''' Check to see if player 1 has won'''
            print("Player 1 Wins!")
            break #Ends loop becuase game has finished
        if sum2 == 21 or sum1 > 21:
            '''Check to see if player 2 has won'''
            print("Player 2 Wins!")
            break # Ends loop becuase game has finished

        # Draw a card and remove it from the deck using pop
        cardDrawn = deck.pop()

        '''First if/else finds out which player's turn it is but does so
        in the form of a string so that only one set of conditionals
        is needed for the game to run '''
        if whoseTurn(turn):
            player = " 1 "
        else:
            player = " 2 "
        print("Player" + player + "draws " + cardDrawn)
        user = input("Pass? (Y/N) ")
        if user.lower() == "y":
            '''Player Draws and sum remains unchanged'''
            pass
        elif user.lower() == "n":
            '''Player chooses to use card and sum is changed by card's value'''
            blank = cardDrawn.find(' ')
            cardDrawn = cardDrawn[:blank]
            if whoseTurn(turn) == True:
                sum1 += getCardNumber(cardDrawn)
            else:
                sum2 += getCardNumber(cardDrawn)
        else:
            break

        turn += 1 # Increments the turn counter to show that it is the next
                    # player's turn



shuffleDeck()
startGame()
