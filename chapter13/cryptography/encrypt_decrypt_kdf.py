import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = "password"

salt = os.urandom(16)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())

key = kdf.derive(password)

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())

#verify() method checks whether deriving a new key from 
#the supplied key generates the same key as the expected_key, 
#and raises an exception if they do not match.
kdf.verify(password, key)

key = base64.urlsafe_b64encode(key)
fernet = Fernet(key)
token = fernet.encrypt("Secret message")


print("Token: "+token)
print("Message: "+fernet.decrypt(token))