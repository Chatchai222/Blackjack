# Code for transferring items from one list to another
from character import *
"""
class Food:
    def __init__(self, name ,score):
        self.name = name
        self.score = score

    def __repr__(self):
        return str(self.name)


a = Food("Apple", 7)
b = Food("Banana", 10)
c = Food("Coconut", 5)
d = Food("Durian", 9)
e = Food("Eggs", 7)

first_list = [a, b, c, d, e]
second_list = []

while len(first_list) > 0:
    for eachitem in first_list:
        second_list.append(eachitem)
        first_list.remove(eachitem)

print(first_list)
print(second_list)
"""

"""

a = Card("Ace", "Spade", 1)
b = Card("Two", "Spade", 2)
c = Card("Three", "Spade", 3)
d = Card("Four", "Spade", 4)
e = Card("Five", "Spade", 5)
f = Card("Six", "Spade", 6)
g = Card("Seven", "Spade", 7)
h = Card("Eight", "Spade", 8)
i = Card("Nine", "Spade", 9)
j = Card("Ten", "Spade", 10)
k = Card("Jack", "Spade", 10)

hand_list = [k,a]


def give_value_of_hand(hand):
    # Really proud of this :D
    hand_value = 0
    for eachcard in hand:
        hand_value += eachcard.value

    for eachcard in hand:
        if hand_value <= 11 and eachcard.name == "Ace":
            hand_value += 10

    return hand_value

my_value = str(give_value_of_hand(hand_list))
print(my_value)
"""
i = 7
while i > 5:
    x = input("Name: ")
    print(x)
    if x == "Doggo":
        print("stop eating my hw")
        continue

    print("You're name is not Doggo")










