from art import * # download Python Art library for having the program functional
import time

class Main: # the Main class of the code storing all the methods
    
    def asciiConsole(): # the non-saving generator
    
        # generating function
        print("non-saving mode")
        print("")
        text = str(input("Enter the text you want to convert: "))
        print("Your text is gonna be converted into an ASCII art.")
        artpiece = text2art(text)
        print(artpiece)
        
        # info and restart
        print("Your art is ready for copying, but ISN'T saved!!!")
        print("Cancelling the program will erase your art.")
        print("")
        Main.asciiConsole()

    def asciiConsoleSaver(): # the saving generator
       
        # converting and printing the art
        print("saving mode")
        print("")
        text = str(input("Enter the text you want to convert: "))
        print("Your text is gonna be converted into an ASCII art.")
        artpiece = text2art(text)
        print(artpiece)
        
        # saving the art into a file
        with open("/home/cathodec/Desktop/art.txt", "w") as saveArt: # edit the file path here to your own
            saveArt.write(artpiece)
        print("Your art is now saved.")
        print("")

        # restart
        def runner():
    
            print("Restart the program?")
            choice = str(input("[Y/N]: "))
    
            if choice == "Y":
                Main.main()
            elif choice == "N":
                quit()
            else:
                print("Sorry - didn't understand - again? ")
                runner()
    
    def main(): # beginning navigator function
        
        # an introduction
        tprint("ASCII Art generator")
        print("SHINY PIECE OF A CODE WHICH TURNS YOUR TEXT INTO AN ASCII ART")
        print("Made with love by Rene Valenta, 2022")
        print("")
        print("Choose the mode you wanna start: ")
        print("")
        print("[0] ASCII art only into the console (for late copying)")

        startup = input("[1] ASCII art that will also save itself into a file automatically: ") 
    
        if startup == "1":
            Main.asciiConsoleSaver()
        elif startup == "0":
            Main.asciiConsole()
        else:
            print("Sorry - again?")
            Main.main()

Main.main()
