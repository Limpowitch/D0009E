

ordlista = {}
#funktion för att lägga till ett ord
def addword():
    while(True):
        #user matar in 1 eller 2 för att lägga till ett ord eller för att bryta while loopen. om input inte är 1 eller 2 returneras "invalid input"
        val = int(input("Vill du lägga till ett ord eller gå bak? Välj menu 1 eller 2\n"))
        if val == 1:
            ord = input("ord\n")
            #om ordet inte finns redan i ordlistan, så assignar vi det inmatade ordet som en nyckel till beskrivning
            if ord not in ordlista.keys(): 
                beskrivning = input("beskrivning\n")
                ordlista[ord]=beskrivning
            else:
                print("detta ord finns redan i listan")
                
        elif val == 2:
            break
        else:
            print("Invalid input")

#funktion för att söka upp ett ord
def searchword():
    while(True):
        print("Vill du söka upp ett ord eller gå bak? Välj menu 1 eller 2")
        val = int(input())
        if val == 1:
            #om det inmatade ordet finns som en nyckel, så printar vi ut beskrivningen då vi tidigare har gjort ordlista[ord]=beskrivning
            ord = input("välj ett ord du vill söka upp\n")  
            if ord in ordlista.keys(): 
                print(ordlista[ord])
            else:
                print("nehe")
        
        elif val == 2:
            break
def main_lst():

#huvudfuktion vilket kallar på addword() och searchword()   
    while(True):
        #samma sort av menusystem som i addword() och searchword()
        print("Hej. Välj 1 för lägga till ord, 2 för att söka upp ett ord, 3 för att avsluta")
        var=None
        try:
            var = int(input())
        except:
            print("This is not a valid choice")
        #kallar på addword()
        if var == 1:
            addword()
        #kallar på searchword()
        if var == 2:
            searchword()
        if var == 3:
            break
#kallar på main_1st()
main_lst()