#!usr/bin/env python
# coding: utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter
import os, time, os.path, stat

from PyPDF2.generic import NameObject, createStringObject

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def get_metadata():
	for dirpath, dirnames, files in os.walk("pdf"):
		for data in files:
			ext = data.lower().rsplit('.', 1)[-1]
			if ext in ['pdf']:
				print(bcolors.OKGREEN + "------------------------------------------------------------------------------------")
				print(bcolors.OKGREEN + "[--- Metadata : " + bcolors.ENDC + bcolors.BOLD + "%s " %(dirpath+os.path.sep+data) + bcolors.ENDC)
				print(bcolors.OKGREEN + "------------------------------------------------------------------------------------")
				pdf = PdfFileReader(open(dirpath+os.path.sep+data, 'rb'))
				info = pdf.getDocumentInfo()

				for metaItem in info:

					print (bcolors.OKGREEN + '[+] ' + metaItem.strip( '/' ) + ': ' + bcolors.ENDC + info[metaItem])
					
				pages = pdf.getNumPages()
				print (bcolors.OKGREEN + '[+] Pages:' + bcolors.ENDC, pages)
				
				layout = pdf.getPageLayout()
				print (bcolors.OKGREEN + '[+] Layout: ' + bcolors.ENDC + str(layout))

				xmpinfo = pdf.getXmpMetadata()

				if hasattr(xmpinfo,'dc_contributor'): print (bcolors.OKGREEN + '[+] Contributor:' + bcolors.ENDC, xmpinfo.dc_contributor)
				if hasattr(xmpinfo,'dc_identifier'): print (bcolors.OKGREEN + '[+] Identifier:' + bcolors.ENDC, xmpinfo.dc_identifier)
				if hasattr(xmpinfo,'dc_date'): print (bcolors.OKGREEN + '[+] Date:' + bcolors.ENDC, xmpinfo.dc_date)
				if hasattr(xmpinfo,'dc_source'): print (bcolors.OKGREEN + '[+] Source:' + bcolors.ENDC, xmpinfo.dc_source)
				if hasattr(xmpinfo,'dc_subject'): print (bcolors.OKGREEN + '[+] Subject:' + bcolors.ENDC, xmpinfo.dc_subject)
				if hasattr(xmpinfo,'xmp_modifyDate'): print (bcolors.OKGREEN + '[+] ModifyDate:' + bcolors.ENDC, xmpinfo.xmp_modifyDate)
				if hasattr(xmpinfo,'xmp_metadataDate'): print (bcolors.OKGREEN + '[+] MetadataDate:' + bcolors.ENDC, xmpinfo.xmp_metadataDate)
				if hasattr(xmpinfo,'xmpmm_documentId'): print (bcolors.OKGREEN + '[+] DocumentId:' + bcolors.ENDC, xmpinfo.xmpmm_documentId)
				if hasattr(xmpinfo,'xmpmm_instanceId'): print (bcolors.OKGREEN + '[+] InstanceId:' + bcolors.ENDC, xmpinfo.xmpmm_instanceId)
				if hasattr(xmpinfo,'pdf_keywords'): print (bcolors.OKGREEN + '[+] PDF-Keywords:' + bcolors.ENDC, xmpinfo.pdf_keywords)
				if hasattr(xmpinfo,'pdf_pdfversion'): print (bcolors.OKGREEN + '[+] PDF-Version:' + bcolors.ENDC, xmpinfo.pdf_pdfversion)

				if hasattr(xmpinfo,'dc_publisher'):
					for y in xmpinfo.dc_publisher:
						if y:
							print (bcolors.OKGREEN + "[+] Publisher:\t" + bcolors.ENDC + y) 

			fsize = os.stat((dirpath+os.path.sep+data))
			print (bcolors.OKGREEN + '[+] Size:' + bcolors.ENDC, fsize[6], 'bytes \n\n')

get_metadata()
