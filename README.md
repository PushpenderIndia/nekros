<p align="center">
  <img src="https://github.com/PushpenderIndia/nekros/blob/master/images/Text_LOGO.png" alt="NekRos Logo" Logo" />
</p>

<h1 align="center">NekRos - Ransomeware</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/nekros/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/nekros/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/PushpenderIndia/nekros">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

             
                        This Awesome Project will Just Blow Your Mind, The Most Scarest Ransomeware.

NekRos is a Ransomeware Generator for Windows, which is written in Python 3, NekRos means DEAD in Greek, now you can imagine that why I named it NekRos.

Project is made for good purpose, unethical use is prohibited, misuse of this project can lead you behind the Bar/Jail, Porject is made to give Practical and Deep Knowledge of Ransomeware and their side effects.

It is the responsibility of end user to use this Software ethically and for testing purpose only : )

## NekRos - THE MOST Scariest Ransomeware
![](/images/Banner.jpg)

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## What is Ransomeware ?

<p align="center">
  <img src="https://github.com/PushpenderIndia/nekros/blob/master/images/Ransomware-Photo.png" alt="Ransomeware Scenario" width=350 height=350 />
</p>

**Ransomware** is a type of malware which **encrypts** the Data of Victim's PC making **Data un-usable**, they are mainly published to Encrypt victim's data which **perpetually block the access** to data unless a ransom is paid to Attacker/Hacker so that Decryption/Recovery of Data could be done. 

## Warning : PAY ATTENTION

<p align="center">
  <img src="https://github.com/PushpenderIndia/nekros/blob/master/images/warning_img.png" alt="Warning Image" />
</p>

If you are using this software then it means you agrees our T&C i.e Any misuse of this software, **YOU - THE END USER** is responsile and not the author.

Our aim of building this software is to give the Practical Knowledge of Ransomeware so that we can Build a Better Cyber Army Which can fight against the Cyber Crimes.

The primary (and original) goal of this project was to provide a proof-of-concept which demonstrated Python's capabilities as a language for real-world malware development as **Traditionally** C, C++ is used to Create Stuff like this.

## Note : Project Under Development

#### TODO 
- [ ] Making GUI Ransomeware Generator
- [ ] Implement Change language Function
- [ ] Improve C&C Server/Website, put some checks that if **payment == True**, then only Retrive Key from Database.
- [ ] Add New Features

#### By Default, Ransomeware Targets .lol, .mrrobot extension files
**Even thought not suggested**, But You Can test it even on your main system, as by default it targets **.lol** and **.mrrobot** extensions file, for testing purpose make your own files with these entensions and then run **main.py**

## Features
- [x] Works on Windows.
- [x] Generates Unique Machine ID for Victim System's Identification.
- [x] Generates Purely **Random** Encryption/Decryption KEY (**MD5 hash**), thus no chance of Making Keygen of This Ransomeware. 
- [x] Decryption/Recovery of Data is only Possible with Valid Key only.
- [x] Changes Wallpaper after Given Interval of Time (In seconds).
- [x] Server (Website) Integrated with Ransomeware which can be used to Retrive **KEY**.
- [x] Searches for Sensitive Files on Default target location.
- [x] Only Encrypt Target Specified Extension files  (Customizable)
- [x] Export KEY to Server before Encryption Process takes place.
- [x] Stylish and Scariest GUI Which looks like WannaCry Ransomeware
- [x] Shows Encryped Files Log in GUI Window
- [x] Timer Integrated With GUI Window
- [x] Extremely Fast and easy to use
- [x] **GUI DATABASE MANAGER** which can be used by hackers to automate database interactions.
- [x] C&C Website/Server With Database, to Stored **Decryption Key**, **Date**, **Payment** [**Boolean Type**] & **Unique ID** 
- [x] Function to Prohibit Encryption of Particular Directorys (**Directory Exclusion**)
- [ ] Function to Change Language of GUI Window to Different Available langauges  **(Coming Soon)** 
- [ ] Function to Disable Decryptor When Payment not made in Given Time **(Coming Soon)** 
- [ ] Creates Executable Binary With Zero Dependencies **(Coming Soon)**
- [ ] Create less size ~ 5mb payload with advance functionality  **(Coming Soon)**
- [ ] Ofusticate the Payload before Generating it, hence Bypassing few more antivirus **(Coming Soon)**
- [ ] Generated Payload is Encryted with base64, hence makes extremely difficult to reverse engineer the payload **(Coming Soon)**
- [ ] Function to Kill Antivirus on Victim PC and tries to disable the security  **(Coming Soon)**

## Prerequisite
- [x] Python 3.X , **Recommended 3.7**
- [x] Few External Modules like **pycryptodome**, **configparser**, **mysql-connector-python** etc.

## Tested On

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 8.1 - Pro**

## Order of Processes Which are taken

**MAIN.py is the Main File Which Do All Hard Work for You In Series**
**main.py** starts **THREE** stages i.e. **stage1**, **stage2**, **stage3**, and then atlast, starts the **GUI Window** which shows warning message.

**GUI Window** is capable to Call **Reverse_Attack** stager which takes **KEY** as argument.

**GUI Window** of Ransomeware is also capable to Show **Encrypted Files Log** In GUI Window.

## TREE to Show Role of Different Files

```
+====================+
+ Ransomeware_Files  +
+====================+
	+
	+===========+
	+  Main.py  +
	+===========+
	+	|____Run Stage1
	+	|____Run Stage2
	+	|____Run Stage3
	+	|____Change Wallpaer After Given IntervL
	+	|____Start GUI 
	+		|____Starts Timer
	+		|____Can Initiate Decrypt Function [Takes KEY As Argument]
	+		|____Can Show Encrypted Files Log
	+	
	+===========+
	+ Stage1.py +
	+===========+
	+	|____*****TAKES 4 Arguments, i.e. [server, username, password, db_name]*****
	+	|____Generates Unique Machine ID
	+	|____Generates Random Encryption Key With Fixed Length
	+	|____Export KEY to Command & Control Server
	+	|____*****RETURN : Encryption/Decryption KEY*****
	+
	+===========+
	+ Stage2.py +
	+===========+
	+	|____*****TAKES NO ARGUMENTS*****
	+	|____Searches for Target Extension Files on Different Thread
	+	|____*****RETURN : List of TARGET Files*****
	+
	+===========+
	+ Stage3.py +
	+===========+
	+	|____*****TAKES 2 ARGUMENTS, i.e. KEY & LIST of Sensitive Files*****
	+	|____Initiate Encryption Process
	+
	+===================+
	+ Reverse_Attack.py +
	+===================+
	+	|____*****TAKES 1 ARGUMENTS, i.e. KEY *****
	+	|____Initiate Decryption Process
	+	
	+=======================+
	+ After_Stage1 (Folder) +
	+=======================+
	+	|
	+	|    +====================+
	+	|____+ changeWallpaper.py +
	+	|    +====================+
	+	|____Images [Wallpaper] 
	+	
	+=======================+
	+ After_Stage2 (Folder) +
	+=======================+
		|
		|    +====================+
		|____+ check_log_gui.py +
		|    +====================+
		|
		|    +====================+
		|____+ decryptor_gui.py +
		|    +====================+
		|
		|    +========+
		|____+ GUI.py +
		|    +========+
		|
		|    +========================================+
		|____+ img [Folder Containing Resource Image] +
		     +========================================+	
 ```
 
## Attack/Stage Breakdown
 
Attack is Divided Into **3 Stages**, Stages are Completed By **Main** Program (main.py)

* In **Stage1**, (Unique MachineID & KEY) are generated and were exported to Remote Server.
* In **Stage2**, Locates Target Extension Files in Default Target Directory.
* In **Stage3**, KEY & List of TargetFiles (obtained from Stage1 & Stage2) are then used to launch Encryption.
* In **Finale Stage**, Main Program launches Ransomeware GUI demanding for Ransome. 

## Default Target Directory

```
+==========================+
+ Default Target Directory +
+==========================+
	|____C:\Users\USERNAME\Pictures
	|____C:\Users\USERNAME\Music
	|____C:\Users\USERNAME\Downloads
	|____C:\Users\USERNAME\Documents
	|____C:\Users\USERNAME\Desktop
```

## ScreenShots

#### Main GUI Window of NekRos Ransomeware
![](/images/nekros_ransomeware.PNG)

#### Check Encryped Files Log ~ GUI Window
![](/images/Check_LOG_Window.PNG)

#### Decryptor ~ GUI Window
![](/images/Decryptor.PNG)

#### Database Manager ~ For Attacker 
![](/images/db_manager.PNG)

#### Website Asking for Machine ID 
![](/images/website1.png)

#### Website showing Result
![](/images/website2.png)

## Usage 

* Upload Website Folder's Content to your server and update **get_decrypt_code.php** with right creds. present in **website/php/**
* Create Database and Import **nekros.sql** in it.
* Update **config.txt** present in **Ransomeware** folder.
* Update **config.txt** present in **db_manager** folder to Manage database using GUI Window.
* Install python and then install required modules using this command :

```
$ python -m pip install requirements.txt
```

* Run **main.py** like this

```
$ python main.py
```

## Decryption of Files

* Key is Exported to Server/Website before encryption process starts 
* Simply Acquire that key from Database throught website by Typing the Machine ID in website page **OR** Directly look for key in database.
* Paste that Key in GUI Window **OR** Direclty Run **reverse_attack.py** and paste the KEY in script
```
#Run reverse_attack.py like this
$ python reverse_attack.py
```

## Contribute

Currently this repo is maintained by me (Pushpender Singh).

Please Contribute this Project, and make this Project **THE BEST**, All pull request will be accepted if they were worthy fro this project : )


## Contact 
singhpushpender250@gmail.com 

## More Features Coming Soon...

