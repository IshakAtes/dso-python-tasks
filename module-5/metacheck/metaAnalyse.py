import os
import csv
import argparse
from tqdm import tqdm
from PyPDF2 import PdfReader

def extract_metadata(pdf_path):
    """Extrahiert Metadaten aus einer einzelnen PDF-Datei."""
    try:
        reader = PdfReader(pdf_path)
        metadata = reader.metadata
        return {
            "Title": metadata.get("/Title", "Nicht vorhanden"),
            "Author": metadata.get("/Author", "Nicht vorhanden"),
            "Creator": metadata.get("/Creator", "Nicht vorhanden"),
            "Created": metadata.get("/CreationDate", "Nicht vorhanden"),
            "Modified": metadata.get("/ModDate", "Nicht vorhanden"),
            "Subject": metadata.get("/Subject", "Nicht vorhanden"),
            "Keywords": metadata.get("/Keywords", "Nicht vorhanden"),
            "Description": metadata.get("/Description", "Nicht vorhanden"),
            "Producer": metadata.get("/Producer", "Nicht vorhanden"),
            "PDF Version": metadata.get("/Version", "Unbekannt")
        }
    except Exception as e:
        print(f"Fehler beim Verarbeiten von {pdf_path}: {e}")
        return None

def process_pdfs(pdf_files, output_file):
    """Verarbeitet eine Liste von PDF-Dateien und speichert die Metadaten in einer CSV-Datei."""
    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Datei", "Title", "Author", "Creator", "Created", "Modified", "Subject", "Keywords", "Description", "Producer", "PDF Version"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for pdf in tqdm(pdf_files, desc="Verarbeite PDFs", unit=" Datei"):
            metadata = extract_metadata(pdf)
            if metadata:
                metadata["Datei"] = os.path.basename(pdf)
                writer.writerow(metadata)

def main():
    parser = argparse.ArgumentParser(description="Extrahiert Metadaten aus PDF-Dateien und speichert sie in einer CSV-Datei.")
    parser.add_argument("-f", help="Pfad zu einer einzelnen PDF-Datei", type=str)
    parser.add_argument("-d", help="Pfad zu einem Verzeichnis mit PDF-Dateien", type=str)
    parser.add_argument("-n", help="Name der Ausgabedatei", required=True)
    args = parser.parse_args()

    pdf_files = []
    if args.f:
        if os.path.isfile(args.f):
            pdf_files.append(args.f)
        else:
            print("Die angegebene Datei existiert nicht.")
            return
    elif args.d:
        if os.path.isdir(args.d):
            pdf_files = [os.path.join(args.d, f) for f in os.listdir(args.d) if f.endswith(".pdf")]
        else:
            print("Das angegebene Verzeichnis existiert nicht.")
            return
    else:
        print("Bitte entweder -f für eine Datei oder -d für ein Verzeichnis angeben.")
        return

    if not pdf_files:
        print("Keine PDF-Dateien gefunden.")
        return

    process_pdfs(pdf_files, args.n)
    print(f"Metadaten wurden in {args.n} gespeichert.")

if __name__ == "__main__":
    main()
