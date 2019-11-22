#!/usr/bin/python3

#Self Written Module to Decrypt Files 

#=========================================================
#This Module is Written to Reverse_Attack of Ransomeware
#=========================================================
# Reverse_Attack
#	|____*****TAKES 1 ARGUMENTS, i.e. KEY *****
#	|____Initiate Decryption Process

from pathlib import Path  #Used to Find the Home Path
import threading #Using Threads to Boost Search Process BY Searching Diff. Drive on Diff. Thread
from os.path import expanduser
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib, base64

class Reverse:
    def __init__(self, key):
        self.decryption_key = key
        self.list_of_files = []

    def start(self):               
        home = self.get_home_dir()
        target1 = home + "Pictures"
        target2 = home + "Music"
        target3 = home + "Downloads"
        target4 = home + "Documents"
        target5 = home + "Desktop"
            
        t1 = threading.Thread(target=self.run_locate_class, args=[target1,])
        t2 = threading.Thread(target=self.run_locate_class, args=[target2,])
        t3 = threading.Thread(target=self.run_locate_class, args=[target3,])
        t4 = threading.Thread(target=self.run_locate_class, args=[target4,])
        t5 = threading.Thread(target=self.run_locate_class, args=[target5,])
        t1.start()   
        t1.join()   
        t2.start() 
        t2.join() 
        t3.start() 
        t3.join() 
        t4.start() 
        t4.join() 
        t5.start()
        t5.join()
        
        for files in self.list_of_files:
            decrypt = Decryptor(self.decryption_key, files)  
            decrypt.decrypt_file()   #Starting Decryption of Each File One-BY-One
    
    def get_home_dir(self):
        return str(Path.home()) + '\\'
    
    def run_locate_class(self, drive_name):
        '''
        Function to make Object of LocateTargetFiles Class
        '''
        starting = LocateEncryptedFiles()
        list_of_files = starting.start(drive_name)
        self.list_of_files.extend(list_of_files)
        return True
       
class LocateEncryptedFiles:
    def __init__(self, exclude = None):
        self.files_on_system = []
        self.target_extension = ['enc',]
        self.exclude_dir = [] 
        if exclude != None:
            self.exclude_dir.extend(exclude)

    def start(self, root_dir):
        self.locate_files(root_dir)
        return self.files_on_system

    def locate_files(self, root_dir):
        for root, _, files in os.walk(root_dir):
            for f in files:
                abs_file_path = os.path.join(root, f)
                self.filter(self.target_extension, abs_file_path)
                
    def filter(self, target_extension, abs_file_path):
        if self.is_excluded_dir(abs_file_path) == False:
            # Filtering Files On the basics of file extension
            if abs_file_path.split('.')[-1] in self.target_extension:
                self.files_on_system.append(abs_file_path) 
            else:
                pass

    def is_excluded_dir(self, path):
        '''
        @summary: Checks whether the specified path should be excluded from encryption
        @param path: The path to check
        @return: True if the path should be excluded from encryption, otherwise False
        '''
      
        for dir_to_exclude in self.exclude_dir:
            lenght = len(dir_to_exclude)
            if path[:lenght] == dir_to_exclude:
                return True          
        return False            

class Decryptor:
    def __init__(self, key, file_name):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self):
        with open(self.file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(self.file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(self.file_name)


if __name__ == '__main__':
    key = input("Enter Key : ")
    
    warning = input("\n!!!Warning!!! \nIs This Key Correct [Wrong KEY Will Just Destroy The Data]  y/n: ")
    if warning.lower() == 'y':
        print("\n[*] Reversing Attack ...")    
        print("\n[*] Initiating Decryption Process ...")
        test = Reverse(key) 
        test.start()
        print("\n[+] Completed Successfully : )")
    elif warning.lower() == 'n':
        print("\nPlease Try Later With Correct KEY !")
    else:
        print("\n[!] Invaid Argument : (")
