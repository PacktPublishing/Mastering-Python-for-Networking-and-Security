import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

encryptor = cipher.encryptor()
print(encryptor)

message_encrypted = encryptor.update("a secret message")

print("\n\nCipher text: "+message_encrypted)
ct =  message_encrypted + encryptor.finalize()

decryptor = cipher.decryptor()

print("\n\nPlain text: "+decryptor.update(ct))
