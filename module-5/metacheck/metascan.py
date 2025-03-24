import os
import re
import csv
import argparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
from PyPDF2 import PdfReader

def get_pdfs_from_website(url):
    """Findet alle PDF-Links auf einer Webseite."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Webseite: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".pdf"):
            full_url = urljoin(url, href)
            pdf_links.append(full_url)

    return pdf_links

def download_pdf(pdf_url, save_dir):
    """Lädt eine PDF-Datei herunter und speichert sie im angegebenen Verzeichnis."""
    filename = os.path.basename(urlparse(pdf_url).path)
    save_path = os.path.join(save_dir, filename)

    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=8192):
                pdf_file.write(chunk)

        return save_path
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Herunterladen von {pdf_url}: {e}")
        return None

def extract_metadata(pdf_path):
    """Extrahiert Metadaten aus einer einzelnen PDF-Datei."""
    try:
        reader = PdfReader(pdf_path)
        metadata = reader.metadata or {}

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
            "PDF Version": reader.trailer["/Root"].get("/Version", "Unbekannt")
        }
    except Exception as e:
        print(f"Fehler beim Verarbeiten von {pdf_path}: {e}")
        return None

def process_pdfs(pdf_urls, output_file):
    """Lädt PDF-Dateien herunter, extrahiert Metadaten und speichert sie in einer CSV-Datei."""
    save_dir = "downloaded_pdfs"
    os.makedirs(save_dir, exist_ok=True)

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Datei", "Title", "Author", "Creator", "Created", "Modified", "Subject", "Keywords", "Description", "Producer", "PDF Version"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for pdf_url in tqdm(pdf_urls, desc="Verarbeite PDFs", unit=" Datei"):
            pdf_path = download_pdf(pdf_url, save_dir)
            if pdf_path:
                metadata = extract_metadata(pdf_path)
                if metadata:
                    metadata["Datei"] = os.path.basename(pdf_path)
                    writer.writerow(metadata)

def main():
    parser = argparse.ArgumentParser(description="Lädt PDFs von einer Webseite herunter und extrahiert Metadaten.")
    parser.add_argument("-u", help="URL der Webseite", required=True, type=str)
    parser.add_argument("-n", help="Pfad zur CSV-Ausgabedatei", required=True, type=str)
    args = parser.parse_args()

    pdf_urls = get_pdfs_from_website(args.u)
    if not pdf_urls:
        print("Keine PDFs gefunden.")
        return

    process_pdfs(pdf_urls, args.n)
    print(f"Metadaten wurden in {args.n} gespeichert.")

if __name__ == "__main__":
    main()
