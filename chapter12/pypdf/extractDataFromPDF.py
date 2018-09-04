# -*- encoding: utf-8 -*-

from PyPDF2 import PdfFileReader
import os 

def printMetaDataPDF():
    for dirpath, dirnames, files in os.walk("pdf"):
        for name in files:
            ext = name.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
                print ("[+] Metadata for file: %s " %(dirpath+os.path.sep+name))
                pdfFile = PdfFileReader(open(dirpath+os.path.sep+name, 'rb'))
                docInfo = pdfFile.getDocumentInfo()
                for metaItem in docInfo:
                    print('[+] ' + metaItem + ':' + docInfo[metaItem])
                print("\n")
				
printMetaDataPDF()