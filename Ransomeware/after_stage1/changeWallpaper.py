#!/usr/bin/env python

import ctypes, os, time, random

#=================================================================#
# Author : Pushpender Singh |  Website : https://technowlogy.tk   #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Python Module to Change Windows Wallpaper in Every Given Time   #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Mainly Developed for Open-Source Ransomeware project            #
#=================================================================#

class ChangeWallpaper:
    def __init__(self, directory=None):
        if directory == None:
            self.directory = os.getcwd().replace("\\", "\\\\") + "\\\\"
            self.path = ''
        else:
            self.directory = os.getcwd() + "\\" + directory
            self.path = "./" + directory + "/"

        
    def time_to_change_wallpaper(self, seconds=10):
        """
        Function Changes wallpaper after every Given time in seconds
        Params : time [In Seconds]
        """
        while True:
            img_list = self.list_all_img()
            img = self.random_img_selector(img_list)
            self.change_wallpaper(self.path + img)
            print(f"[*] Changing wallpaper again after {seconds} Seconds")
            time.sleep(seconds)

    def locate_images(self):
        list_of_all_files = []
    
        for root, _, files in os.walk(self.directory):
            for f in files:
                list_of_all_files.append(f)
                
        return list_of_all_files

    def list_all_img(self):
        """Function to return a list of image file in current working direcotry"""
        img_list = []
        img_extension = ['jpg', 'jpeg', 'png']
        file_list = self.locate_images()
        for img in file_list:
            a = len(img)
            b = a - 3
            if img[b:a] in img_extension:
                img_list.append(img)
        return img_list

    def random_img_selector(self, img):
        """Selects random Image from a given Image List"""
        img_list = img
        total_files = len(img_list)
        random_number = random.randint(0, total_files-1)
        img_selected = img[random_number]
        return img_selected

    def change_wallpaper(self, img):
        """
        Function to Change wallper [MAIN Function]
        Params : Image Path
        """
        img_path = os.getcwd() + "\\" +img
        print("\n[*] Changing Wallpaper ...")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
        print("[+] Wallpaper Changed Successfully!")
        

if __name__ == '__main__':
    change_wallpaper = ChangeWallpaper()
    change_wallpaper.time_to_change_wallpaper(10)