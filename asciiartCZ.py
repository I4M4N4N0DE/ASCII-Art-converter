from art import * # nutno stáhnout knihovnu python-art pro funkčnost
import time

class Main: # hlavní třída Main se všemi metodami
    
    def asciiConsole(): # generátor bez ukládání
        
        # funkce generátoru
        print("režim bez ukládání")
        print("")
        text = str(input("Napiš text co chceš převést: "))
        print("Z tvého textu se teď stane ASCII umění.")
        artpiece = text2art(text)
        print(artpiece)
        
        # info a restart
        print("Tvé umění je ready na zkopírování, ale NENÍ uloženo!!!")
        print("Zavřením programu přijdeš o své umění.")
        print("")
        Main.asciiConsole()

    def asciiConsoleSaver(): # generátor s ukládáním

        # konverze a tisk artu
        print("režim s ukládáním")
        print("")
        text = str(input("Napiš text co chceš převést: "))
        print("Z tvého textu se teď stane ASCII umění.")
        artpiece = text2art(text)
        print(artpiece)
        
        # uložení artu do souboru
        with open("/home/cathodec/Desktop/art.txt", "w") as saveArt: # změň si cestu k souboru podle sebe a pojmenuj jak chceš
            saveArt.write(artpiece)
        print("Tvé umění je uloženo.")
        print("")

        # restart
        def runner():
    
            print("Restartovat program?")
            choice = str(input("[A/N]: "))
    
            if choice == "A":
                Main.main()
            elif choice == "N":
                quit()
            else:
                print("Promiň - nerozuměl jsem - znovu? ")
                runner()
    
    # funkce počátečního navigátoru
    def main():
        
        # uvedení
        tprint("ASCII Art generator")
        print("SKVOSTNÝ KUS KÓDU, KTERÝ UDĚLÁ Z TVÉHO TEXTU ASCII ART")
        print("Copyright: René Valenta 2022")
        print("")
        print("Vyber režim, který chceš: ")
        print("")
        print("[0] pouze ASCII art v terminálu (pro kopírování)")

        startup = input("[1] ASCII art, co se následně uloží do souboru: ") 
    
        if startup == "1":
            Main.asciiConsoleSaver()
        elif startup == "0":
            Main.asciiConsole()
        else:
            print("Promiň - znovu: ")
            Main.main()

Main.main()
