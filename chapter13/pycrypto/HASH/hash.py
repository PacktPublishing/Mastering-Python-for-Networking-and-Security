from Crypto.Hash import MD5

def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = MD5.new()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

print('The MD5 checksum is' + md5Checksum('hash.py'))
