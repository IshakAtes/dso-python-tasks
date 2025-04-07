from PyPDF2 import PdfReader, PdfWriter
import os

# Using like this
# python metaChanger.py ~/Desktop/entfernen.pdf


def write_meta(full_path, metadata):
    print('path', full_path)
    
    path = os.path.dirname(full_path)  # Holt den Ordnerpfad
    filename = os.path.basename(full_path)  # Holt nur den Dateinamen
    
    writer = PdfWriter()
    tmp = os.path.join(path, f'tmp_{filename}')  # Sauberer temporärer Dateiname

    with open(full_path, 'rb') as pdf_in:
        pdf = PdfReader(pdf_in)
        for page in range(len(pdf.pages)):  # `getNumPages()` ist veraltet, `len(pdf.pages)` nutzen
            writer.add_page(pdf.pages[page])  # `addPage()` wurde in `add_page()` umbenannt
    
    # 🎭 NEUE METADATEN FAKEN (hier kannst du deine eigenen Daten setzen)
    fake_metadata = {
        "/Title": "Geheime PDF Datei",
        "/Author": "James FakeBond",
        "/Subject": "Vertraulich",
        "/Creator": "Python Skript",
        "/Producer": "PyPDF2"
    }

    writer.add_metadata(fake_metadata)

    with open(tmp, 'wb') as out:
        writer.write(out)  # `write()` muss außerhalb der Schleife stehen
    
    os.replace(tmp, full_path)
    print(f'Neue Datei mit gefälschten Metadaten gespeichert: {full_path}')




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
    
    del pdf

    with open(tmp, 'wb') as out:
        writer.write(out)  # `write()` muss außerhalb der Schleife stehen
    
    os.remove(full_path)
    os.rename(tmp, path + filename)
    print(f'Neue Datei ohne Metadaten gespeichert: {tmp, full_path}')



def read_meta(path):
    with open(path, 'rb') as _in:
        pdf = PdfReader(_in)
        meta = pdf.metadata
        pages = len(pdf.pages)

    write_meta(path, meta) # meta daten überschreiben
    # delete_meta(path) # meta daten löschen
    creationdate = meta.get('/CreationDate', "Nicht vorhanden")
    moddate = meta.get('/ModDate', "Nicht vorhanden")
    title = meta.get('/Title', "Nicht vorhanden")
    subject = meta.get('/Subject', "Nicht vorhanden")
    author = meta.get('/Author', "Nicht vorhanden")
    creator = meta.get('/Creator', "Nicht vorhanden")
    producer = meta.get('/Producer', "Nicht vorhanden")
    print(f'meta Bilgiler: {meta}')


def main():
    path = os.path.join(os.path.dirname(__file__), "entfernen.pdf")
    pdf = PdfReader(path)

    print("Metadaten:", pdf.metadata)  # Falls None, dann hat die Datei keine Metadaten
    print("Seiten:", len(pdf.pages))   # Prüfen, ob PDF Seiten hat

    write_meta(path, pdf.metadata)
    # read_meta(path)


if __name__ == "__main__":
    main()