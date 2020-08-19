# This is classes for dealer and the player
import random

class Card:
    def __init__(self, name, suit, value, faceup):
        self.name = name
        self.suit = suit
        self.value = value
        self.faceup = faceup
        pass

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


class Hand:
    def __init__(self, cardlist, bet, state):
        self.cardlist = cardlist
        self.bet = bet
        self.state = state


class Cardshoe:
    def __init__(self, cardlist=[], cutcard):
        self.cardlist = cardlist
        self.cutcard = cutcard
        pass

    def shuffle_card(self):
        random.shuffle(self.cardlist)



class Cardbin:
    def __init__(self, cardlist,):
        pass


class Player():
    def __init__(self, box, money):  # The box contains hands
        pass











class Dealer():
    def __init__(self):
        pass

    # Pregame checkup
    def transfer_card_from_bin_to_shoe(self, cardbin, cardshoe):
        for



    def check_if_player_has_money(self, player):
        player_have_money = True
        if player.money <= 0:
            player_have_money = False
        return player_have_money





    # The following method is for insurance bet part
    def check_for_dealer_ace(self, hand):
        there_is_an_ace = False
        for card in hand:
            if card.faceup and card.name == 'Ace':
                there_is_an_ace = True
        return there_is_an_ace

    def ask_player_for_insurance_bet(self, player):

        print("Would you like an insurance bet?")



    def check_value_of_hand(self, hand):
        pass

    def check_if_busted(self, hand, value):
        pass

    def move_card_from_bin_to_shoe(self, bin, shoe):
        pass

    def check_if_player_has_money(self, player, amount):
        pass

    def deal_card_to_dealer(self, dealer, shoe):
        pass

    def deal_card_to_player(self, player, shoe):
        pass

    def ask_player_for_insurance_bet(self, player):
        pass

    def check_for_black_jack(self, character):
        pass




