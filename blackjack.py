import random

kortkategorier = ['Hjärter', 'Ruter', 'Klöver', 'Spader']
korts_list = ['Ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dam', 'Kung']
deck = [(kort, category) for category in kortkategorier for kort in korts_list]

def kort_value(kort):
    if kort[0] in ['Knekt', 'Dam', 'Kung']:
        return 10
    elif kort[0] == 'Ess':
        return 11
    else:
        return int(kort[0])
    
random.shuffle(deck)
spelare_kort = [deck.pop(), deck.pop()]
dealer_kort = [deck.pop(), deck.pop()]

# Spelarens tur
while True:
    spelare_poäng = sum(kort_value(kort) for kort in spelare_kort)
    dealer_poäng = sum(kort_value(kort) for kort in dealer_kort)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("\n")

    if spelare_poäng > 21:
        print("Dealern vinner (spelaren förlorar eftersom den är tjock (över 21 poäng))")
        break

    choice = input('Vad vill du göra? ["ge" för att få ytterligare kort, "stopp" för att stanna]: ').lower()
    if choice == "ge":
        nytt_kort = deck.pop()
        spelare_kort.append(nytt_kort)
        if spelare_poäng > 21:
            print("Dealern vinner (spelaren förlorar eftersom den är tjock (över 21 poäng))")
            break
    elif choice == "stopp":
        break
    else:
        print("Felaktigt val, försök igen.")
        continue


# Dealerns tur
while dealer_poäng < 17 and spelare_poäng < 22:
    nytt_kort = deck.pop()
    dealer_kort.append(nytt_kort)
    dealer_poäng += kort_value(nytt_kort)

if spelare_poäng < 22:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("\n")

# Räkna ut vem som vann
if dealer_poäng > 21 and spelare_poäng < 22:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("Spelaren vinner (Dealern förlorar för att den blev tjock (poäng över 21)")
elif spelare_poäng > dealer_poäng and spelare_poäng < 22:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("Spelaren vinner (spelaren har högre poäng än dealern)")
elif dealer_poäng > spelare_poäng and spelare_poäng < 22:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("Dealern vinner (dealern har högre poäng än spelaren)")
elif spelare_poäng > 22:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("Dealern vinner (spelaren är tjock (över 21 poäng))")
elif spelare_poäng == dealer_poäng:
    print("Dealerns kort:", dealer_kort)
    print("Dealerns poäng:", dealer_poäng)
    print("Spelarens kort:", spelare_kort)
    print("Spelarens poäng:", spelare_poäng)
    print("Det blev oavgjort.")