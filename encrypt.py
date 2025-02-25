import base64
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def keyGen():
    key = os.urandom(32)
    privKey =base64.b64encode(key).decode()
    filename = 'private.txt'
    with open(filename, "w") as file:
        file.write(privKey)


publicKey = "securepassword1"

def xorEncript(message):
    return ''.join(f'{ord(c) ^ ord(publicKey[i % len(publicKey)]):02x}' for i, c in enumerate(message))

def xorDecrypt(encryptedMesg):
    cipher_bytes = bytes.fromhex(encryptedMesg)

    decrypted_bytes = bytes([cipher_bytes[i] ^ ord(publicKey[i % len(publicKey)]) for i in range(len(cipher_bytes))])
    
    return decrypted_bytes.decode(errors='ignore')

def encryptMesg(message):
    key = load_key()
    cipher = AES.new(key, AES.MODE_CBC)
    cypText = cipher.encrypt(pad(message.encode(),AES.block_size))
    sendMESG = base64.b64encode(cipher.iv + cypText).decode()
    with open("Mesg.txt", "w") as file:
        file.write(sendMESG)
    return sendMESG

def decryptMesg(encryptedMesg):
    key = load_key()
    encryptedData = base64.b64decode(encryptedMesg)
    iv = encryptedData[:16]  # Extract IV
    cyptext = encryptedData[16:]  # Extract only the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cyptext), AES.block_size).decode()



def load_key(filename="private.txt"):
    with open(filename, "r") as file:
        key = file.read()  # Read Base64-encoded key
    return base64.b64decode(key)

# CopyRight@Watkins2025
