possible_cards = "AKQJT98765432"[::-1]

class Hand:
    def __init__(self, hand: str, bid: int):
        self.bid = bid
        self.hand_type = self.getHandType(hand)
        self.first_card = self.getCardIndex(hand[0])

        self.hand_array = [self.getCardIndex(i) for i in hand]

        self.HandStats = [self.hand_type, self.hand_array, self.bid]

    def getHandType(self, hand):
        cards_distinct = ""
        for i in hand:
            if i not in cards_distinct: cards_distinct += i

        if len(cards_distinct) <= 2:
            match hand.count(cards_distinct[0]):
                case 5: return 6
                case 4 | 1: return 5
                case 3 | 2: return 4

        for i in hand:
            match hand.count(i):
                case 3: return 3
                case 2:
                    match len(cards_distinct):
                        case 3: return 2
                        case 4: return 1
        return 0

    def getHighCard(self, hand):
        for i in range(len(possible_cards)):
            if possible_cards[i] in hand: return possible_cards[::-1].index(possible_cards[i])

    def getCardIndex(self, card): return possible_cards.index(card)

def main():
    with open("7.txt","r",encoding="UTF-8") as f: text = f.readlines()

    hands = []
    for i in text: hands.append(Hand(i.split(" ")[0],int(i.split(" ")[1])).HandStats)

    hand_split = [[] for i in range(7)]
    for i in hands: hand_split[i[0]].append(i)

    for j in range(len(hand_split)):
        for k in range(4,-1,-1): hand_split[j] = sorted(hand_split[j], key = lambda x: int(x[1][k]))

    hands = []

    for i in hand_split:
        for j in i: hands.append(j)

    winnings = 0
    for i in range(len(hands)): winnings += hands[i][-1] * (i+1)

    return winnings

if __name__ == "__main__": print(main())