#Datenstrukturen

# ----------------Listen-Methoden-----------------------------------------
# Mithilfe von .append kann man der liste eine neue Zahl hinzufüge. Wenn du aber mehrere hinzufügen möchtest, dann kannst du es tun indem
# du die zweite liste mit der ersten addierst
zahlen = [1, 2, 3, 4, 5]

zahlen.append(6)
print(zahlen)

# Mehrere listen zusammenfügen, indem man die listen zusammen addiert
neueZahlen = [10, 8, 9, 7]
total = zahlen + neueZahlen
print(total)

# Liste Sortieren
total.sort()
print(total)

# Liste Absteigend Sortieren
total.sort(reverse=True)
print(total)

# Mit Count feststellen, wie oft etwas in der liste vorkommt
print(total.count(1))

# Elemente aus der Liste entfernen
total.remove(10)
print(total)

# Ein Element in eine bestimmte Stelle in der Liste hinzufügen
total.insert(9, 0)
print(total)

# Die Liste Kopieren
kopieListe = total.copy()
print(kopieListe)

# Die Liste  leeren
total.clear()
print(total)
print(kopieListe)

# Nach einem Element in der Liste suchen und seinen Index-Wert erhalten
position = kopieListe.index(3)
print(position)

# Prüfen ob ein Element in der liste enthalten ist oder nicht. Wir bekommen dann, ein True oder ein False.
print(11 in kopieListe)

# Elemente in einer Liste mit einem zeichen oder auch ohne zusammenführen
stringListe = ["I", "s", "h", "a", "k"]

print(";".join(stringListe))
print("".join(stringListe))