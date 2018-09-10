from Crypto.Cipher import DES

# How we use DES, the blocks are 8 characters
# Fill with spaces the user until 8 characters
user =  "user    "
password = "password"

# we create the cipher with DES
cipher = DES.new('mycipher')

# encrypt username and password
cipher_user = cipher.encrypt(user)
cipher_password = cipher.encrypt(password)

# we send credentials
print("User: " + cipher_user)
print("Password: " + cipher_password)


# We simulate the server where the messages arrive encrypted.
# we decode messages and remove spaces with strip ()
cipher = DES.new('mycipher')
decipher_user = cipher.decrypt(cipher_user).strip()
decipher_password = cipher.decrypt(cipher_password)

print("SERVER decipher:")
print("User: " + decipher_user)
print("Password: " + decipher_password)