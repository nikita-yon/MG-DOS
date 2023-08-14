from ast import Try
import time
from colorama import Fore, Back
from colorama import Style
from colorama import init as colorama_init
import os
import sys
import wmi
import atexit
from configparser import ConfigParser
from time import sleep 
from itertools import cycle 
import datetime as dt
from datetime import datetime, timedelta
from alive_progress import alive_bar
from time import sleep
from itertools import cycle
from time import sleep
from PIL import Image
from subprocess import call
from playsound import playsound
import webbrowser
import keyboard as keyb
import operator
import psutil
import random
import platform
import re
from datetime import datetime
from deep_translator import GoogleTranslator
import shutil
from datetime import datetime, timedelta
from time import sleep 
from itertools import cycle
import sys
import msvcrt
import subprocess
import winsound
import threading
import itertools
import time 
from pytimedinput import timedInput
from random import randint
import os
from colorama import Fore, init

import random

config = ConfigParser()


clear = lambda: os.system("cls")







def one():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Collecting data about CFG-FILES... ", i,end='\r') 
        sleep(0.1)

def two():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Loading command information and saved data... ", i,end='\r') 
        sleep(0.2)

def tre():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("Updating resourses from Github... ", i,end='\r') 
        sleep(0.2)

def chet():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Cheking screen resolution... ", i,end='\r') 
        sleep(0.1)

def pat():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("calculating... ", i,end='\r') 
        sleep(0.1)

def shest():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=4):
            break
        print("Downloading resourses... ", i,end='\r') 
        sleep(0.4)

def sem():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("calculating... ", i,end='\r') 
        sleep(0.2)

def translate():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("translating... ", i,end='\r') 
        sleep(0.2)

def enc():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("encrypting... ", i,end='\r') 
        sleep(0.2)
def dec():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("decrypting... ", i,end='\r') 
        sleep(0.2)


def vom():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("collecting system information... ", i,end='\r') 
        sleep(0.2)

def format_size(size_in_bytes):
    # Function to format size from bytes to a human-readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            break
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} {unit}"

def format_size(size_in_bytes):
    # Функция для форматирования размера из байтов в человеко-читаемый формат
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            break
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} {unit}"

def list_directory(path="."):
    # Функция для вывода содержимого директории в формате, аналогичном выводу команды "dir" в Windows
    print("{:<19} {:<15} {:<12} {:>20} {}".format("Date", "Time", "Type", "Size", "FileName"))
    print("=" * 80)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        item_stat = os.stat(item_path)
        mod_time = dt.datetime.fromtimestamp(item_stat.st_mtime)
        if os.path.isdir(item_path):
            type_str = "<DIR>"
            size_str = ""
        else:
            type_str = ""
            size_str = format_size(item_stat.st_size)
        print("{:<19} {:<15} {:<12} {:>20} {}".format(
            mod_time.strftime("%d.%m.%Y"),
            mod_time.strftime("%H:%M"),
            type_str,
            size_str,
            item
        ))

    total_size = sum(os.stat(os.path.join(path, item)).st_size for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)))
    print("=" * 80)
    print("{:>31} files {:>36}".format(len(os.listdir(path)), format_size(total_size)))

def run(file_path):
    
        subprocess.run(file_path, shell=True)


def YorN():
    key = msvcrt.getch().decode("utf-8")
    if key == "y":
        pass

def KBSTART():

    print("0001")
    time.sleep(0.1)
    clear = lambda: os.system("cls")
    clear()
    print("00001 KB OK")
    time.sleep(0.1)
    clear()
    print("00002 KB OK")
    time.sleep(0.1)
    clear()
    print("00004 KB OK")
    time.sleep(0.1)
    clear()
    print("00011 KB OK")
    time.sleep(0.1)
    clear()
    print("00014 KB OK")
    time.sleep(0.1)
    clear()
    print("00019 KB OK")
    time.sleep(0.1)
    clear()
    print("00020 KB OK")
    time.sleep(0.1)
    clear()
    print("00021 KB OK")
    time.sleep(0.1)
    clear()
    print("00023 KB OK")
    time.sleep(0.1)
    clear()
    print("00025 KB OK")
    time.sleep(0.05)
    clear()
    print("00027 KB OK")
    time.sleep(0.05)
    clear()
    print("00029 KB OK")
    time.sleep(0.05)
    clear()
    print("00030 KB OK")
    time.sleep(0.05)
    clear()
    print("00039 KB OK")
    time.sleep(0.05)
    clear()
    print("00059 KB OK")
    time.sleep(0.05)
    clear()
    print("00062 KB OK")
    time.sleep(0.05)
    clear()
    print("00065 KB OK")
    time.sleep(0.05)
    clear()
    print("00080 KB OK")
    time.sleep(0.05)
    clear()
    print("00089 KB OK")
    time.sleep(0.05)
    clear()
    print("00092 KB OK")
    time.sleep(0.05)
    clear()
    print("00102 KB OK")
    time.sleep(0.05)
    clear()
    print("00112 KB OK")
    time.sleep(0.05)
    clear()
    print("00129 KB OK")
    time.sleep(0.05)
    clear()
    print("00131 KB OK")
    time.sleep(0.05)
    clear()
    print("00139 KB OK")
    time.sleep(0.05)
    clear()
    print("00142 KB OK")
    time.sleep(0.05)
    clear()
    print("00146 KB OK")
    time.sleep(0.05)
    clear()
    print("00162 KB OK")
    time.sleep(0.05)
    clear()
    print("00170 KB OK")
    time.sleep(0.05)
    clear()
    print("00182 KB OK")
    time.sleep(0.05)
    clear()
    print("00193 KB OK")
    time.sleep(0.05)
    clear()
    print("00199 KB OK")
    time.sleep(0.05)
    clear()
    print("00214 KB OK")
    time.sleep(0.05)
    clear()
    print("00219 KB OK")
    time.sleep(0.05)
    clear()
    print("00224 KB OK")
    time.sleep(0.05)
    clear()
    print("00229 KB OK")
    time.sleep(0.05)
    clear()
    print("00311 KB OK")
    time.sleep(0.05)
    clear()
    print("00322 KB OK")
    time.sleep(0.05)
    clear()
    print("00328 KB OK")
    time.sleep(0.05)
    clear()
    print("00329 KB OK")
    time.sleep(0.05)
    clear()
    print("00331 KB OK")
    time.sleep(0.05)
    clear()
    print("00342 KB OK")
    time.sleep(0.05)
    clear()
    print("00354 KB OK")
    time.sleep(0.05)
    clear()
    print("00363 KB OK")
    time.sleep(0.05)
    clear()
    print("00372 KB OK")
    time.sleep(0.05)
    clear()
    print("00385 KB OK")
    time.sleep(0.05)
    clear()
    print("00390 KB OK")
    time.sleep(0.05)
    clear()
    print("00395 KB OK")
    time.sleep(0.05)
    clear()
    print("00412 KB OK")
    time.sleep(0.05)
    clear()
    print("00419 KB OK")
    time.sleep(0.05)
    clear()
    print("00421 KB OK")
    time.sleep(0.05)
    clear()
    print("00427 KB OK")
    time.sleep(0.05)
    clear()
    print("00430 KB OK")
    time.sleep(0.05)
    clear()
    print("00438 KB OK")
    time.sleep(0.05)
    clear()
    print("00443 KB OK")
    time.sleep(0.05)
    clear()
    print("00445 KB OK")
    time.sleep(0.05)
    clear()
    print("00451 KB OK")
    time.sleep(0.05)
    clear()
    print("00458 KB OK")
    time.sleep(0.05)
    clear()
    print("00460 KB OK")
    time.sleep(0.05)
    clear()
    print("00465 KB OK")
    time.sleep(0.05)
    clear()
    print("00471 KB OK")
    time.sleep(0.05)
    clear()
    print("00476 KB OK")
    time.sleep(0.05)
    clear()
    print("00480 KB OK")
    time.sleep(0.05)
    clear()
    print("00484 KB OK")
    time.sleep(0.05)
    clear()
    print("00489 KB OK")
    time.sleep(0.05)
    clear()
    print("00494 KB OK")
    time.sleep(0.05)
    clear()
    print("00499 KB OK")
    time.sleep(0.05)
    clear()
    print("00501 KB OK")
    time.sleep(0.05)
    clear()
    print("00510 KB OK")
    time.sleep(0.05)
    clear()
    print("00515 KB OK")
    time.sleep(0.05)
    clear()
    print("00519 KB OK")
    time.sleep(0.05)
    clear()
    print("00529 KB OK")
    time.sleep(0.05)
    clear()
    print("00534 KB OK")
    time.sleep(0.05)
    clear()
    print("00539 KB OK")
    time.sleep(0.05)
    clear()
    print("00541 KB OK")
    time.sleep(0.05)
    clear()
    print("00546 KB OK")
    time.sleep(0.05)
    clear()
    print("00549 KB OK")
    time.sleep(0.05)
    clear()
    print("00551 KB OK")
    time.sleep(0.05)
    clear()
    print("00553 KB OK")
    time.sleep(0.05)
    clear()
    print("00559 KB OK")
    time.sleep(0.05)
    clear()
    print("00563 KB OK")
    time.sleep(0.05)
    clear()
    print("00568 KB OK")
    time.sleep(0.05)
    clear()
    print("00570 KB OK")
    time.sleep(0.05)
    clear()
    print("00573 KB OK")
    time.sleep(0.05)
    clear()
    print("00579 KB OK")
    time.sleep(0.05)

    clear()
    print("00583 KB OK")
    time.sleep(0.05)
    clear()
    print("00586 KB OK")
    time.sleep(0.05)
    clear()
    print("00587 KB OK")
    time.sleep(0.05)
    clear()
    print("00590 KB OK")
    time.sleep(0.05)
    clear()
    print("00594 KB OK")
    time.sleep(0.05)
    clear()
    print("00599 KB OK")
    time.sleep(0.05)
    clear()
    print("00605 KB OK")
    time.sleep(0.05)
    clear()
    print("00614 KB OK")
    time.sleep(0.05)

def logo():

    print("  __  __  _____        _____   ____   _____ ")
    print(" |  \/  |/ ____|      |  __ \ / __ \ / ____|")
    print(" | \  / | |  __ ______| |  | | |  | | (___  ")
    print(" | |\/| | | |_ |______| |  | | |  | |\___ \ ")
    print(" | |  | | |__| |      | |__| | |__| |____) |")
    print(" |_|  |_|\_____|      |_____/ \____/|_____/ ")

    #print("╭━╮╭━┳━━━╮ ╭━━━┳━━━┳━━━╮")
    #print("┃┃╰╯┃┃╭━╮┃ ╰╮╭╮┃╭━╮┃╭━╮┃")
    #print("┃╭╮╭╮┃┃ ╰╯  ┃┃┃┃┃ ┃┃╰━━╮")
    #print("┃┃┃┃┃┃┃╭━┳━━┫┃┃┃┃ ┃┣━━╮┃")
    #print("┃┃┃┃┃┃╰┻━┣━┳╯╰╯┃╰━╯┃╰━╯┃")
    #print("╰╯╰╯╰┻━━━╯ ╰━━━┻━━━┻━━━╯")


MGDOSVER = "1.5"

def openn1():                          
        print(f"MG-DOS Version {MGDOSVER}")
        print("(c) Mistikal Green studio (MG Electron Corporation). All rights reserved.")
        print("Type 'help' to more commands.")
        print()









#ssssssSSssssssssssssssssssssS2222222225sssss
#ss5333333sssssssssssssssssi33          3Ssss
#S32     .3issssssssssssiS3X             23Ss
#Xr        XSssssssssssiXX                 35
#XSi       :2sssssssssiX      33XXXXX      .X
#i333,     ,2ssssssssi3     33  ,XsssX3     X
#sss2,      X5ssssssS3    333   ,Xssss2X    X
#sssX,      25ssssssX    33     ,XssssiX    X
#sssX,       XSssss53   23      ,XssssiX    X
#sssX,       XSsss53    2       ,Xssssi3    X
#sssX,       55iss5    33       ,XsssssSX  32
#sssX,        3isiX    3        ,XssssssS555s
#sssX,        XisS2   33        ,Xsssssssssss
#sssX,         3sS    3         ,Xsssssssssss
#sssX,  ;,     3i3   33  .      35sssssssssss
#sssX,  ;,     X2X   3   X,     3ssssssssssss
#sssX,  ;3.    .3X  33   X,     3ssssssssssss
#sssX,  ;33     ;X; 3   X3,     3ssssssssssss
#sssX,  ;33     ,XX3    33,    333333333333ss
#ss5X   ;33.     33X   X33,   3,..........X3s
#ss52   ;23X     2X   ,333,  3             3s
#ss52   ;5s3     .5   3sr3,   3,.....      3s
#ss52   ;is33         3 r3,    333333      3s
#ss52   ;isi3        3.  X,     3sssX      3s
#ss52   risi3       3s   X,     3sssX      3s
#sS3    Ssss33      3     3     3sssX      3s
#sSX    SsssS3      3     .X    35ssX      3s
#sSX    Ssssi3.     33     .X.  23XSX      3s
#i3     Sssss33    3is3      .3333333      3s
#iX     Sssss53    3isi3                  23s
#25    Xssssss3,  3Ssssi33               53ss
#SX5,,2Xssssssi3 32issssii33          ,X33iss
#sS333XssssssssX32sssssssssi3333333333Xssssss



def br(content=1):
    for i in range(content):
        print()


def lokan1():
    clear()
    for i in range(150):
        print("| MG | MG | CF | G | MG | MG | MG | MG | MG | MG | ME | MO | RY | MG | MG | MG | HE | MG | MG | MG |")
    print(i,)
    clear()
    sleep(0.5)
    KBSTART()
    clear()
    sleep(0.8)
    print("Starting MG-DOS...")
    br(4)
    logo()
    sleep(1.5)
    clear()


het = str(platform.system())



def lokanmg():
    os.system("title MG-DOS-1.4_08")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii55iiiiiiiiiiiiiiiiiiii5XXXXXXXXX2iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2999999iiiiiiiiiiiiiiiiiS99          95iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii59X...  ,9SiiiiiiiiiiiiS593             X95iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiii23s        35iiiiiiiiiiS33                 92iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiii535S.      ;XiiiiiiiiiS3      9933333      ,3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiS999:     :XiiiiiiiiS9     99  :3iii39    .3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiX:      32iiiiii59    999   :3iiiiX3    3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:      X2iiiiii3    99     :3iiiiS3    3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:       35iiii29   X9      :3iiiiS3    3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:       35iii29    X       :3iiiiS9    3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:       22Sii2    99       :3iiiii53  9Xiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:        9SiS3    9        :3iiiiii5222iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:        3Si5X   99        :3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:        .9i5    9         :3iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:  r:     9S9   99  ,      92iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:  r:     3X3   9   3:    .9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:  r9,    ,93  99   3:    .9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:  r99     r3r 9   39:    .9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii3:  r99.    :339    99:    999999999999iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii23   r99,     993   399:   9:,,,,,,,,,,39iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2X   rX93     X3   :999:  9             9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2X   r2i9     ,2   9is9:   9:,,,,,      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2X   rSi99         9 s9:    999999      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2X   rSiS9        9,  3:    .9iii3      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii2X   sSiS9       9i   3:    .9iii3      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii59    5iii99      9.    9    .9iii3      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii53    5iii59      9     ,3    92ii3      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii53    5iiiS9,    .99     ,3,  X9353      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiS9     5iiii99    9Si9      ,9999999      9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiS3     5iiii29    9SiS9                  X9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiX2    3iiiiii9:  95iiiS99               29iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii532::X3iiiiiiS9.9XSiiiiSS99.         :399Siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii59993iiiiiiii39XiiiiiiiiiS99999999993iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii9999iiiiiiiiiiiiiiiiiii999iiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii99999999999999iiiiiiiiiiiiiiii999    999iiiiiiiiiiiii999   999iiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiii999              99iiiiiiiiiiiii9          99iiiiiiiiii9         9iiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiii9                   99iiiiiiiiii9             9iiiiiiii9   9999    9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiii999      9999        9iiiiiiii9    99999      9iiiiii9  99iiii9   9iiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiii9     9iii999     9iiiiiii9    9iiiii99     9iiii9  9iiiiiii9  9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiii9    99iiiii9    9iiiiiiii9    9iii9   9iiiiiii9  9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiii9    9iiiii9   9iiiiiiiii9     9ii9   9iiiiiii9  9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiii9    9iii9    9iiiiiiiiii9    9ii9   9iiiiiiii99iiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiii9    9ii9     9iiiiiiiiii9    9ii9   9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9ii9    9iiiiiiiiiii9     9i9   9iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9ii9    9iiiiiiiiiii9     9i9    99iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9    9i9    9iiiiiiiiiii9     9ii9     9iiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9    9i9    9iiiiiiiiiii9     9ii9      99iiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9    9i9    9iiiiiiiiiiii9    9iii99      99iiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9    99     9iiiiiiiiiiii9    9iiiii9       9iiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9i9     9iiiiiiiiiiii9    9iiiiii9       9iiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9i9     9iiiiiiiiiii9     9iiiiiii99      9iiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9ii9    9iiiiiiiiiii9     9iiiiiiiii99     9iiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9   9ii9    9iiiiiiiiiii9    9iiiiiiiiiiii9    9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiiii9  9iii9    9iiiiiiiiiii9    9iiiiiiiiiiiii9   9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiii9   9iii9     9iiiiiiiiii9    9iii9iiiiiiiii9   9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiiii9   9iii9     9iiiiiiiiii9   9iii9 9iiiiiiiii9  9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiiii9   9iiiii9    9iiiiiiiii9    9iii9 9iiiiiiiii9  9iiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    9iiiiiii99   9iiiii9     9iiiiiiii9   9iii9  9iiiiiiii9   9iiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    print("iiiiiiiiiiiiiiiiiiii9    9iiiii99    9iiiiiii9     9iiiiii9    9iii9  9iiiiiiii9  9iiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9    999999     9iiiiiiiii9     999999    9iiii9   9iiiiii9   9iiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9              9iiiiiiiiiii9             9iiiii9    999999   9iiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiii9            99iiiiiiiiiiiii9          99iiiiiii9          99iiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiS99999    999iiiiiiiiiiiiiiii999    999iiiiiiiiii999    999iiiiiiiiiiiiiiiiiiiiiiiiiii")
    print("iiiiiiiiiiiiiiiiiiiiiiiiii9999iiiiiiiiiiiiiiiiiiiiii9999iiiiiiiiiiiiiiii9999iiiiiiiiiiiiiiiiiiiiiiiiiiiiii"),sleep(0.21)
    sleep(4)
    clear()
    sleep(1)
    KBSTART()
    clear()
    sleep(1)
    print("Starting MG-DOS...")
    sleep(3)
    clear()
    
def sort_files(extension):
    # Set the directory to search
    directory = os.path.join(os.path.expanduser("~"), "Desktop")

    # Find the files with the specified extension
    files = [f for f in os.listdir(directory) if f.endswith("." + extension)]

    # Print the results
    print(f"{len(files)} {extension} files found in {os.path.basename(directory)}:")
    print()
    for file in files:
        print(file)



def allcommand():
    lokan1()
    clear(), time.sleep(1)
    openn1()
    def wiltru():
        history = []
        while True:
            
            



            word = input(f"{os.getcwd()}>").lower()
            history.append(word)


            if word == "help":
                print()
                print(f"to check a specific command type HELP <command name>")
                print(f"write [filename] '[content]'       write to txt file              ")
                print(f"clear, cls                       clear the console          ")
                print(f"reboot                           restarts MG-DOS      ")
                print(f"cipher                           decrypt & encrypt any text")                          
                print(f"calc                             calculator                  ")
                print(f"compare                          compare two numbers      ")          
                print(f"listen [filename.extension]      listen to audio file      ")
                print(f"sort [extension]                 see how many txt, ico and... files    ")
                print(f"read [filename.extension]        read files file             ")
                print(f"open                             open 'folder' from dir      ")
                print(f"tree [directory]                 file tree                   ")
                print(f"dir  [directory]                 browse directories           ")
                print(f"dirc                             dir current folder (pc)    ")
                print(f"volume                           shows list of available volumes")
                print(f"rename [old-name] '[new-name]'   rename any file or folder")
                print(f"mkdir [filename]                 make folder    ")
                print(f"mktxt [filename.extension]       make any extension file    ")
                print(f"run [filename.extension]         run script files")
                print(f"delete [any files]               delete any type of files")
                print(f"cd [directory]                   delete any type of files")
                print(f"pause                            pauses MG-DOS")
                print(f"exit                             exit MG-DOS")
                print(f"save                             saves MG-DOS command history")

            
            def press_any_key():
                print("Press any key to continue . . .")
                msvcrt.getch()
                print()

            per = "\ n"

            if word == "break":
                exit()

            try:    
                regex = "help ([\s\S]+)"
                if match := re.match(regex, word):
                    xtx = match.groups()[0]
                    if xtx == "help":
                        print("usage: help [command] 'see command usage'")
                    if xtx == "write":
                        print(f"usage: write [filename.extension] '[content]' 'write to file ;WARNING>write content in quotes;'")
                    if xtx == "clear":
                        print("usage: clear or cls 'to clear the console'")
                    if xtx == "reboot":
                        print("usage: reboot 'restart MG-DOS'")
                    if xtx == "cipher":
                        print("usage: cipher 'encrypt / decrypt any text or message'")
                    if xtx == "calc":
                        print("usage: calc 'calculate any numbers (1 + 1 = 2)'")
                    if xtx == "campare":
                        print("usage: compare 'compare any numbers (1 < 2)'")
                    if xtx == "listen":
                        print("usage: listen [filename.extension] 'listen to audio files like mp3, wav'")
                    if xtx == "sort":
                        print("usage: sort [extension] 'see how many [extension] files is in current folder'")
                    if xtx == "read":
                        print("usage: read [filename.extension] 'read any files like txt, py'")
                    if xtx == "tree":
                        print("usage: tree [directory] 'make file system tree'")
                    if xtx == "dir":
                        print("usage: dir [directory] 'browse directory'")
                    if xtx == "dirc":
                        print("usage: dirc 'dir current folder'")
                    if xtx == "mkdir":
                        print("usage: mkdir [filename] 'make folder'")
                    if xtx == "mktxt":
                        print("usage: mktxt [filename.extension] 'make any text file like txt, py'")
                    if xtx == "run":
                        print("usage: run [[filename.extension]] 'run any script file like py, html, svelte'")
                    if xtx == "delete":
                        print("usage: delete [filename] 'delete any file'")
                    if xtx == "cd":
                        print("usage: cd [directory] 'change directory'")
                    if xtx == "pause":
                        print("usage: pause 'pauses all process'")
                    if xtx == "rename":
                        print("usage: rename [old-name] '[new-name]' 'rename folder or file ;WARNING>write a new name in quotes;'")
                    if xtx == "volume":
                        print("usage: volume 'shows list of available connected devices like - volumes, USB, SSD, CD-ROM, DVD, HARD-DRIVE'")
            except:
                print("Error: Something went wrong")
                        
            #if word == "rename":
                # reman1 = input("new name >")
            #  print(Fore.GREEN+"Name succesfuly changed!")



            #   reman1 = "User"
            #if word == "cpustats":    
             #   print("Proccesor: ") + platform.processor(), time.sleep(0.10)
            #    print("Machine version: "+Fore.YELLOW+ platform.machine()),time.sleep(0.10)
            #    print("release date: "+Fore.YELLOW + platform.release()), time.sleep(0.10)
            #    print("node name: "+Fore.YELLOW+ platform.node()), time.sleep(0.50)
            #    print("system: "+Fore.YELLOW+ platform.system()), time.sleep(0.10)
            #    print("Maximum Cpu speed: "+Fore.YELLOW + str(psutil.cpu_freq(max)) + " Mhz"), time.sleep(0.70)
            #    print("Minimum Cpu speed: "+Fore.YELLOW+str(psutil.cpu_freq(min))+" Mhz"), time.sleep(0.10)
            #    print("Current Cpu speed: "+Fore.YELLOW+ str(psutil.cpu_freq()) +" Mhz"), time.sleep(0.40)
            #    print("system release: "+Fore.YELLOW+ platform.system() + platform.release()), time.sleep(0.10)
            #    print("win edition: "+Fore.YELLOW + platform.win32_edition()), time.sleep(1) 

            if word == "dirc":
                list_directory()




                                
            if word == "ver":
                print(f"MG-DOS {MGDOSVER} Original Edition")
            if word == "version":
                print(f"MG-DOS {MGDOSVER} Original Edition")





            if word == "timer":
                
                    print("are you sure to set a timer?")
                    ged = input("No(N) or Yes(Y)>")
                    if ged == "y":
                        try:
                            tim = int(input("seconds>"))
                            
                            def dev():
                                start = datetime.now()
                                for i in cycle(["[♪♪♪      ] |", "[ ♪♪♪     ] /", "[  ♪♪♪    ] -", "[   ♪♪♪   ] \\", "[    ♪♪♪  ] |", "[     ♪♪♪ ] /", "[      ♪♪♪] -", "[     ♪♪♪ ] \\", "[    ♪♪♪  ] |", "[   ♪♪♪   ] /", "[  ♪♪♪    ] -", "[ ♪♪♪     ] \\"]):
                                    if datetime.now() > start + timedelta(seconds=int(tim)):
                                        break
                                    print(""+ ""+i,end='\r') 
                                    sleep(0.1)  
                            
                            dev()
                            print("")
                            
                            playsound('sound.mp3')
                        except Exception:
                            print("Error: Incorrect time! / Alarm file not found!")
                    else:
                        pass
                

            if word == "cipher":

                try:    
                    alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                    print("1) decrypt message!")
                    print("2) encrypt message!")
                    vibor = input("choose>")
                    if vibor == "1":

                        smeshenie = int(input('encryption step: '))
                        message = input("Message to decrypt: ").upper()
                        itog = ''
                        lang = input('choose language RU/EU: ')
                        if lang == 'RU':
                            for i in message:
                                mesto = alfavit_RU.find(i)
                                new_mesto = mesto - smeshenie
                                if i in alfavit_RU:
                                    itog += alfavit_RU[new_mesto]
                                else:
                                    itog += i
                        else:
                            for i in message:
                                mesto = alfavit_EU.find(i)
                                new_mesto = mesto - smeshenie
                                if i in alfavit_EU:
                                    itog += alfavit_EU[new_mesto]
                                else:
                                    itog += i
                        dec()
                        print("")
                        print (itog)
                    if vibor == "2":
                        smeshenie = int(input('encryption step: '))
                        message = input("Message to encrypt: ").upper()
                        itog = ''
                        lang = input('choose language RU/EU: ')
                        if lang == 'RU':
                            for i in message:
                                mesto = alfavit_RU.find(i)
                                new_mesto = mesto + smeshenie
                                if i in alfavit_RU:
                                    itog += alfavit_RU[new_mesto]
                                else:
                                    itog += i
                        else:
                            for i in message:
                                mesto = alfavit_EU.find(i)
                                new_mesto = mesto + smeshenie
                                if i in alfavit_EU:
                                    itog += alfavit_EU[new_mesto]
                                else:
                                    itog += i
                        enc()
                        print("")
                        print (itog)
                except Exception:
                        print("Error: Something went wrong...")
                



            if word == "cls":
                clear()
                openn1()
            if word == "clear":
                clear()
                openn1()

            if word == "dossier":
                print("Create a new dossier file?")
                print("|__1 - yes create")
                print("|__2 - cancel")
                aj = input("choose>")
                if aj == "1":
                    name = input("name>")
                    familie = input("family name>")
                    birthdate = input("birth date>")
                    obrazov = input("education>")
                    number = input("phone number>")
                    county = input("Residence Country>")
                    country = input("Birth Country>")
                    laung = input("Languages>")
                    code = input("code sign>")
                    se = input("gender>")
                    zodiak = input("Zodiac Sign>")
                    mom = input("Mom info (name, phone number, birth date, birth country)>")
                    Dad = input("dad info (name, phone number, birth date, birth country)>")
                    other = input("other family info (brothers name/sisters name, phone number, birth date, birth country)>")
                    fileman = input("filename>")
                    filname = fileman + '.txt'
                    os.system("echo dossier to "+ name + familie +" > "+filname+"")
                    
                    file = open(filname, 'w', encoding=enc)
                    file.write("name - "+name+"\n")
                    file.write("family name - "+familie+"\n")
                    file.write("birth date - "+birthdate+"\n")
                    file.write("education - "+obrazov+"\n")
                    file.write("phone number - "+number+"\n")
                    file.write("Residence country - "+county+"\n")
                    file.write("Birth country - "+country+"\n")
                    file.write("Languages - "+laung+"\n")
                    file.write("code sign - "+code+"\n")
                    file.write("gender - "+se+"\n")
                    file.write("Zodiac Sign - "+ zodiak +"\n")
                    file.write("Mom info (name, phone number, birth date, birth country - "+mom+"\n")
                    file.write("dad info (name, phone number, birth date, birth country - "+Dad+"\n")
                    file.write("other family info (brothers name/sisters name, phone number, birth date, birth country - "+other+"\n")
                    file.write("Dossier+ 1.0 by nikita!")
                else:
                    pass

            if word == "reboot":
                print("are you sure to reboot?")
                asd = input("No[N] or Yes[Y]>")
                if asd == "y":

                    atexit.register(write_history_to_log, history, "log.txt")
                    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
                else:
                    pass

            try:    
                regex = "echo ([\s\S]+)"
                if match := re.match(regex, word):
                    txt = match.groups()[0]
                    print(txt)
            except:
                print("Error: File " + file3 + " not found...")

            try:    
                regex = "dir ([\s\S]+)"
                if match := re.match(regex, word):
                    dirr = match.groups()[0]
                    list_directory(dirr)

            except Exception as exc:
                print(f"Error: {exc}")
            
            if word == "dir":
                list_directory()
            
            

                


                
                
                
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
                    
            
            try:    
                regex = "sort ([\s\S]+)"
                if match := re.match(regex, word):
                    fila = match.groups()[0]
                    sort_files(fila)
            except:
                print("Error: Something went wrong...")

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
                    print("Error: Not correct directory or folder name")
                # def hek():
            #    try:    
            #         packs()
            #     except Exception:
            #         print(Fore.RED + "Error: Packages Folder is missing..." + str(Exception))
            # hek()
 

            if word == "translate":
                rera = input("youre text>")
                lanl = input("language>")
                try:
                    translated = GoogleTranslator(source='auto', target=lanl).translate(rera)
                    translate()
                    print("youre text '"+ rera +"', translated to "+ lanl+" '"+translated+"'")
                except Exception:
                    print("Error")




            def calculate(expression):
                operators = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv
                }

                tokens = re.findall(r'(\d+|\W)', expression)
                stack = []

                for token in tokens:
                    if token.isdigit():
                        stack.append(float(token))
                    elif token in operators:
                        if len(stack) < 2:
                            return None  # Неправильный формат выражения
                        b = stack.pop()
                        a = stack.pop()
                        operator_func = operators[token]
                        result = operator_func(a, b)
                        stack.append(result)
                    else:
                        return None  # Неподдерживаемый оператор или неправильный формат выражения

                if len(stack) == 1:
                    return stack[0]
                else:
                    return None

            if word == "volume":
                c = wmi.WMI()
                def tom():
                    for disk in c.Win32_DiskDrive():
                        partitions = disk.associators("Win32_DiskDriveToDiskPartition")
                        for partition in partitions:
                            logical_disks = partition.associators("Win32_LogicalDiskToPartition")
                            for logical_disk in logical_disks:
                                print(f"")
                                print(f"{logical_disk.VolumeName} ({logical_disk.DeviceID})")
                print("Available Volumes List:")
                tom()
                print("")
                    
                

            # Пример использования функции
            #expression = input("Введите выражение: ")
            #result = calculate(expression)
            #if result is not None:
            #    print("Результат:", result)
            #else:
            #    print("Ошибка: Неправильное выражение")
            try:
                regex = "calcnotworked ([\s\S]+)"
                if match := re.match(regex, word):
                    express = match.groups()[0]

                    result = calculate(express)
                    if result is not None:
                        print("result:", result)
                    else:
                        print("Error: not correct operation")
            except Exception as exc:
                print(f"Error: {exc}")
                            

            


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


                            number1 = float(input('Enter first number: '))
                            op = input('Enter operator (+,-,*,/,**): ')
                            number2 = float(input('Enter second number: '))
                            sem()
                            result=calculate(number1,number2,op)
                            res = number1,op,number2, "=", result
                            print(res)
                        except Exception:
                            print("Error: Not correct operation or number")



            if word == "compare":
                try:
                    
                        


                    number11 = float(input('Enter first number: '))
                    number22 = float(input('Enter second number: '))
                    if number11 == number22:
                            result = str(number11) + " = " + str(number22)
                    elif number11 > number22:
                                result = str(number11) + " > " + str(number22)
                    elif number11 < number22:
                                result =  str(number11) + " < " + str(number22)
                    pat()
                    print(result)
                except Exception:
                    print("Error: Not correct operation or number")
            try:    
                regex = "run ([\s\S]+)"
                if match := re.match(regex, word):
                    file3 = match.groups()[0]
                    run(file3)
            except FileNotFoundError:
                print(f"File '{file3}' not found")
            except subprocess.CalledProcessError:
                print(f"Error occurred while running '{file3}'")
            try:    
                regex = "cd ([\s\S]+)"
                if match := re.match(regex, word):
                    file31 = match.groups()[0]
                    os.system("cd "+file31)
            except:
                print("Error: File " + file3 + " not found...")

            try:    
                regex = "listen ([\s\S]+)"
                if match := re.match(regex, word):
                    file5 = match.groups()[0]
                    playsound(file5)
            except FileNotFoundError:
                print("Error: File '" + file3 + "' not found...")
            except Exception:
                 print("Error: Something went wrong...")
            #if word == "opengame":
          #      def openpy():
         #           pyfil = input("filename>")
           #         clear()
            #        sleep(0.5)
             #       print("Starting " + pyfil + "...")
              #      sleep(2)
               #     call(["python", pyfil])
                #try:
                 #   openpy()
                #except:
                 #   print("Something gone wrong...")
                #clear()
                #openn1()

            def read(file):
                f = open(file, "r")
                content = f.read()
                print(content)
                f.close()

           # if word == "read":
            try:
                regex = "read ([\s\S]+)"
                if match := re.match(regex, word):
                    file = match.groups()[0]
                    read(file)
            except FileNotFoundError:
                    print("Error: File '"+file+"' not found.")
            
            except Exception:
                    print("Error: Can't read file '"+file+"'")

                # try:
                            #fil = input("filename>")   
                            #try:
                                #with open(fil) as file:
                                    #print(file.read())
                            #except FileNotFoundError:
                               # print("File " + fil + " not found :(")
               # except Exception:
                  #  print()



                
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
                    print("Error: Something went wrong...")


            try:
                def rename_file(old_name, new_name):
                    os.rename(old_name, new_name)

                regex = "rename ([\s\S]+) '([\s\S]+)'"
                if match := re.match(regex, word):
                    filename, newname = match.groups()
                    old_name=filename
                    new_name=newname
                    rename_file(old_name, new_name)
                    print(f"File '{filename}' successfully renamed to '{newname}'")   
            except FileNotFoundError:
                print(f"File '{old_name}' not found")
            except FileExistsError:
                print(f"File named '{new_name}' already exists")

            try:

                regex = "write ([\s\S]+) '([\s\S]+)'"
                if match := re.match(regex, word):
                    filename, content = match.groups()
                    content = content.replace(r'\n', '\n')
                    with open(filename, 'w') as file:
                        file.write(content)
                        print(f"File '{filename}' written successfully!")          

                    
            except FileNotFoundError:
                    print("Error: file '"+filename+"' not found.")
            except Exception:
                    print(f"Error: {Exception}")

            try:
                regex = "cd ([\s\S]+)"
                if match := re.match(regex, word):
                    asd23 = match.groups()[0]
                    os.chdir(asd23)
            except FileNotFoundError:
                    print("Error: folder '"+asd23+"' not found.")    
            except Exception:
                    print("Error: Something went wrong...")         

            def write_history_to_log(history, log_file):
                current_time = str(dt.now())
   
                print(f"creating LOG.txt {log_file}...")
                with open(log_file, "w") as file:
                        for word in history:
                            file.write(current_time+ " | "+">>>"+word + "\n")


            try:
                regex = "delete ([\s\S]+)"
                if match := re.match(regex, word):
                    dr12 = match.groups()[0]
                    print("Are you sure to delete '"+dr12+"'")
                    asd = input("No[N] or Yes[Y]>")
                    if asd == "y":
                        os.remove(dr12)
     
            except FileNotFoundError:
                    print("Error: file '"+dr12+"' not found.")
            except Exception:
                    print("Error: Something went wrong...")

            try:
                regex = "mktxt ([\s\S]+)"
                if match := re.match(regex, word):
                    dr1 = match.groups()[0]
                    open(dr1, 'x')
                    print("file '"+dr1+"' created successfully")

            except FileExistsError:
                    print("Error: file '"+dr1+"' already exists.")
            except Exception:
                    print("Error: Something went wrong...")

            try:
                regex = "mkdir ([\s\S]+)"
                if match := re.match(regex, word):
                    dr = match.groups()[0]
                    os.system("mkdir " + dr)
                    print("folder '"+dr+"' created successfully")
            except FileExistsError:
                    print("Error: folder '"+dr+"' already exists.")
            except Exception:
                    print("Error: Something went wrong...")

            if word == "pause":
                press_any_key()


            if word == "logo":
                print( "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)
                print( "█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████"), time.sleep(0.25)
                print( "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██░░░░░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░░░░░██████████░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
                print( "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)

                
            if word == "ussr":
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*****##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++--=+*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#++#%%%%%%%%%%%#*=--=+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----+#%%%%%%%%%%%#=---+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=---------+%%%%%%%%%%%%+----*%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+----------*%%%%%%%%%%%%%%%*----*%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----------#%%%%%%%%%%%%%%%%%+----#%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%*--------------+%%%%%%%%%%%%%%%%#-----%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-----=**=-----+%%%%%%%%%%%%%%%-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=+#%%%%*------+#%%%%%%%%%%%#-----*%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------+%%%%%%%%%%=-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+------+%%%%%%#=-----+%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+%%%%%%%%%%%+------+=------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------=+#%%%%%%%%#+-----------+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%*+=---+=------=++*****+---------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%#=-----+%%%%*=----------------------+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%#-----=#%%%%%%%%#*+=----------=+=----=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print( f"%%%%%%%%%%%%%%%%%%%%%%%+=+*#%%%%%%%%%%%%%%%%%####%%%%%%*==#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print( f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
   
            if word == "exit":
                atexit.register(write_history_to_log, history, "log.txt")
                break

            if word == "save":
                atexit.register(write_history_to_log, history, "log.txt")
                print("MG-DOS history saved to log.txt")
            
        ##print("Unknown command, to get help type 'help'")
                 
    
    
    wiltru()
allcommand()


















