import time
import random
 
name = input("Vad är ditt namn? ")
print(f"Hej {name}, dags för lite hänga gubbe!")
 
# En lista med ord som hangman slumpmässigt kommer plocka ifrån
words_universe = ["falukorv", "garderob", "husvagn", "kotte", "strykjärn"]
 
# Slumpa fram ett ord ur ovanstående lista
word = random.choice(words_universe)
 
# Räkna antal bokstäver i ordet:
char_count = len(word)
guesses = ''
 
# Antal omgångar
turns = 10
 
print(f"Ordet består av {char_count} bokstäver")
 
while turns > 0: # Kollar om omgångarna är fler än 0    
    failed = 0 # Startar en räknare som håller koll på felgissningarna
    for char in word: # För varje bokstav i word-variabeln
        if char in guesses: # Kolla om bokstaven finns i spelarens gissning
            print(char,end=""), # Skriv isf ut bokstaven
        else:
            print("_",end=""), # Om den inte finns, skriv ut ett underscore
            failed += 1 # Och öka antalet i failed-räknaren
   
    # Om failed är lika med 0
    if failed == 0:
        print(" - RÄTT! Du har vunnit!")
        break # Avsluta scriptet om spelaren har vunnit
   
    guess = input(" : Gissa en bokstav: ") # Be användaren gissa
   
    guesses += guess # Sätt spelarens gissningar till guesses
       
    # Om gissningen inte finns i det hemliga ordet
    if guess not in word:
        turns -= 1 # Ta bort ett försök från räknaren
        print("Fel!")
        print(f"Du har nu {turns} försök kvar")
   
        if turns == 0:
            print("Du har förlorat")
