# Alle methoden anzeigen
# print(dir(str))

# Zwingt unseren String 10 zeichen zu haben, und füllt die leeren stellen mit 0.
print("Ishak".zfill(10))

# Alle Zeichen in unserem String werden Groß angezeigt.
print("Ishak".upper())

# Alle Zeichen in unserem String werden klein angezeigt.
print("IsHAk!".lower())

# Nur der Anfangsbuchstabe wird groß geschrieben, der Rest klein.
print("isHAk!".capitalize())

# Sind alle Buchstaben im String Groß? wenn ja wird true ausgegeben sonst false.
print("ISHAK!".isupper())

# Prüft ob alle Zeichen im String Zahlen sind. Wenn ja wird true ausgegeben, sonst false.
print("45645465123".isnumeric())

# Prüft ob alle Zeichen im String Buchstaben sind. Wenn ja wird true ausgegeben, sonst false.
print("Ishak".isalpha())

# Wenn du dateien oder Namen aus einer Datei ziehst werden die Daten manchmal so wie hier angezeigt.
# In so einem Fall, kann mann mit der methode: split simicolon,
# den String an den stellen, wo ein simicolon ist unterbrechen und die Namen werden dann in einem Array bzw. liste angezeigt
print("Ishak;Mike;Mia;Marco".split(';'))

# mit dem Backslash-n \n werden die namen einzelnd untereinander angezeigt mit zeilenumbrüchen
print("Ishak\nMike\nMia\nMarco")

# mit dem Backslash-n \n werden die namen einzelnd untereinander angezeigt mit zeilenumbrüchen
# mit splitlines werden die namen in einer liste eingetragen
print("Ishak\nMike\nMia\nMarco".splitlines())

# mit strip werden die leerzeichen vor und nach dem String entfernt, aber nicht die in der mitte
print("     Ishak      ".strip())
print("     Is  h  ak      ".strip())

# mit replace kannst du bestimmte zeichen durch andere ersetzen. In unserem Beispiel wird das leerzeichen durch nichts ersetzt
# Somit werden die leerzeichen vor und nach dem String entfernt, aber im gegesatz zu strip auch die leerzeichen in der mitte werden entfernt
print("     Ishak      ".replace(" ", ""))
print("     Is  h  ak      ".replace(" ", ""))

# Prüft wie oft etwas vorkommt
print("Wasserfall, Abfall".count('fall'))

# Prüft an welcher stelle etwas ist, was wir suchen bzw. was wir als parameter übergeben haben und gibt uns den index zurück
# Problematik: Wirft ein fehler, wenn nichts gefunden wird
print("Wasserfall, Abfall".index('s'))

# Sucht an welcher stelle unser parameter vorkommt
# Problematik: Wirft kein fehler, wenn nichts gefunden wird aber gibt stattdesen -1 zurück, wenn nichts gefunden wurde
print("Wasserfall, Abfall".find('f'))

# Gibt ein Wahrheitswert zurück. Ist unser parameter enthalten oder nicht.
# In unserem Beispiel ist a in Wasserfall enthalten oder nicht. Wenn ja dann bekommen wir True als boolean zurück, sonst false
print("a" in "Wasserfall")

# [::-1] Dies ist keine Methode sondern eine slicing variante, die sehr häufig verwendet wird,
# um den String zu verdrehen bzw. zu reversen (9876543210), deshalb steht es hier in der Liste
print("0123456789"[::-1])