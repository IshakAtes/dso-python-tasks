#Datenstrukturen

# ----------------Listen-Methoden-----------------------------------------
# Mithilfe von .append kann man der liste eine neue Zahl hinzufüge. Wenn du aber mehrere hinzufügen möchtest, dann kannst du es tun indem
# du die zweite liste mit der ersten addierst
zahlen = [1, 2, 3, 4, 5]

zahlen.append(6)
print(zahlen)
# Ausgabe: [1, 2, 3, 4, 5, 6]

# Mehrere listen zusammenfügen, indem man die listen zusammen addiert
neueZahlen = [10, 8, 9, 7]
total = zahlen + neueZahlen
print(total)
# Ausgabe: [1, 2, 3, 4, 5, 6, 10, 8, 9, 7]

# Liste Sortieren
total.sort()
print(total)
# Ausgabe: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Liste Absteigend Sortieren
total.sort(reverse=True)
print(total)
# Ausgabe: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Mit Count feststellen, wie oft etwas in der liste vorkommt
print(total.count(1))
# Ausgabe: 1

# Elemente aus der Liste entfernen
total.remove(10)
print(total)
# Ausgabe: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Ein Element in eine bestimmte Stelle in der Liste hinzufügen
total.insert(9, 0)
print(total)
# Ausgabe: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Die Liste Kopieren
kopieListe = total.copy()
print(kopieListe)
# Ausgabe: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Die Liste  leeren
total.clear()
print(total)
# Ausgabe: []
print(kopieListe)
# Ausgabe: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Nach einem Element in der Liste suchen und seinen Index-Wert erhalten
position = kopieListe.index(3)
print(position)
# Ausgabe: 6

# Prüfen ob ein Element in der liste enthalten ist oder nicht. Wir bekommen dann, ein True oder ein False.
print(11 in kopieListe)
# Ausgabe: False

# Elemente in einer Liste mit einem zeichen oder auch ohne zusammenführen
stringListe = ["I", "s", "h", "a", "k"]

print(";".join(stringListe))
# Ausgabe: I;s;h;a;k
print("".join(stringListe))
# Ausgabe: Ishak





# ----------------Tupel-----------------------------------------
# Ein Tupel ist eine unveränderliche Datenstruktur
# Unterschied zwischen Liste und tupel:
# Liste:
# teilnehmer = ["Flo", "Pam", "Pia", "Lea"] => Das ist eine Liste. Sie ist veränderbar. Man kann elemente (append) hinzufügen oder elemente (remove) entfernen
#
#  Tupel => Das Beispiel unten ist ein Tupel. Die Variable haben werte, die nicht veränderbar sind.
# p1 = (1,2)
# p2 = (2,1)
# print(type(p1))
# Ausgabe: <class 'tuple'>
# 
# Anderes Beispiel: Das unten ist auch ein Tupel. Wir returnen eine Datenmenge (Tupel), diese rückgabewerte sind nicht änderbar.
def rückgabe():
    return True, "Antwort", 42
ergebnis = rückgabe()

print(type(ergebnis))
# Ausgabe: <class 'tuple'>
print(ergebnis)
# (True, "Antwort", 42)

() # Das ist auch schon ein Tupel