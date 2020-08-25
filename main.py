# This a program for a blackjack game in the console using OOP
import random
from character import *

cardshoe = Cardshoe()
cardbin = Cardbin()
player = Player(50000)
dealer = Dealer()

game_over = False

# Pregame setup phase #
dealer.transfer_card_from_cardbin_to_cardshoe(cardbin, cardshoe)
if not dealer.check_if_player_has_money(player):
    print("You're broke bruh...get out.")
    game_over = True

# Initial card dealing
dealer.deal_card_to_player(player, cardshoe)
dealer.deal_card_to_dealer(cardshoe)

#





# Insurance check
if dealer.check_for_dealer_ace():  # Dealer has a faceup ace card
    dealer.ask_player_for_insurance_bet(player)
    dealer.payout_for_insurance(player)

# Check for player blackjacks
if dealer.give_value_of_hand(player.box[0])














