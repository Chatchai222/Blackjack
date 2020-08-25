# This is classes for dealer and the player
import random

class Card:
    def __init__(self, name, suit, value, faceup=True):
        self.name = name
        self.suit = suit
        self.value = value
        self.faceup = faceup

    def turn_faceup(self):
        if self.faceup:
            pass
        elif not self.faceup:
            self.faceup = True

    def turn_facedown(self):
        if not self.faceup:
            pass
        elif self.faceup:
            self.faceup = False

    def __repr__(self):
        return str(self.value) + self.suit


class Hand:
    def __init__(self, bet=0, state="Play"):
        self.cardlist = []
        self.bet = bet
        self.state = state


class Cardshoe:
    def __init__(self, deck=5, cutcard=75):
        self.cardlist = []
        self.cutcard = cutcard
        self.deck = deck
        self.create_deck()

    def create_deck(self):
        for x in range(self.deck):
            self.cardlist.append(Card("Ace", "Spade", 1))
            self.cardlist.append(Card("Two", "Spade", 2))
            self.cardlist.append(Card("Three", "Spade", 3))
            self.cardlist.append(Card("Four", "Spade", 4))
            self.cardlist.append(Card("Five", "Spade", 5))
            self.cardlist.append(Card("Six", "Spade", 6))
            self.cardlist.append(Card("Seven", "Spade", 7))
            self.cardlist.append(Card("Eight", "Spade", 8))
            self.cardlist.append(Card("Nine", "Spade", 9))
            self.cardlist.append(Card("Ten", "Spade", 10))
            self.cardlist.append(Card("Jack", "Spade", 10))
            self.cardlist.append(Card("Queen", "Spade", 10))
            self.cardlist.append(Card("King", "Spade", 10))

            self.cardlist.append(Card("Ace", "Heart", 1))
            self.cardlist.append(Card("Two", "Heart", 2))
            self.cardlist.append(Card("Three", "Heart", 3))
            self.cardlist.append(Card("Four", "Heart", 4))
            self.cardlist.append(Card("Five", "Heart", 5))
            self.cardlist.append(Card("Six", "Heart", 6))
            self.cardlist.append(Card("Seven", "Heart", 7))
            self.cardlist.append(Card("Eight", "Heart", 8))
            self.cardlist.append(Card("Nine", "Heart", 9))
            self.cardlist.append(Card("Ten", "Heart", 10))
            self.cardlist.append(Card("Jack", "Heart", 10))
            self.cardlist.append(Card("Queen", "Heart", 10))
            self.cardlist.append(Card("King", "Heart", 10))

            self.cardlist.append(Card("Ace", "Club", 1))
            self.cardlist.append(Card("Two", "Club", 2))
            self.cardlist.append(Card("Three", "Club", 3))
            self.cardlist.append(Card("Four", "Club", 4))
            self.cardlist.append(Card("Five", "Club", 5))
            self.cardlist.append(Card("Six", "Club", 6))
            self.cardlist.append(Card("Seven", "Club", 7))
            self.cardlist.append(Card("Eight", "Club", 8))
            self.cardlist.append(Card("Nine", "Club", 9))
            self.cardlist.append(Card("Ten", "Club", 10))
            self.cardlist.append(Card("Jack", "Club", 10))
            self.cardlist.append(Card("Queen", "Club", 10))
            self.cardlist.append(Card("King", "Club", 10))

            self.cardlist.append(Card("Ace", "Diamond", 1))
            self.cardlist.append(Card("Two", "Diamond", 2))
            self.cardlist.append(Card("Three", "Diamond", 3))
            self.cardlist.append(Card("Four", "Diamond", 4))
            self.cardlist.append(Card("Five", "Diamond", 5))
            self.cardlist.append(Card("Six", "Diamond", 6))
            self.cardlist.append(Card("Seven", "Diamond", 7))
            self.cardlist.append(Card("Eight", "Diamond", 8))
            self.cardlist.append(Card("Nine", "Diamond", 9))
            self.cardlist.append(Card("Ten", "Diamond", 10))
            self.cardlist.append(Card("Jack", "Diamond", 10))
            self.cardlist.append(Card("Queen", "Diamond", 10))
            self.cardlist.append(Card("King", "Diamond", 10))

    def shuffle_card(self):
        random.shuffle(self.cardlist)


class Cardbin:
    def __init__(self):
        self.cardlist = []


class Player:
    def __init__(self, money=10000):  # The box contains hands
        self.box = []
        self.money = money
        self.insurance = 0


class Dealer:
    def __init__(self, blackjack_rate=1.5):
        self.blackjack_rate = blackjack_rate
        self.cardlist = []

    # Pre-requisite methods
    def give_value_of_hand(self, hand):
        # Really proud of this :D
        # It gives the true value of a hand of blackjack (with ace helping the hand)
        hand_value = 0
        for eachcard in hand:
            hand_value += eachcard.value

        for eachcard in hand:
            if hand_value <= 11 and eachcard.name == "Ace":
                hand_value += 10

        return hand_value

    # Pregame set up
    def transfer_card_from_cardbin_to_cardshoe(self, cardbin, cardshoe):
        if len(cardshoe.cardlist) < cardshoe.cardcut:
            while len(cardbin.cardlist) > 0:
                for eachcard in cardbin.cardlist:
                    cardshoe.cardlist.append(eachcard)
                    cardbin.cardlist.remove(eachcard)

    def check_if_player_has_money(self, player):
        player_have_money = True
        if player.money <= 0:
            player_have_money = False
        return player_have_money

    def pregame_set_up(self, cardbin, cardshoe, player):
        self.transfer_card_from_cardbin_to_cardshoe(cardbin, cardshoe)
        self.check_if_player_has_money(player)

    # Initial card dealing
    def deal_card_to_player(self, player, cardshoe):
        # Deal with user input for bet (Not negative bet, enough money, not string input)
        allow_to_deal = False
        player_bet = input("Please enter your bet (int or float): ")
        while not allow_to_deal:
            try:
                player_bet = float(player_bet)
                allow_to_deal = True
                if player_bet > player.money or player_bet < 0:
                    allow_to_deal = False
                    player_bet = input("Insufficient money or negative bet, please re-enter your bet: ")
            except ValueError:
                player_bet = input("Wrong input, please re-enter your bet: ")

        # Subtract money from player
        player.money = player.money - player_bet

        # Move 'n' amount of card from cardshoe to the hand and put hand into player box
        n = 2
        begin_hand = Hand(player_bet)
        for x in range(n):
            begin_hand.cardlist.insert(0, cardshoe.cardlist.pop())

        player.box.append(begin_hand)

    def deal_card_to_dealer(self, cardshoe):
        # Deal 2 card and then turn one of them facedown
        self.cardlist.append(cardshoe.cardlist.pop)
        self.cardlist.append(cardshoe.cardlist.pop)
        self.cardlist[0].turn_facedown




    # The following method is for insurance bet part
    def check_for_dealer_ace(self):
        there_is_an_ace = False
        for card in self.cardlist:
            if card.faceup and (card.name == 'Ace'):
                there_is_an_ace = True
        return there_is_an_ace

    def ask_player_for_insurance_bet(self, player):
        allow_to_bet = False
        initial_bet = player.box[0].bet
        insurance_bet = input("Please enter the insurance bet (zero if you don't want to bet): ")
        while not allow_to_bet:
            try:
                insurance_bet = float(insurance_bet)
                allow_to_bet = True
                if insurance_bet > player.money or insurance_bet < 0 or insurance_bet > (initial_bet/2):
                    allow_to_bet = False
                    insurance_bet = input("Insufficient money or Negative/Wrong bet, please re-enter your bet: ")
            except ValueError:
                insurance_bet = input("Wrong input, please re-enter your bet: ")

        player.insurance = insurance_bet
        player.money = player.money - insurance_bet

    def payout_for_insurance(self, player):
        if player.insurance > 0:
            if Dealer.give_value_of_hand(self.cardlist) == 21:
                player.money += (player.insurance * 2)
                player.insurance = 0
            else:
                player.insurance = 0
                print("Insurance bet lost")

    # The following is for checking if player has blackjack and payout
    def check_for_player_blackjack(self, player):
        if self.give_value_of_hand(player.box[0].cardlist) == 21:
            if self.give_value_of_hand(self.cardlist) == 21:
                print("Bets are pushed dealer and player has blackjack")
            else:
                print("BLACKJACK!")
                player.money += player.box[0].bet * self.blackjack_rate

    def check_for_dealer_blackjack(self):
        if self.give_value_of_hand(self.cardlist) == 21:
            print("Dealer got blackjack, bad luck")

    def






























































