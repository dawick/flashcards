import random

def print_card(card) :
    for word in card :
        print word, "      ",
    print ""


cards = [
	['One', '1'],
	['Two', '2'],
	['Three', '3'],
	['Four', '4'],
        ['Five', '5'],
	]


#bonus_words = len(cards)
card = ['', '']
blah = ['']

version = """
Please select your version:
(1) = Word
(2) = Number
(3) = Random
\n:"""

jon = raw_input(version)



while True :
    random.shuffle(cards)
    if len(cards) == 0:
        break
    
    card = cards.pop()
    if jon == '1':
        which = card[0]
    elif jon == '2':
        which = card[1]
    elif jon == '3':
        which = random.choice(card)
    else:
        print 'Something Odd'
        break

    print which
    if raw_input() == "q" :
        break
    print_card(card)

    ans = raw_input()
    if ans == "q" :
        break
    if ans != "" :
        # Save another copy of this word in the list
        cards.append(card)
        blah.append(card)


# Print the ones missed
print "\nMissed:"
#for card in cards[bonus_words:] :
#    print_card(card)
for card in blah:
    print_card(card)

