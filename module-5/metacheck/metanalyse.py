from PyPDF2 import PdfReader, PdfWriter
import os

def delete_meta(full_path):
    print('path', full_path)
    
    path = os.path.dirname(full_path)  # Holt den Ordnerpfad
    filename = os.path.basename(full_path)  # Holt nur den Dateinamen
    
    writer = PdfWriter()
    tmp = os.path.join(path, f'tmp_{filename}')  # Sauberer temporärer Dateiname

    with open(full_path, 'rb') as pdf_in:
        pdf = PdfReader(pdf_in)
        for page in range(len(pdf.pages)):  # `getNumPages()` ist veraltet, `len(pdf.pages)` nutzen
            writer.add_page(pdf.pages[page])  # `addPage()` wurde in `add_page()` umbenannt
    
    with open(tmp, 'wb') as out:
        writer.write(out)  # `write()` muss außerhalb der Schleife stehen
    
    # os.remove(full_path)  # Falls du das Original löschen willst
    print(f'Neue Datei ohne Metadaten gespeichert: {tmp}')



def read_meta(path):
    with open(path, 'rb') as _in:
        pdf = PdfReader(_in)
        meta = pdf.metadata
        pages = len(pdf.pages)
        delete_meta(path)
    creationdate = meta.get('/CreationDate', "Nicht vorhanden")
    moddate = meta.get('/ModDate', "Nicht vorhanden")
    title = meta.get('/Title', "Nicht vorhanden")
    subject = meta.get('/Subject', "Nicht vorhanden")
    author = meta.get('/Author', "Nicht vorhanden")
    creator = meta.get('/Creator', "Nicht vorhanden")
    producer = meta.get('/Producer', "Nicht vorhanden")
    print(f'meta Bilgiler', meta)


def main():
    print('halo World')
    path = os.path.join(os.path.dirname(__file__), "Metadatenfaken.pdf")
    pdf = PdfReader(path)

    print("Metadaten:", pdf.metadata)  # Falls None, dann hat die Datei keine Metadaten
    print("Seiten:", len(pdf.pages))   # Prüfen, ob PDF Seiten hat

    read_meta(path)


if __name__ == "__main__":
    main()