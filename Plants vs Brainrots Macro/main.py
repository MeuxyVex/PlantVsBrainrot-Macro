#!/usr/bin/python3
########################################################################################################
##########################################################################################################
#pip ensure                                 
import subprocess
import sys
import importlib
import time
from assets import seeds, gear, retour                                                         
def verifierpip():
    try:
        import pip
    except ImportError:
        print("Pip n'est pas encore installer, \nLancement de l'installation...")
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            print("Installer avec succès !")
            input("Appuyez sur Entrée pour continuer...")
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
        except subprocess.CalledProcessError:
            print("Echec de l'installation, nouvelle tentative...")
        import urllib.request
        import os
        url = "https://bootstrap.pypa.io/get-pip.py"
        get_pip = "get-pip.py"
        urllib.request.urlretrieve(url, get_pip)
        subprocess.check_call([sys.executable, get_pip])
        os.remove(get_pip)
        print("Installation réussi")
        input("Appuyez sur Entrée pour continuer...")
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    else:
        print("PIP ✔️")
if __name__ == "__main__":
    verifierpip()

##########################################################################################################
##########################################################################################################
#ensure packages 
def verifiepackage():
    installed = []
    packages = ["pydirectinput", "pynput", "colorama", "pyfiglet",]
    for package in packages:
        try:
            importlib.import_module(package)
            installed.append(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
            print(package, "Installés avec succès")
            installed.append(package)
    if len(installed) == len(packages):
        print("Colorama✔️, pyfiglet✔️, pynput ✔️, pydirectinput ✔️")

if __name__ == "__main__":
    verifiepackage()


##########################################################################################################
##########################################################################################################
#Main 
import colorama
import pyfiglet

texte1 = pyfiglet.figlet_format("Plant vs brainrot Macro \n By @vexeee333")
print(colorama.Fore.MAGENTA + texte1 + colorama.Style.RESET_ALL)


texte2 = pyfiglet.figlet_format("Setup")
print(colorama.Fore.LIGHTWHITE_EX + texte2 + colorama.Style.RESET_ALL)
times = int(input(colorama.Fore.CYAN + "Enter the time the money will be collect (in minutes): " + colorama.Style.RESET_ALL))
gear1 = input(colorama.Fore.BLUE +"Do you want to collect gears ? y/n : " + colorama.Style.RESET_ALL)
collectseeds = input(colorama.Fore.GREEN +"Wich seeds do you want to collect (For exemple mango-sunflower) : " + colorama.Style.RESET_ALL)
saves = input(colorama.Fore.YELLOW +"Do you want to save this setup in a file for the next launch ? y/n : " + colorama.Style.RESET_ALL)

print(colorama.Fore.MAGENTA + "Ensure to follow the macro guide on the file readme.txt" + colorama.Style.RESET_ALL)
launch = input("Setup completed, Press any key to launch and close the window to leave...")

for i in range(10, 0, -1):
    print(f"the macro will begin in {i}")
    time.sleep(1)

print(colorama.Fore.RED +"The macro is running" + colorama.Style.RESET_ALL)    
while True:
    seeds()
    gear()
    retour()
    
    


##########################################################################################################
##########################################################################################################





        





    






