# ---------------- Functions -----------------------------------------
# Beispiel-1
def greet(name, lastname):
    print(f"Hello {name} {lastname} !!!")

greet("Ishak", "Feuer")

# Beispiel-2
def addieren(a, b):
    summe = a + b
    return summe

s = addieren(11, 22)
print(f"Summe ist: {s}")





# ---------------- Args -----------------------------------------
# Was sind nun Args. Das Beispiel ist, wie wir normalierweise eine addieren funktion schreiben würden. Sie ist aber nicht dynamisch genug
def addieren(summand1, summand2, summand3):
    summe = summand1 + summand2 + summand3
    print(summe)

addieren(1, 2, 3)

# Wir schreiben jetzt einen Args Parameter, eine art Container oder Funktion die wir einmal definieren. Danach können wir sie mehrmals
# und in verschiedenen szenarien verwenden,da wir nicht an die anzahl der parameter gebunden sind.
def addieren(*summanden):
    print(sum(summanden))

addieren(99,-1,33)


# Args Parameter kombinieren
# Der positional Argument muss angegeben werden. Aber wenn ein stern dafür ist (*summanden), also wenn es ein args argument ist,
# dann muss auch kein parameter angegeben werden.
# Bemerkung: Es müssen immer als erstes die positional Arguments, also die normalen Variablen bzw parameter angegeben werden,
# erst danach kommt der Args Parameter, da er so viele x beliebige parameter aufnahmen kann.
def ausgabe(name, *summanden):
    print(f"Hallo {name}")
    print(f"Deine Zahlen: {summanden}")

ausgabe("ishak", 45, 45, 55, 99, 33)