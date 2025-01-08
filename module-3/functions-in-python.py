# if-elif-else-Anweisungen
note = input("Gib die Note ein: ")

if note == "1":
    print("Sehr gut!")
elif note == "2":
    print("Gut!")
elif note == "3":
    print("Befriedigend.")
elif note == "4":
    print("Ausreichend.")
elif note == "5":
    print("Mangelhaft!")
else:
    print("Ungenügend!!!")

# --------------------------------------------------------------------------------

# match-case
note = [1,11,111]

match note:
    case [1,11,111]: # Du kannst auch Objekte übergeben
        print("Mathe Genie")
    case "1":
        print("Sehr gut!")
    case "2":
        print("Gut!")
    case "3":
        print("Befriedigend.")
    case "4":
        print("Ausreichend.")
    case "5":
        print("Mangelhaft!")
    case _:
        print("Ungenügend!!!")

# --------------------------------------------------------------------------------

# for-Schleifen
passwörter = ["abc123", "gehe1m", "test", "123456"]

for passwort in passwörter:
    print(passwort)
    if len(passwort) < 5:
        break