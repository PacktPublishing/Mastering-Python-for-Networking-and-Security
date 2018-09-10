from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suite = Fernet(key)

print("Key "+str(cipher_suite))

message = "Secret message"

cipher_text = cipher_suite.encrypt(message)

plain_text = cipher_suite.decrypt(cipher_text)

print("\n\nCipher text: "+cipher_text)

print("\n\nPlain text: "+plain_text)