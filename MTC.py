import time
from colorama import Fore, Back
from colorama import Style
from colorama import init as colorama_init
import os
import sys
from time import sleep 
from itertools import cycle 
from datetime import datetime, timedelta
from alive_progress import alive_bar
from time import sleep
from itertools import cycle
from time import sleep
from PIL import Image
from playsound import playsound
import webbrowser
import keyboard as keyb
import psutil
import platform
from datetime import datetime
import shutil
from datetime import datetime, timedelta
from time import sleep 
from itertools import cycle
import sys
import threading
import itertools
import time 
from spinners import Spinners
from rich.console import Console









dcfpc = lambda: os.system('dir')
dcfan = lambda: os.system('ls')
clear = lambda: os.system('cls')
it = cycle([''] + ['\b \b'] * 3)
def pogbar():
    print('loading', end='')
    for i in range (13):
        sleep(.2)
        print(next(it),
              end='',
             flush=True)
    #print('\nTg @SpacePython')
def baro():
    for total in 700, 0, 700, 0:
         with alive_bar(total) as bar:
              for _ in range(700):
                   time.sleep(.001)
                   bar()

cpufreq = psutil.cpu_freq()




def lokan():
     print("Starting MTC OS 1.4 | MG Electron"), time.sleep(1)
     print("( OK ) Data and CFG-FILES"), time.sleep(1)
     print("Collecting data about CFG-FILES ")
     time.sleep(1)
     print("Loading command information and saved data...")
     time.sleep(0.20)
     print("( OK ) Updating resourses from Github..."), time.sleep(0.20)
     print("Cheking screen resolution ")
     time.sleep(1)
     print("Cheking screen resolution... Done!")
     print("Wellcome! to MTC OS 1.4!"), time.sleep(1)
     print("Downloading resourses...")
     time.sleep(2)
     print("Downloading resourses... Done!")
     print("collecting system information..."), time.sleep(0.10)
     print("Proccesor: " +Fore.YELLOW+ platform.processor()), time.sleep(0.10)
     print("Machine version: "+Fore.YELLOW+ platform.machine()),time.sleep(0.10)
     print("release date: "+Fore.YELLOW + platform.release()), time.sleep(0.10)
     print("node name: "+Fore.YELLOW+ platform.node()), time.sleep(0.50)
     print("system: "+Fore.YELLOW+ platform.system()), time.sleep(0.10)
     print("Maximum Cpu speed: "+Fore.YELLOW + str(psutil.cpu_freq(max)) + " Mhz"), time.sleep(0.70)
     print("Minimum Cpu speed: "+Fore.YELLOW+str(psutil.cpu_freq(min))+" Mhz"), time.sleep(0.10)
     print("Current Cpu speed: "+Fore.YELLOW+ str(psutil.cpu_freq()) +" Mhz"), time.sleep(0.40)
     print("system release: "+Fore.YELLOW+ platform.system() + platform.release()), time.sleep(0.10)
     print("win edition: "+Fore.YELLOW + platform.win32_edition()), time.sleep(1)
     print(Fore.CYAN+"=================================== MTC OS Succesfuly started! ==================================="), time.sleep(1)
     print(Fore.GREEN + "###########################################")
     print(Fore.GREEN + "#######*-::-=+*############*+=-::-+######## ")
     print(Fore.GREEN + "######*  :--.  .-+######+-.  .:--  *#######")
     print(Fore.GREEN + "######*  -####+-. .-++-. .-+*###=  *#######")
     print(Fore.GREEN + "#######=  *######*-    :*######*  -########"), time.sleep(0.10)
     print(Fore.GREEN + "########- .+####*=. ::  -*####*. :#########")
     print(Fore.GREEN + "#########=  =#*-  :*##*-  -*#=  -########## ")
     print(Fore.GREEN + "##########+. .. :*######*:  : .+########### ")
     print(Fore.GREEN + "###########+   :##########:   +############  ")
     print(Fore.GREEN + "##########=  -: .=######+. .-  =########### ")
     print(Fore.GREEN + "#########- .+##+. .=##+: .=##*. :*#########"), time.sleep(0.10)
     print(Fore.GREEN + "########: .*#####+: .. :+#####*. .*########")
     print(Fore.GREEN + "#######- .*#####*=:    .=*#####*. :########")
     print(Fore.GREEN + "######*  =###+=:  :=**=:  :-+*##+  *#######")
     print(Fore.GREEN + "######*. .:.  .-+*######*+:.  .:. .*#######")
     print(Fore.GREEN + "#######*+===+*##############*+====*########"), time.sleep(0.10)
     print(Fore.GREEN + "###########################################"), time.sleep(2)

     




keyb.add_hotkey('Ctrl + B', lambda: keyb)

#autoreset=True
colorama_init(autoreset=True)
def openn():
    print(Back.BLUE +"╔═════════════════════════════════════════╗"+ Back.BLACK)                           
    print(Back.BLUE + Fore.WHITE+"║ "+ Fore.LIGHTGREEN_EX +"Wellcome to MG-DOS 1.4 "+Fore.WHITE+"                 ║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ For a commands list you must type help  ║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ "+Fore.CYAN+"author mail - niktonianna@gmail.com  "+Fore.WHITE+"   ║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ "+ Fore.RED +"high "+ Fore.WHITE +"speed "+ Fore.YELLOW +"mini"+ Fore.WHITE +" operating system        ║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ author "+ Fore.RED +"Nikita Yonih"+ Fore.WHITE +"                     ║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ smart and easy! you need to find "+ Fore.LIGHTMAGENTA_EX +"README!"+ Fore.WHITE +"║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ "+ Fore.LIGHTGREEN_EX +"HAVE FUN!"+ Fore.WHITE +"                               ║"+ Back.BLACK)                    
    print(Back.BLUE + Fore.WHITE+"║ "+Fore.RED+"program to work correctly, "+Fore.LIGHTGREEN_EX +" Alt + Enter "+Fore.WHITE+"║"+ Back.BLACK)
    print(Back.BLUE + Fore.WHITE+"║ YT - mistikal_green                     ║"+ Back.BLACK)
    print(Back.BLUE +            "╚═════════════════════════════════════════╝"+ Back.BLACK)


lokan()
clear(), time.sleep(1)
openn()
def wiltru():
    while True:
        
        



        word = input("MG-DOS" + ">")
        if word == "help":
            print(f"{Fore.LIGHTGREEN_EX}╔════════════════════════════════════╗")
            print(f"{Fore.LIGHTGREEN_EX}║ help - see more commands           ║")
            print(f"{Fore.LIGHTGREEN_EX}║ dir - browse directories           ║")
            print(f"{Fore.LIGHTGREEN_EX}║ open - open 'folder' from dir      ║")
            print(f"{Fore.LIGHTGREEN_EX}║ write - write message              ║")
            print(f"{Fore.LIGHTGREEN_EX}║ read - read a txt file             ║")
            print(f"{Fore.LIGHTGREEN_EX}║ link, [link] - opens link          ║")
            print(f"{Fore.LIGHTGREEN_EX}║ clear - clear the console          ║")
            print(f"{Fore.LIGHTGREEN_EX}║ reboot - restarts the console      ║")
            print(f"{Fore.LIGHTGREEN_EX}║ image - open image and see data    ║")
            print(f"{Fore.LIGHTGREEN_EX}║ listen - listen to audio file      ║")
            print(f"{Fore.LIGHTGREEN_EX}║ create - create custom folder      ║")
            print(f"{Fore.LIGHTGREEN_EX}║ logo, ussr - bonus command         ║")
            print(f"{Fore.LIGHTGREEN_EX}║ cpustats - youre cpu statistics    ║")
            print(f"{Fore.LIGHTGREEN_EX}║ packlist - show pack list (demo)   ║")
            print(f"{Fore.LIGHTGREEN_EX}║ tree - file tree                   ║")
            print(f"{Fore.LIGHTGREEN_EX}║ calcinfo - calc operation info     ║")
            print(f"{Fore.LIGHTGREEN_EX}║ calc - calculator                  ║")
            print(f"{Fore.LIGHTGREEN_EX}║ dcfpc - dir current folder (pc)    ║")
            print(f"{Fore.LIGHTGREEN_EX}║ dcfan - dir current folder android ║")
            print(f"{Fore.LIGHTGREEN_EX}╚════════════════════════════════════╝")

        if word == "open":
                try:   
                    rec = input("directory or name >")
                    os.startfile(rec)
                    wiltru()
                except Exception:
                     print(Fore.RED+"Error: Not correct executable file or directory")
                     
        #if word == "rename":
            # reman1 = input("new name >")
           #  print(Fore.GREEN+"Name succesfuly changed!")
             
          #   reman1 = "User"
        if word == "cpustats":    
            print("Proccesor: " +Fore.YELLOW+ platform.processor()), time.sleep(0.10)
            print("Machine version: "+Fore.YELLOW+ platform.machine()),time.sleep(0.10)
            print("release date: "+Fore.YELLOW + platform.release()), time.sleep(0.10)
            print("node name: "+Fore.YELLOW+ platform.node()), time.sleep(0.50)
            print("system: "+Fore.YELLOW+ platform.system()), time.sleep(0.10)
            print("Maximum Cpu speed: "+Fore.YELLOW + str(psutil.cpu_freq(max)) + " Mhz"), time.sleep(0.70)
            print("Minimum Cpu speed: "+Fore.YELLOW+str(psutil.cpu_freq(min))+" Mhz"), time.sleep(0.10)
            print("Current Cpu speed: "+Fore.YELLOW+ str(psutil.cpu_freq()) +" Mhz"), time.sleep(0.40)
            print("system release: "+Fore.YELLOW+ platform.system() + platform.release()), time.sleep(0.10)
            print("win edition: "+Fore.YELLOW + platform.win32_edition()), time.sleep(1) 

        if word == "dcfpc":
             int(dcfpc())

        if word == "dcfan":
             int(dcfan())

        if word == "start":
             os.system("cmd")

             


        if word == "clear":
            clear()

 

        if word == "reboot":
            print("are you sure to reboot?")
            print(Fore.GREEN + "1) yes i sure")
            print(Fore.RED + "2) dont sure")
            asd = input("select option >")
            if asd == "1":
                clear()
                lokan()
                clear()
                openn()
            if asd == "2":
                pass

        
        if word == "write":
            pebr = input("write anything >")
            def prer():
                print(Fore.CYAN+"@Console.MG>" + pebr)
            prer()
        
        if word == "dir":
            dirctw=input("enter directory >")
            try:    
                    dcwfpc = lambda: os.system('dir ' + dirctw)
                    dcwfpc()
                    #lisat = os.listdir(dirctw)
                    #print (lisat)
            except Exception:
                     print(Fore.RED+"Error: Not correct directory or folder name")
            

            
            
            
            
             #print("1) all directories dir (too longest)")
             #print("2) easy dir (only all files)")
             #chuse = input("choose 1 or 2 >")
             #if chuse == "1":
                #for path, dirs, files in os.walk(dirct):
                   # print("the current folder is : " + path)
                  #  for dir in dirs:
                   #     print("Subfolder of : " + path + dir)
                  #  for file in files:
                    #    print("folder outside : " + " : " + path + file)
            #if chuse == "2":
                #lisat = os.listdir(dirct)
                #  print (lisat)
                  
        

        
        if word == "packlist":
            print("packages")
            print("|__"+Fore.CYAN+"scripts")
            print("|   |__"+Fore.CYAN+"main.dll")
            print("|__"+Fore.BLUE+"Sovietmode.dll")
            print("|__"+Fore.BLUE+"Mginput.dll")
            print("|__"+Fore.BLUE+"helpcommand.dll")
            #packs = lambda: os.system('dir packages')
            #def packs():
                #lisat = os.listdir('packages')
                #print (lisat)
                
        if word == "tree":
            try:
                dire= input("enter directory >")
                leara = lambda: os.system('tree ' + dire)
                leara()
            except Exception:
                print(Fore.RED+"Error: Not correct directory or folder name")
            # def hek():
           #    try:    
           #         packs()
           #     except Exception:
           #         print(Fore.RED + "Error: Packages Folder is missing..." + str(Exception))
           # hek()
        if word == "packinstall":
            pass


        if word == "calcinfo":
            print()
            print(Fore.CYAN+"--<Calc operation list>--")
            print(Fore.YELLOW+" |__  + = add")
            print(Fore.YELLOW+" |__  - = subtract")
            print(Fore.YELLOW+" |__  * = multiply")
            print(Fore.YELLOW+" |__  / = divide")
            print()


                
        if word == "calc":
            try:
                def calculate(n1,n2,op):
                    if op == '+':
                        result = n1+n2
                    elif op == '-':
                        result = n1-n2
                    elif op == '*':
                        result =  n1*n2
                    elif op == '/':
                        result = n1/n2
                    elif op=='**':
                        result =  n1**n2
                        
                    return result


                number1 = float(input(Fore.YELLOW +'Enter first number: '))
                op = input(Fore.YELLOW+'Enter operator (+,-,*,/,**): ')
                number2 = float(input(Fore.YELLOW+'Enter second number: '))
                result=calculate(number1,number2,op)
                res = number1,op,number2, "=", result
                print(res)
            except Exception:
                print(Fore.RED+"Error: Not correct operation or number")
            


        if word == "read":
            try:
                        fil = input("enter directory of txt file >")   
                        file = open(fil, 'r')
            except Exception:
                print(Fore.RED+"Error: Not correct directory or file type (need .txt)")

            
        if word == "image":
            try:    
                filename = input("type directory or filename >")
                img = Image.open(filename)
                print("1) open the image")
                print("2) see properties")
                choes = input("choose 1 or 2 >")
                if choes == "1":
                    img.show()
                if choes == "2":
                    print(img)
            except Exception:
                print(Fore.RED+"Error: Something went wrong...")

        if word == "listen":
             urals = input("name or directory of audio file >")
             def ply():
                playsound(urals)
             try:
                print(Fore.MAGENTA + "playing: " + urals)
                ply()
             except Exception:
                print(Fore.RED+"Error: Something went wrong...")


        if word == "create":
             pathh = input("directory and name>")

             try:
                  os.mkdir(pathh)
                  print("folder:" + pathh + " created!")
             except FileExistsError:
                  print("file already exists.")
             except Exception:
                print(Fore.RED+"Error: Something went wrong...")

        if word == "link":
            try:
                wbb = input("type link >")
                webbrowser.open_new(wbb)
            except Exception:
                print(Fore.RED+"Error: Not correct link")

        if word == "logo":
             print(Fore.RED + "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)
             print(Fore.RED + "█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██░░░░░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
             print(Fore.RED + "█░░░░░░██████████░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
             print(Fore.RED + "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)

             
        if word == "ussr":
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*****##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++--=+*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#++#%%%%%%%%%%%#*=--=+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----+#%%%%%%%%%%%#=---+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=---------+%%%%%%%%%%%%+----*%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+----------*%%%%%%%%%%%%%%%*----*%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----------#%%%%%%%%%%%%%%%%%+----#%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%*--------------+%%%%%%%%%%%%%%%%#-----%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-----=**=-----+%%%%%%%%%%%%%%%-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=+#%%%%*------+#%%%%%%%%%%%#-----*%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------+%%%%%%%%%%=-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+------+%%%%%%#=-----+%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+%%%%%%%%%%%+------+=------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------=+#%%%%%%%%#+-----------+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%*+=---+=------=++*****+---------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%#=-----+%%%%*=----------------------+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%#-----=#%%%%%%%%#*+=----------=+=----=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%+=+*#%%%%%%%%%%%%%%%%%####%%%%%%*==#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                  print( Fore.RED + f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)


                
        if word == "love":
             print(Fore.RED + "────────█████─────────────█████")
             print(Fore.RED + "────████████████───────████████████")
             print(Fore.RED + "──████▓▓▓▓▓▓▓▓▓▓██───███▓▓▓▓▓▓▓▓▓████")
             print(Fore.RED + "─███▓▓▓▓▓▓▓▓▓▓▓▓▓██─██▓▓▓▓▓▓▓▓▓▓▓▓▓███")
             print(Fore.RED + "███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███")
             print(Fore.RED + "██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██")
             print(Fore.RED + "██▓▓▓▓▓▓▓▓▓──────────────────▓▓▓▓▓▓▓▓██")
             print(Fore.RED + "██▓▓▓▓▓▓▓─██───████─█──█─█████─▓▓▓▓▓▓██")
             print(Fore.RED + "██▓▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██")
             print(Fore.RED + "███▓▓▓▓▓▓─██───█──█─█──█─█████─▓▓▓▓▓▓██")
             print(Fore.RED + "███▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██")
             print(Fore.RED + "─███▓▓▓▓▓─████─████─████─█████─▓▓▓▓███")
             print(Fore.RED + "───███▓▓▓▓▓──────────────────▓▓▓▓▓▓███")
             print(Fore.RED + "────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████")
             print(Fore.RED + "─────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████")
             print(Fore.RED + "───────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████")
             print(Fore.RED + "──────────████▓▓▓▓▓▓▓▓▓▓▓▓████")
             print(Fore.RED + "─────────────███▓▓▓▓▓▓▓████")
             print(Fore.RED + "───────────────███▓▓▓███")
             print(Fore.RED + "─────────────────██▓██")
             print(Fore.RED + "──────────────────███")


        if word == "love1":
                    print(Fore.WHITE + f"                    .-=+***++=-.                           :-++***++=-.     "), time.sleep(0.05)
                    print(Fore.WHITE + f"               :=*#%%%%%%%%%%%%%%#+-.                 .=*#%%%%%%%%%%%%%%#*-. "), time.sleep(0.05)
                    print(Fore.WHITE + f"            .+%%%%%%%%%%%%%%%%%%%%%%%#+.           -*%%%%%%%%%%%%%%%%%%%%%%%#=."), time.sleep(0.05)
                    print(Fore.WHITE + f"          -#%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-       -#%%%%%%%%%%%%%%%%%%%%%%%%%%%%*. "), time.sleep(0.05)
                    print(Fore.WHITE + f"       :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%: =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*"), time.sleep(0.05)
                    print(Fore.WHITE + f"      .#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*"), time.sleep(0.05)
                    print(Fore.WHITE + f"      #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%="), time.sleep(0.05)
                    print(Fore.WHITE + f"     :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#"), time.sleep(0.05)
                    print(Fore.WHITE + f"     =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.05)
                    print(Fore.WHITE + f"     +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."), time.sleep(0.05)
                    print(Fore.WHITE + f"     +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."), time.sleep(0.05)
                    print(Fore.WHITE + f"     =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."), time.sleep(0.05)
                    print(Fore.BLUE + f"     -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#"), time.sleep(0.05)
                    print(Fore.BLUE + f"     .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*"), time.sleep(0.05)
                    print(Fore.BLUE + f"      *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%-"), time.sleep(0.05)
                    print(Fore.BLUE + f"      .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.05)
                    print(Fore.BLUE + f"       +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:"), time.sleep(0.05)
                    print(Fore.BLUE + f"        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%="), time.sleep(0.05)
                    print(Fore.BLUE + f"         =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%="), time.sleep(0.05)
                    print(Fore.BLUE + f"          =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#."), time.sleep(0.05)
                    print(Fore.BLUE + f"           -*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*."), time.sleep(0.05)
                    print(Fore.BLUE + f"             -#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*."), time.sleep(0.05)
                    print(Fore.BLUE + f"               =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:"), time.sleep(0.05)
                    print(Fore.BLUE + f"                 -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#-"), time.sleep(0.05)
                    print(Fore.RED + f"                  .+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#-"), time.sleep(0.05)
                    print(Fore.RED + f"                     :*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+."), time.sleep(0.05)
                    print(Fore.RED + f"                       :*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%="), time.sleep(0.05)
                    print(Fore.RED + f"                          =%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:"), time.sleep(0.05)
                    print(Fore.RED + f"                           .-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-"), time.sleep(0.05)
                    print(Fore.RED + f"                              :*%%%%%%%%%%%%%%%%%%%%%%%%%%%+."), time.sleep(0.05)
                    print(Fore.RED + f"                                .=#%%%%%%%%%%%%%%%%%%%%%*="), time.sleep(0.05)
                    print(Fore.RED + f"                                   =%%%%%%%%%%%%%%%%%%%:"), time.sleep(0.05)
                    print(Fore.RED + f"                                     -#%%%%%%%%%%%%%*:"), time.sleep(0.05)
                    print(Fore.RED + f"                                       :*%%%%%%%%%+."), time.sleep(0.05)
                    print(Fore.RED + f"                                          +%%%%#-"), time.sleep(0.05)
                    print(Fore.RED + f"                                            *%="), time.sleep(0.05)

                                      
                                                                  






        if word == "quit":
             break
        else:
            wiltru()


wiltru()























