from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, random, struct

def decrypt_file(key, filename):
	
	chunk_size = 64*1024
	
	output_filename = os.path.splitext(filename)[0]
	
	#open the encrypted file and read the file size and the initialization vector. 
	#The IV is required for creating the cipher.
	with open(filename, 'rb') as infile:
		origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
		iv = infile.read(16)
		
		#create the cipher using the key and the IV.
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		
		#We also write the decrypted data to a verification file, 
		#so we can check the results of the encryption 
		#and decryption by comparing with the original file.
		with open(output_filename, 'wb') as outfile:
			while True:
				chunk = infile.read(chunk_size)
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))
				
			outfile.truncate(origsize)


password = "password"

def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()
	
decrypt_file(getKey(password), 'file.txt.encrypted');