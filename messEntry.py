import Com
import encrypt

# TODO Rose:
# write a true loop so it constenly runs while started waiting on messages 
# if message comes in run through the recive message method 
# if send message type message and run through the send message method 
# socket layer work on together with azab and myself 
Server_ip = ""
client = Com.client_mode(Server_ip)


def sendMesg(client, message):
    newMessage = encrypt.xorEncript(message)
    encryptedMesg = encrypt.encryptMesg(newMessage)
    client.sendall(encryptedMesg)
    print(f"Sent Text: {encryptedMesg}")
    
def reciveMesg(client, message):
    decript1 = encrypt.decryptMesg(message)
    readMessage = encrypt.xorDecrypt(decript1)
    print(f"Message from {client} : {readMessage}")