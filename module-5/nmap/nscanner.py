import socket
import argparse
import concurrent.futures

# Liste der bekannten Ports und ihrer Dienste
KNOWN_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
}

def scan_port(host, port):
    """Versucht, einen Port zu scannen."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                service = KNOWN_PORTS.get(port, "Unbekannter Dienst") if port <= 100 else "Unbekannt"
                return f"Port {port} ist offen ({service})"
            else:
                return f"Port {port} ist geschlossen"
    except Exception as e:
        return f"Fehler beim Scannen von Port {port}: {e}"

def scan_ports(host, min_port, max_port):
    """Scannt die angegebenen Ports parallel."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(host, p), range(min_port, max_port + 1))
        for result in results:
            print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Einfacher Port-Scanner in Python")
    parser.add_argument("host", help="IP-Adresse oder DNS-Name des Ziels")
    parser.add_argument("-p", help="Portbereich, z. B. 10-100 oder -p- für alle Ports", required=True)
    
    args = parser.parse_args()
    host = args.host
    
    if args.p == "-":
        min_port, max_port = 1, 65535
    else:
        try:
            min_port, max_port = map(int, args.p.split("-"))
            if not (0 <= min_port <= max_port <= 65535):
                raise ValueError("Ungültiger Portbereich")
        except ValueError:
            print("Bitte gib einen gültigen Portbereich an, z. B. 10-100 oder -p-")
            exit(1)
    
    print(f"Scanne {host} von Port {min_port} bis {max_port}...")
    scan_ports(host, min_port, max_port)
