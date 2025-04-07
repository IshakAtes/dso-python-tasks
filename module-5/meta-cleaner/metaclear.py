# steps in bash
# exiftool -all= document.pdf -o tmp.pdf
# qpdf --linearize tmp.pdf document.clean.pdf

# rm tmp.pdf
# mv document.clean.pdf document.pdf
# -------------------------------------
import argparse
import subprocess
import os

def remove_metadata(pdf_file):
    tmp_pdf = "tmp.pdf"
    cleaned_pdf = "document.clean.pdf"

    print(pdf_file)
    # pdf daten auslesen
    # 1. Metadaten entfernen mit exiftool → tmp.pdf erzeugen
    subprocess.run(["exiftool", "-all=", pdf_file, "-o", tmp_pdf], check=True)

    # 2. Linearize mit qpdf → document.clean.pdf erzeugen
    subprocess.run(["qpdf", "--linearize", tmp_pdf, cleaned_pdf], check=True)

    # 3. tmp.pdf löschen
    os.remove(tmp_pdf)

    # 4. clean.pdf → original überschreiben
    os.replace(cleaned_pdf, pdf_file)
    
    print(f"[+] Metadaten erfolgreich entfernt: {pdf_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF-Metadaten entfernen")
    parser.add_argument("pdf", help="Pfad zur PDF-Datei")
    args = parser.parse_args()

    remove_metadata(args.pdf)