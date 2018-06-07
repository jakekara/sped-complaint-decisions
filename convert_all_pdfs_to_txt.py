""" Convert all the PDFs to text. Requires ocrmypdf, which can be brew installed """

import PyPDF2
import os
import subprocess

pdf_dir = "pdf"
txt_dir = "txt"


def do_year(year):

    print "Processing year: " + str(year)
    
    for fname in os.listdir(pdf_dir):

        if not fname.startswith(year): continue
        fpath = os.path.join(pdf_dir, fname)
        txtpath = os.path.join(txt_dir, fname + ".txt")
        if os.path.exists(txtpath): continue

        pdfFileObj = open(fpath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfReader.numPages
        pageObj = pdfReader.getPage(0)

        # pageObj.extractText().encode("ascii", "xmlcharrefreplace")
        txt = pageObj.extractText().encode("ascii", "xmlcharrefreplace")

        if len(txt) >= 10:
            open(txtpath,"wb").write(txt)

        if len(txt) < 10:

            ocrpath = os.path.join("searchable/", fname)
            # if os.path.exists(ocrpath): continue

            print("OCRing: " + fpath)         
            subprocess.call(["ocrmypdf", "--sidecar", txtpath, fpath, ocrpath])


for y in range(1, 18):
    pref = str(y).zfill(2)
    do_year(str(pref))
