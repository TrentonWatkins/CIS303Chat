import base64
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet


def keyGen():
    privKey = Fernet.generate_key()
    with open("private.pem", "wb") as priv_file:
        priv_file.write(privKey)
        

publicKey = "securepassword1"

def xorEncript(message):
    return ''.join(f'{ord(c) ^ ord(publicKey[i % len(publicKey)]):02x}' for i, c in enumerate(message))

def xorDecrypt(encryptedMesg):
    cipher_bytes = bytes.fromhex(encryptedMesg)

    decrypted_bytes = bytes([cipher_bytes[i] ^ ord(publicKey[i % len(publicKey)]) for i in range(len(cipher_bytes))])
    
    return decrypted_bytes.decode(errors='ignore')

def encryptMesg(message):
    key = load_private_key()
    cipher = AES.new(key, AES.MODE_CBC)
    cypText = cipher.encrypt(pad(message.encoder(),AES.block_size))
    return base64.b64encode(cipher.iv + cypText).decode()

def decryptMesg(encryptedMesg):
    key = load_private_key()
    encryptedData = base64.b64decode(encryptedMesg)
    iv = encryptedData[:16]
    cyptext = encryptedData[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cyptext),AES.block_size).decode()



def load_private_key():
    with open("private.pem", "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())
    return private_key



