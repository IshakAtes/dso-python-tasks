# ----------------if-elif-else-Anweisungen-----------------------------------------
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





# ----------------match-case-----------------------------------------
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





# ----------------for-Schleifen-----------------------------------------
# for-Schleifen / Die Schleife durchläuft jedes Element (hier: jedes Passwort) in der Liste nacheinander,
#  bis alle durchlaufen sind oder es durch ein break abgebrochen wird.
passwörter = ["abc123", "gehe1m", "test", "123456"]

for passwort in passwörter:
    print(passwort)
    if len(passwort) < 5:
        break





# ----------------While-Schleifen-----------------------------------------
# While-Schleifen / Läuft solange die Bedingung gegeben ist

# while-Schleifen Beispiel-1
x = 25
runde = 1

while x > 0:
    print(f"Runde: {runde}")
    runde += 1
    x -=1

# while-Schleifen Beispiel-2
name = input("Gib einen Namen ein! X zum Abbruch: ")
namensliste = []

while name != "X":
    namensliste.append(name)
    print(namensliste)
    name = input("Gib einen Namen ein! X zum Abbruch: ")





# ----------------Endlosschleifen-----------------------------------------
# Endlosschleifen
# ACHTUNG hier wurde bewusst ein Break eingebaut, damit es nicht unendlich läuft

teilnehmerliste = []

teilnehmer = input("Gib einen Namen für die Endlosschleife ein!: ")
i = 0

while True:
    teilnehmerliste.append(teilnehmer)
    print(teilnehmerliste)
    if len(teilnehmerliste) >= 1000:
        break

print(teilnehmerliste)



# Es gibt aber Fälle, in denen eine Endlosschleife tatsächlich erwünscht ist. Das ist z. B. bei einem
# Videospiel der Fall, das so lange laufen soll, bis der Spieler das Spiel beenden möchte. Hier
# spricht man von einer sogenannten Hauptereignisschleife, die so lange ausgeführt wird, bis der
# Benutzer das Programm beenden möchte. Als Beispiel schauen wir uns den folgenden
# Ausschnitt aus einem Spiel an, das mit der Bibliothek pygame entwickelt wurde:

# weiter = True
# while weiter:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             weiter = False

# In Zeile 1 wird mit weiter ein Schalter gesetzt, der dann kontinuierlich abgefragt wird. In
# Zeile 3 werden alle Events, die im Spiel auftreten, abgefangen und nacheinander
# durchgegangen. In Zeile 4 wird geprüft, ob das Event pygame.QUIT dabei war, d. h., der
# Spieler möchte das Spiel beenden. Erst dann wird der Wert von weiter auf False gesetzt und
# die Schleife dadurch beendet. Hier ergibt es Sinn, eine (zumindest temporäre) Endlosschleife
# einzusetzen, da man ansonsten bspw. erraten müsste, wann der Spieler sein Spiel beenden
# möchte. Eine weitere Anwendung von Endlosschleifen findet man bei der Client-/Server-
# Programmierung. Der Server muss ständig laufen, um Anfragen von den Client-Programmen bei
# Bedarf entgegennehmen zu können.





# ----------------Walross-Operator-----------------------------------------
# Walross-Operator
# Mit dem Walross-Operator := können wir jetzt direkt die Nutzer eingabe in einer Variable (teilnehmer) abspeichern
# und der Bedingung der While schleife eingeben. Diese Variable wird jetzt verglichen ob es (!=) nicht gleich X ist.
# Wenn es nicht gleich X ist, wird die Schleife fortgesetzt. Andernfalls wird die Schleife beendet und die teilnehmerliste wird geprinted

teilnehmerliste = []

while (teilnehmer := input("Bitte gib einen Teilnehmer ein (X): ")) != "X":
    teilnehmerliste.append(teilnehmer)

print(teilnehmerliste)