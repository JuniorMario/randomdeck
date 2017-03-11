import glob, random

def card_it():
    carding = glob.glob("static/img/*.png")
    cards = []
    for i in carding:
        set(cards)
        if len(cards) < 4:
            choice = random.choice(carding)
            if choice not in cards: #gambiarra pra resolver meu problema com o set()
                cards.append(choice)
            else:
                pass
        else:
            pass
    return cards
