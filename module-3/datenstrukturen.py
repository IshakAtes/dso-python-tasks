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


# Tupel Methoden

# Tupel sind nicht veränderbar, aber mann kann sie kombinieren
tupel= (1, 2, 3, 4)
neuerTupel = tupel + (5, 6, 7, 8)
print(neuerTupel)

# Tupel können auch ausgelesen werden
tupel= (1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1)
n = tupel.count(1)
print(n)

i = tupel.index(3)
print(i)

# Man kann Tupel auch kopieren, aber da Tupel eh nicht veränderbar sind, ist es auch nicht nötig
tupel= (1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1)
fakeTupel = tupel
print(tupel)
print(fakeTupel)


# Tupel in eine Liste umwandeln um sie verändern zu können
zahlen = (1, 6, 2, 0, 5)
zahlen = [1, 6, 2, 0, 5]

liste = list(zahlen)
liste.sort()
print(liste)





# ----------------Sets-----------------------------------------
# Set in python ist eine ungeordnete Sammlung von Elementen ohne Duplikate
# Das set kann auch nicht mit methoden wie sort sortiert werden. In einem Set ist es nicht so ohne Weiteres möglich, bestimmte Elemente auszulesen. Das
# liegt daran, dass hier keine Ordnung herrscht.
# In der praxis wird es angewendet mit " seen = set() " um festzustellen ob man schon eine bestimmte zahl oder elemente in einer schleife schon gesehen hat 

leeres_set = set()
print({12, 28, 38, 12, True, 29, "Ishak", 12})


# Set Methoden

# Uns interessiert bei Sets nicht, wo sich ein bestimmtes Element befindet,
# sondern ob ein bestimmtes Element überhaupt enthalten ist oder nicht.
# Dazu kannst du das Keyword in verwenden. Davor schreibst du das
# gesuchte Element und dahinter das Set, in dem du suchen möchtest.
# in , mit in kannst du prüfen ob dein statement im Set enthalten ist oder nicht.
meinSet = {12, 28, 38, 12, True, 29, "Ishak", 12}
print(12 in meinSet)

# add , etwas zum Set hinzufügen
meinSet.add(-1)
print(meinSet)

# remove , etwas vom Set entfernen
meinSet.remove(28)
print(meinSet)

# copy , das Set kopieren
kopie = meinSet.copy()
print(kopie)

# clear , etwas das Set entleeren
meinSet.clear()
print(meinSet)
print(kopie)

# list() , Set umwandeln in liste
prim = {5, 2, 33, 5, 3, 5, 7, 11}
primList = list(prim)
primList.sort()
print(primList)





# ----------------Dictionaries-----------------------------------------
telefonbuch = {
    "Junus" : "12345",
    "Florian": "1124352345",
    "Ishak": "24345"
}
print(telefonbuch.get("Ishak"))
print(telefonbuch)


# Dictionaries- Methods
passwort_hashes = {
    "abc123" : " e99a18c428cb38d5f260853678922e03",
    "1337" : " e48e13207341b6bffb7fb1622282247b",
    "love" : " b5c0b187fe309af0f4d35982fd961d7e"
}
# auslesen der Werte mit den [] eckigen klammern oder mit get()
print(passwort_hashes["abc123"])
print(passwort_hashes.get("ultrageheim"))

# Du kannst auch einen Default-Wert übergeben. Falls der Schlüssel nicht gefunden wird, wird der Default-Wert dem Schlüssen übergeben.
print(passwort_hashes.get("ultrageheim", "fe309ae48e132082247bf0f4d35982fd"))

# Ein Wert in der Dictionary updaten
telefonbuch = {
    "Junus" : "12345",
    "Florian": "1124352345",
    "Ishak": "24345"
}
# Ein Wert ändern
telefonbuch["Junus"] = "345354"
print(telefonbuch)

# einen neuen Schlüssel mit Wert hinzufügen
telefonbuch["Eva"] = "9876"
print(telefonbuch)

# oder einen neuen Schlüssel mit Wert also einen Dictionary mit der update() methode hinzufügen
telefonbuch.update({"Mehmet" : 567567})
print(telefonbuch)

# Einen Schlüssel aus dem Dictionary entfernen
del telefonbuch["Florian"]
print(telefonbuch)

# Dictionary Kopieren
fakeTelefonbuch = telefonbuch.copy()
print(fakeTelefonbuch)

# Dictionary leeren
telefonbuch.clear()
print(telefonbuch)
print(fakeTelefonbuch)

# Telefonbuch in Liste umwandeln
telefonbuch = {
    "Junus" : "12345",
    "Florian": "1124352345",
    "Ishak": "24345"
}

# Keys vom dictionary auslesen
print(list(telefonbuch.keys()))

# Werte vom dictionary auslesen
print(list(telefonbuch.values()))