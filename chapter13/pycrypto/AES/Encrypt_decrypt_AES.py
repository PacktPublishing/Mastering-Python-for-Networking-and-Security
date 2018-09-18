
# AES pycrypto package
from Crypto.Cipher import AES

# key has to be 16, 24 or 32 bytes long
encrypt_AES = AES.new('secret-key-12345', AES.MODE_CBC, 'This is an IV-12')

# Fill with spaces the user until 32 characters
message = "This is the secret message      "

ciphertext = encrypt_AES.encrypt(message)
print("Cipher text: " , ciphertext)

# key must be identical
decrypt_AES = AES.new('secret-key-12345', AES.MODE_CBC, 'This is an IV-12')
message_decrypted =  decrypt_AES.decrypt(ciphertext)

print("Decrypted text: ",  message_decrypted.strip())