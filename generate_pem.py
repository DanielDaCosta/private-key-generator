from Crypto.PublicKey import RSA


KEY = """{PASTE YOUR KEY IN HERE}"""
privateKey = RSA.importKey(KEY)
privKey = privateKey.exportKey('PEM') 
with open("testing.pem", "w") as prv_file:
    prv_file.write(privKey.decode())