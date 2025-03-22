from PyPDF2 import PdfReader
import os


def read_meta(path):
    with open(path, 'rb') as _in:
        pdf = PdfReader(_in)
        meta = pdf.metadata
        pages = len(pdf.pages)
        print(path)
    creationdate = meta.get('/CreationDate', "Nicht vorhanden")
    moddate = meta.get('/ModDate', "Nicht vorhanden")
    title = meta.get('/Title', "Nicht vorhanden")
    subject = meta.get('/Subject', "Nicht vorhanden")
    author = meta.get('/Author', "Nicht vorhanden")
    creator = meta.get('/Creator', "Nicht vorhanden")
    producer = meta.get('/Producer', "Nicht vorhanden")
    print(meta)


def main():
    print('halo World')
    path = os.path.join(os.path.dirname(__file__), "Metadatenfaken.pdf")
    pdf = PdfReader(path)

    print("Metadaten:", pdf.metadata)  # Falls None, dann hat die Datei keine Metadaten
    print("Seiten:", len(pdf.pages))   # Prüfen, ob PDF Seiten hat

    read_meta(path)


if __name__ == "__main__":
    main()