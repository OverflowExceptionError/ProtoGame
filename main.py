# IDK new game project i'm working on
# VuLVE Software
import obscure_text, hashlib
import colorama, os, time, pygame
colorama.init()
from colorama import Fore, Back, Style
os.system("cls")
print(Fore.GREEN)
#Startup message
print("Hello.")
print("If you are not a fan of ARGs or similar types of games, this is not the game for you.")
print("By pressing ENTER, you will start the game. Are you ready?")
input(">>> ")
print("Starting system...")
os.system("cls")
# System startup
print("American Megatrade(TEEM)")
print("(C) 2002 Outtell")
print("powered by OUTELL(tm) OUTSIDE")
print("Beginning memory scan...")
time.sleep(0.3)
print("1G Memory fully functional.")
time.sleep(0.02)
print("Scanning for drives...")
time.sleep(0.1)
print("WD40 29rFgGB drive, sectors ???")
time.sleep(0.04)
print("EJAD 21D4 model drive, sectors 1959")
time.sleep(0.04)
print("SONE CD-ROM drive, no sectors")
time.sleep(0.04)
print("Starting boot selection menu, multiple bootable drives detected.")
time.sleep(1)
os.system("cls")
# A r e y o u h a v i n g f u n y e t
print("Hello again.")
time.sleep(0.3)
print("How have you enjoyed your experience?")
time.sleep(0.3)
print(obscure_text.T_C0 + "?")
time.sleep(0.3)
os.system("cls")
#Boot selection menu
print("Options:")
print("1. WD40 29rFgGB")
print("2. EJAD 21D4 model")
a = input(" BIOS > ")
shagen = hashlib.sha256()
def terminal_adults():
    pass
def terminal_kids():
    pass
if a == "1":
    #WD40
    os.system("cls")
    print(Fore.WHITE)
    print("Starting SFSROS")
    try:
        os.mkdir("filesys_sfsr")
        os.mkdir("filesys_sfsr/sfsr")
        os.mkdir("filesys_sfsr/users")
        os.mkdir("filesys_sfsr/users/admin")
        os.mkdir("filesys_sfsr/users/guest")
        os.mkdir("filesys_sfsr/users/kids")
        os.mkdir("filesys_sfsr/users/admin/documents")
        os.mkdir("filesys_sfsr/users/admin/downloads")
        os.mkdir("filesys_sfsr/users/guest/documents")
        os.mkdir("filesys_sfsr/users/kids/documents")
        os.mkdir("filesys_sfsr/users/guest/downloads")
        os.mkdir("filesys_sfsr/users/kids/downloads")
        f = open("filesys_sfsr/users/guest/documents/Welcome.txt","w")
        f.write(obscure_text.gu_we)
        f.close()
        f = open("filesys_sfsr/Note for Jacob.txt","w")
        f.write(obscure_text.root_message)
        f.close()
    except OSError:
        pass
    print("System for Stupid Reasons")
    time.sleep(2)
    print("Sign in or use guest account.")
    print("Options:")
    print("1. Admin")
    print("2. Kids")
    print("3. Guest")
    a = input(" > ")
    if a == "1":
        pass # Call admin prompt/login
    if a == "2":
        pass # Call kids prompt/login
    if a == "3":
        print("Hello, Guest.")
        print("Type a command.")
        running = True
        directory = "/users/guest"
        print("Type 'help' to see all commands.")
        while running:
            a = input(directory + " > ").split(" ")
            if a[0] == "gensha256":
                print("Administrators only command.")
                shagen = hashlib.sha256()
                shagen.update(bytes(a[1]))
                print(shagen.hexdigest())
if a == "2":
    pass # Call secondary drive