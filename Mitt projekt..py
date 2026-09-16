class Game:
    def __init__(self, namn, genre, ar, betyg):
        self.namn = namn
        self.genre = genre
        self.ar = ar
        self.betyg = betyg

    def visa_info(self):
        print("Namn:", self.namn)
        print("Genre:", self.genre)
        print("År:", self.ar)
        print("Betyg:", self.betyg, "/10")
        print("--------------------")


# Här sparas alla spel
spel = []


# Funktion för att lägga till ett spel
def lagg_till():
    print("\n--- Lägg till spel ---")

    namn = input("Vad heter spelet? ")
    genre = input("Vilken genre är spelet? ")

    # Försöker få användaren att skriva ett nummer
    while True:
        try:
            ar = int(input("Vilket år kom spelet ut? "))
            break
        except:
            print("Skriv ett nummer.")

    # Betyget måste vara mellan 1 och 10
    while True:
        try:
            betyg = int(input("Ge spelet ett betyg mellan 1 och 10: "))

            if betyg >= 1 and betyg <= 10:
                break
            else:
                print("Betyget måste vara mellan 1 och 10.")

        except:
            print("Skriv ett nummer.")

    # Skapar ett nytt Game objekt
    nytt_spel = Game(namn, genre, ar, betyg)

    # Lägger spelet i listan
    spel.append(nytt_spel)

    print("Spelet har lagts till!")


# Funktion för att visa alla spel
def visa_spel():
    print("\n--- Alla spel ---")

    if len(spel) == 0:
        print("Det finns inga spel.")
    else:
        for ett_spel in spel:
            ett_spel.visa_info()


# Funktion för att söka efter ett spel
def sok():
    print("\n--- Sök efter spel ---")

    sokning = input("Skriv namnet på spelet: ")

    hittat = False

    for ett_spel in spel:
        if sokning.lower() in ett_spel.namn.lower():
            ett_spel.visa_info()
            hittat = True

    if hittat == False:
        print("Spelet hittades inte.")


# Funktion för att ta bort ett spel
def ta_bort():
    print("\n--- Ta bort spel ---")

    namn = input("Vilket spel vill du ta bort? ")

    for ett_spel in spel:
        if ett_spel.namn.lower() == namn.lower():
            spel.remove(ett_spel)
            print("Spelet har tagits bort.")
            return

    print("Spelet hittades inte.")


# Funktion för att ändra betyg
def andra_betyg():
    print("\n--- Ändra betyg ---")

    namn = input("Vilket spel vill du ändra? ")

    for ett_spel in spel:
        if ett_spel.namn.lower() == namn.lower():

            while True:
                try:
                    nytt_betyg = int(input("Nytt betyg 1-10: "))

                    if nytt_betyg >= 1 and nytt_betyg <= 10:
                        ett_spel.betyg = nytt_betyg
                        print("Betyget har ändrats.")
                        return
                    else:
                        print("Betyget måste vara mellan 1 och 10.")

                except:
                    print("Skriv ett nummer.")

    print("Spelet hittades inte.")


# Menyn
def meny():
    print("\n========================")
    print("       SPELREGISTER")
    print("========================")
    print("1. Lägg till spel")
    print("2. Visa alla spel")
    print("3. Sök efter spel")
    print("4. Ta bort spel")
    print("5. Ändra betyg")
    print("6. Avsluta")
    print("========================")


# Programmet körs här
while True:

    meny()

    val = input("Välj ett alternativ: ")

    if val == "1":
        lagg_till()

    elif val == "2":
        visa_spel()

    elif val == "3":
        sok()

    elif val == "4":
        ta_bort()

    elif val == "5":
        andra_betyg()

    elif val == "6":
        print("Programmet avslutas. Hej då!")
        break

    else:
        print("Felaktigt val. Försök igen.")

