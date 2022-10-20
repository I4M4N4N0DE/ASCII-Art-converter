import art as ar # nutno stáhnout knihovnu python-art pro funkčnost
import time
    
def asciiConsole(): # generátor bez ukládání
        
    # funkce generátoru
    print("režim bez ukládání")
    print("")
    text = str(input("Napiš text co chceš převést: "))
    print("Z tvého textu se teď stane ASCII umění.")
    artpiece = ar.text2art(text)
    print(artpiece)
        
    # info a restart
    print("Tvé umění je ready na zkopírování, ale NENÍ uloženo!!!")
    print("Zavřením programu přijdeš o své umění.")
    print("")
        
    while True:
            
        # restart
        print("Restartovat program?")
        choice = str(input("[A/N]: "))
    
        if choice == "A":
            main()
        elif choice == "N":
            quit()
        else:
            print("Promiň - nerozuměl jsem ti - znovu: ")

def asciiConsoleSaver(): # generátor s ukládáním

    # konverze a tisk artu
    print("režim s ukládáním")
    print("")
    text = str(input("Napiš text co chceš převést: "))
    print("Z tvého textu se teď stane ASCII umění.")
    artpiece = ar.text2art(text)
    print(artpiece)
        
    # uložení artu do souboru
    with open("/home/cathodec/Desktop/art.txt", "w") as saveArt: # změň si cestu k souboru podle sebe a pojmenuj jak chceš
        saveArt.write(artpiece)
        print("Tvé umění je uloženo.")
        print("")

    while True:
            
        # restart
        print("Restartovat program?")
        choice = str(input("[A/N]: "))
    
        if choice == "A":
            main()
        elif choice == "N":
            quit()
        else:
            print("Promiň - nerozuměl jsem ti - znovu: ")
    
# funkce počátečního navigátoru
def main():
        
    # uvedení
    ar.tprint("ASCII Art generator")
    print("SKVOSTNÝ KUS KÓDU, KTERÝ UDĚLÁ Z TVÉHO TEXTU ASCII ART")
    print("Copyright: René Valenta 2022")
    print("")
    print("Vyber režim, který chceš: ")
    print("")
    print("[0] pouze ASCII art v terminálu (pro kopírování)")
        
    while True:

        startup = input("[1] ASCII art, co se následně uloží do souboru: ") 
    
        if startup == "1":
            asciiConsoleSaver()
        elif startup == "0":
            asciiConsole()
        else:
            print("Promiň - znovu: ")
main()
