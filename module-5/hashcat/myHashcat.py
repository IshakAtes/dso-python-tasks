import argparse
import hashlib
import itertools
import string

def hash_function(algorithm, text):
    hash_algorithms = {
        "0": hashlib.md5,
        "1": hashlib.sha1,
        "2": hashlib.sha256,
        "3": hashlib.sha512
    }
    
    hash_func = hash_algorithms.get(algorithm)
    if hash_func:
        return hash_func(text.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash mode")

def brute_force_attack(hash_value, algorithm, max_length=6):
    characters = string.ascii_lowercase + string.digits
    
    for length in range(1, max_length + 1):
        for candidate in itertools.product(characters, repeat=length):
            candidate_password = ''.join(candidate)
            if hash_function(algorithm, candidate_password) == hash_value:
                return candidate_password
    return None

def dictionary_attack(hash_value, algorithm, dictionary_file):
    try:
        with open(dictionary_file, "r", encoding="utf-8") as file:
            for line in file:
                password = line.strip()
                if hash_function(algorithm, password) == hash_value:
                    return password
    except FileNotFoundError:
        print("Dictionary file not found.")
    return None

def main():
    parser = argparse.ArgumentParser(description="Simple Hash Cracker")
    parser.add_argument("-m", required=True, help="Hash mode: MD5 (0), SHA-1 (1), SHA-256 (2), SHA-512 (3)")
    parser.add_argument("-a", required=True, help="Attack mode: Brute-Force (0), Dictionary (1)")
    parser.add_argument("-H", "--hash", help="Hash value")
    parser.add_argument("-F", "--file", help="File containing hash value")
    parser.add_argument("-d", "--dictionary", help="Dictionary file (required for dictionary attack)")
    
    args = parser.parse_args()
    
    # Hole Hash-Wert aus Parameter oder Datei
    if args.hash:
        hash_value = args.hash
    elif args.file:
        try:
            with open(args.file, "r") as file:
                hash_value = file.read().strip()
        except FileNotFoundError:
            print("Hash file not found.")
            return
    else:
        print("Hash value is required.")
        return
    
    # Angriff starten
    if args.a == "0":
        print("Starting Brute-Force attack...")
        password = brute_force_attack(hash_value, args.m)
    elif args.a == "1":
        if not args.dictionary:
            print("Dictionary file required for dictionary attack.")
            return
        print("Starting Dictionary attack...")
        password = dictionary_attack(hash_value, args.m, args.dictionary)
    else:
        print("Invalid attack mode.")
        return
    
    # Ergebnis ausgeben
    if password:
        print(f"Password found: {password}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
