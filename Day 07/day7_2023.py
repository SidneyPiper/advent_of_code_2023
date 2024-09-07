with open("input.txt") as f:
    lines = f.readlines()


def starOne():
    five_of_kind = []
    four_of_kind = []
    full_house = []
    three_of_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        cards = list(line.split(" ")[0])
        value = int(line.split(" ")[1])

        cards_set = {card: cards.count(card) for card in cards}

        if len(cards_set) == 1:
            five_of_kind.append((cards, value))

        if len(cards_set) == 2:
            if 4 in cards_set.values():
                four_of_kind.append((cards, value))
            else:
                full_house.append((cards, value))

        if len(cards_set) == 3:
            if 3 in cards_set.values():
                three_of_kind.append((cards, value))
            else:
                two_pair.append((cards, value))

        if len(cards_set) == 4:
            one_pair.append((cards, value))

        if len(cards_set) == 5:
            high_card.append((cards, value))

    values = "AKQJT98765432"

    five_of_kind = sorted(
        five_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )
    four_of_kind = sorted(
        four_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )
    full_house = sorted(full_house, key=lambda word: [values.index(c) for c in word[0]])
    three_of_kind = sorted(
        three_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )
    two_pair = sorted(two_pair, key=lambda word: [values.index(c) for c in word[0]])
    one_pair = sorted(one_pair, key=lambda word: [values.index(c) for c in word[0]])
    high_card = sorted(high_card, key=lambda word: [values.index(c) for c in word[0]])

    cards = (
        five_of_kind
        + four_of_kind
        + full_house
        + three_of_kind
        + two_pair
        + one_pair
        + high_card
    )

    result = 0

    for i, card in enumerate(cards):
        result += (len(cards) - i) * card[1]

    print(result)


def starTwo():
    five_of_kind = []
    four_of_kind = []
    full_house = []
    three_of_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        cards = list(line.split(" ")[0])
        value = int(line.split(" ")[1])

        cards_set = {card: 0 for card in cards}

        for card in cards:
            cards_set[card] += 1

        if len(cards_set) == 1:
            five_of_kind.append((cards, value))

        if len(cards_set) == 2:
            if "J" in cards_set.keys():
                five_of_kind.append((cards, value))
            elif 4 in cards_set.values():
                four_of_kind.append((cards, value))
            else:
                full_house.append((cards, value))

        if len(cards_set) == 3:
            if "J" in cards_set.keys():
                if cards_set["J"] == 1:
                    cards_set.pop("J")
                    valueList = list(cards_set.values())
                    if valueList[0] == valueList[1]:
                        full_house.append((cards, value))
                    else:
                        four_of_kind.append((cards, value))
                else:
                    four_of_kind.append((cards, value))
            elif 3 in cards_set.values():
                three_of_kind.append((cards, value))
            else:
                two_pair.append((cards, value))

        if len(cards_set) == 4:
            if "J" in cards_set.keys():
                three_of_kind.append((cards, value))
            else:
                one_pair.append((cards, value))

        if len(cards_set) == 5:
            if "J" in cards_set.keys():
                one_pair.append((cards, value))
            else:
                high_card.append((cards, value))

    values = "AKQT98765432J"

    five_of_kind = sorted(
        five_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )

    four_of_kind = sorted(
        four_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )

    full_house = sorted(full_house, key=lambda word: [values.index(c) for c in word[0]])

    three_of_kind = sorted(
        three_of_kind, key=lambda word: [values.index(c) for c in word[0]]
    )

    two_pair = sorted(two_pair, key=lambda word: [values.index(c) for c in word[0]])

    one_pair = sorted(one_pair, key=lambda word: [values.index(c) for c in word[0]])

    high_card = sorted(high_card, key=lambda word: [values.index(c) for c in word[0]])

    cards = (
        five_of_kind
        + four_of_kind
        + full_house
        + three_of_kind
        + two_pair
        + one_pair
        + high_card
    )

    result = 0

    for i, card in enumerate(reversed(cards)):
        print("".join(card[0]) + " " + str(card[1]))
        result += (len(cards) - i) * card[1]

    print(result)


starTwo()
