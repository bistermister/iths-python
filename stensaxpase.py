from random import randint

spelare_vinner = 0
dator_vinner = 0
winning_score = 1

while spelare_vinner < winning_score and dator_vinner < winning_score:
    print("Sten...")
    print("Sax...")
    print("Påse...")
    

    player = input("Make your move: ").capitalize()
    comp = randint(1, 3)
    if player == "quit" or player == "q":
        break

    if comp == 1:
        comp = "Sten"
    elif comp == 2:
        comp = "Påse"
    elif comp == 3:
        comp = "Sax"


    print("Datorns drag: " +comp)
    print("Spelarens drag: " +player)
    if player == comp:
        print("Oavgjort!\n")
    elif player == "Sten" and comp == "Sax":
        print("Spelare vinner!\n")
        spelare_vinner += 1
    elif player == "Påse" and comp == "Sten":
        print("Spelare vinner!\n")
        spelare_vinner += 1
    elif player == "Sax" and comp == "Påse":
        print("Spelare vinner! \n")    
        spelare_vinner += 1
    elif player == "Sax" and comp == "Sten":
        print("Dator vinner! \n")  
        dator_vinner += 1
    elif player == "Sten" and comp == "Påse":
        print("Dator vinner! \n")  
        dator_vinner += 1 
    elif player == "Påse" and comp == "Sax":
        print("Dator vinner! \n")  
        dator_vinner += 1
    else: 
        print("Du måste välja sten, sax eller påse! \n")


if dator_vinner > spelare_vinner:
    print(f"Spelet över, datorn vann!")
else: 
    print(f"Spelet över, spelaren vann!")
