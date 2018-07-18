#!/usr/bin/env python
import ftplib

FTP_SERVER_URL = 'ftp.be.debian.org'
DOWNLOAD_DIR_PATH = '/pub/linux/network/wireless/'
DOWNLOAD_FILE_NAME = 'iwd-0.3.tar.gz'

def ftp_file_download(path, username):
	# open ftp connection
	ftp_client = ftplib.FTP(path, username)
	# list the files in the download directory
	ftp_client.cwd(DOWNLOAD_DIR_PATH)
	print("File list at %s:" %path)
	files = ftp_client.dir()
	print(files)
	# download a file
	file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
	ftp_cmd = 'RETR %s' %DOWNLOAD_FILE_NAME
	ftp_client.retrbinary(ftp_cmd,file_handler.write)
	file_handler.close()
	ftp_client.quit()

if __name__ == '__main__':
	ftp_file_download(path=FTP_SERVER_URL,username='anonymous')
