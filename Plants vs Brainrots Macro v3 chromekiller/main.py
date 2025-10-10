#!/usr/bin/python3
########################################################################################################
##########################################################################################################
#pip ensure                                 
import subprocess
import sys
import importlib
import time
import json
import os
                                                    
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
    # Liste des packages et versions spécifiques si besoin
    packages = {
        "pydirectinput": None,
        "pynput": None,
        "colorama": None,
        "pyfiglet": None,
        "playsound": "1.2.2"  # version stable pour Windows
    }

    installed = []
    failed = []

    for package, version in packages.items():
        try:
            importlib.import_module(package)
            print(f"{package} ✔️ already installed")
            installed.append(package)
        except ImportError:
            # Essayer d'installer
            try:
                pkg_name = f"{package}=={version}" if version else package
                print(f"Installing {pkg_name}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", pkg_name])
                print(f"{package} Succesfully installed ✔️")
                installed.append(package)
            except subprocess.CalledProcessError as e:
                print(f"❌ Error while installing {package} : {e}")
                failed.append(package)

    
    print("\n=== Packages ===")
    print(f"Successfully installed ({len(installed)}): {', '.join(installed)}")
    if failed:
        print(f"Error ({len(failed)}): {', '.join(failed)}")
    else:
        print("All packages have been installed sucessfully ✔️")

if __name__ == "__main__":
    verifiepackage()


##########################################################################################################
##########################################################################################################
#Main 
import colorama
import pyfiglet
import threading
import time
import playsound
from assets import seeds, gear, retour, loading, collectmoney, ascii_art

#musique
music = input("Music yes or no ? y/n : ").lower()
if music == "y":
    file_pathe = os.path.join(os.path.dirname(__file__), "assets", "karkerkar.mp3")
    def jouer_musique():
        playsound.playsound(file_pathe)
    threading.Thread(target=jouer_musique, daemon=True).start()

#text
texte1 = pyfiglet.figlet_format("By @vexeee333")
print(colorama.Fore.GREEN + ascii_art + pyfiglet.figlet_format("Anaconda Macro") + texte1 + colorama.Style.RESET_ALL)
texte2 = pyfiglet.figlet_format("Setup")
print(colorama.Fore.LIGHTWHITE_EX + texte2 + colorama.Style.RESET_ALL)

# reconnexion
load = input(colorama.Fore.LIGHTMAGENTA_EX + "Do you want to load your saved config ? if it's the first time you launch please press n -> y/n : ").lower()
file_path = os.path.join(os.path.dirname(__file__), "saves.json")
if load == "n":
    time1 = int(input(colorama.Fore.CYAN + "Enter the time you'll be automaticaly reconnect (60 minutes are recommended) (in minutes): " + colorama.Style.RESET_ALL))
    url1 = (input(colorama.Fore.CYAN + "Enter the url of your private server, please follow the instructions of the readme.txt : " + colorama.Style.RESET_ALL))
    #files
    saves = input(colorama.Fore.YELLOW +"Do you want to save this setup in a file for the next launch ? y/n : " + colorama.Style.RESET_ALL).lower()
    if saves == "y":
        #json
        donnees = {
            "time": time1,
            "url": url1,
        }

        with open(file_path, "w") as f:
            json.dump(donnees, f, indent=4)  

        print("✅ Data saved")
else :
    with open(file_path, "r") as f:
        setup = json.load(f)
   
    time1 = setup["time"]
    print(f" {time1} minutes")
    url1 = setup["url"]
    print(f" private server url {url1} ")

print(colorama.Fore.MAGENTA + "Ensure to follow the macro guide on the file readme.txt" + colorama.Style.RESET_ALL)
launch = input("Setup completed, Press any key to launch and close the window to leave...")

for i in range(10, 0, -1):
    print(f"the macro will begin in {i}")
    time.sleep(1)

print(colorama.Fore.RED +"The macro is running" + colorama.Style.RESET_ALL) 

lock = threading.Lock()
PAUSE_DURATION = 60

def reco(x, y):
    while True:
        lock.acquire()
        print("url launch")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        proc = subprocess.Popen([chrome_path, x])
        time.sleep(PAUSE_DURATION)
        os.system('taskkill/im chrome.exe /f')
        time.sleep(2)
        loading()
        time.sleep(2)
        lock.release()

        time.sleep(y * 60)

t = threading.Thread(target=reco, args=(url1, time1), daemon=True)
t.start()

while True:
    with lock: 
        seeds()
        gear()
        collectmoney()
        retour()
    time.sleep(0.1)

        

##########################################################################################################
##########################################################################################################