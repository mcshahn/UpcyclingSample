class Card():
    def __init__(self, rarity):
        self.rarity = rarity

    def get_rarity(self):
        return self.rarity

#let inputted_cards be a list of Cards that we want to upcycle into the system

#Version 1
def is_same_rarity(inputted_cards):
    rarity = inputted_cards[0].get_rarity()
    for card in inputted_cards:
        if card.get_rarity() != rarity:
            return False
    return True

def trading1(inputted_cards):
    #common to rare
    if (len(inputted_cards) == 10 and is_same_rarity(inputted_cards)):
        if inputted_cards[0].get_rarity() == "common":
            return #rare pack
        if inputted_cards[0].get_rarity() == "rare":
            return #very rare pack
        if inputted_cards[0].get_rarity() == "very rare":
            return #legendary pack

#Version 2 (threshold version + allows for mix of cards)
card_values = {"legendary": 125 , "very rare": 25, "rare": 5, "common": 1}
pack_values = {"rare": 10, "very rare": 50, "legendary": 250}


def trading2(inputted_cards):
    input_value = 0
    for Card in inputted_cards:
        input_value += card_values[Card.get_rarity()]
    
    if input_value > pack_values["legendary"]:
        return #legendary pack
    if input_value > pack_values["very rare"]:
        return #very rare pack
    if input_value > pack_values["rare"]:
        return #rare pack


#Version 3 (probability version + allows for mix of cards)
card_values = {"legendary": 125 , "very rare": 25, "rare": 5, "common": 1}
pack_values = {"rare": 10, "very rare": 50, "legendary": 250}

def trading3(inputted_cards):
    
