import argparse

# Parser erstellen
parser = argparse.ArgumentParser(description='Beispiel')

# Argumente hinzufügen
parser.add_argument('-f', '--file', type=str, help='Dateiname zum Lesen')
parser.add_argument('-v', '--verbose', action='store_true', help='Aktiviere ausführliche')

# Argument parsen
args = parser.parse_args()

# Zugriff auf die analysierten Argumente
if args.verbose:
    print('Verbose-Modus aktiviert')

if args.file:
    print(f'Datei zu Lesen: {args.file}')
else:
    print('Keine Datei angegeben')