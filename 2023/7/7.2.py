all_cards = "AKQT98765432J"[::-1]

class Hand:
    def __init__(self, hand: str, bid: int):
        self.bid = bid
        self.hand_jokerized = jokerize(hand)
        self.hand_type = self.getHandType(self.hand_jokerized)
        self.first_card = getCardIndex(self.hand_jokerized[0])

        self.hand_array = [getCardIndex(i) for i in hand]
        self.hand_array_jokerized = [getCardIndex(i) for i in self.hand_jokerized]

        self.HandStats = [self.hand_type, self.hand_array, self.hand_array_jokerized, self.bid]

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

def getCardIndex(card): return all_cards.index(card)

def jokerize(hand:str):
    if hand == "JJJJJ": return "AAAAA"
    if "J" not in hand: return hand

    cards_distinct = []
    j_indexes = []
    lhand = list(hand)

    for i in range(len(hand)):
        if hand[i] != "J" and [getCardIndex(hand[i]),hand.count(hand[i])] not in cards_distinct: cards_distinct.append([getCardIndex(hand[i]),hand.count(hand[i])])
        if i not in j_indexes and hand[i] == "J": j_indexes.append(i)

    split_cards_distinct = [[] for i in range(len(all_cards))]
    for i in cards_distinct: split_cards_distinct[i[0]].append(i)

    cards_distinct = []

    for i in split_cards_distinct[::-1]:
        for j in i:
            cards_distinct.append(j)

    cards_distinct = sorted(cards_distinct, key=lambda x: int(x[1]), reverse=True)
    del split_cards_distinct

    replacement_card = all_cards[cards_distinct[0][0]]
    for i in j_indexes: lhand[i] = replacement_card
    return "".join(lhand)

def sortHands(hands:list):

    hand_split = [[] for i in range(7)]
    for i in hands: hand_split[i[0]].append(i)

    for j in range(len(hand_split)):
        for k in range(4,-1,-1): hand_split[j] = sorted(hand_split[j], key = lambda x: int(x[1][k]))

    hands = []

    for i in hand_split:
        for j in i: hands.append(j)

    return hands

def main():
    with open("7.txt","r",encoding="UTF-8") as f: text = f.readlines()

    hands = []

    for i in text: 
        arr = i.split(" ")
        hand = arr[0]
        bid = int(arr[1])

        hands.append(Hand(hand,bid).HandStats)

    hands = sortHands(hands)

    winnings = 0
    for i in range(len(hands)): winnings += hands[i][-1] * (i+1)

    return winnings

if __name__ == "__main__": print(main())