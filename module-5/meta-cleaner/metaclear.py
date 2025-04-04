exiftool tmp.pdf | wc -l
qpdf --linearize tmp.pdf document.clean.pdf

rm tmp.pdf
mv document.clean.pdf document.pdf
