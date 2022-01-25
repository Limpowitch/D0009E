

ordlista = []
#funktion för att lägga till ett ord
def addword():
    while(True):
        #user matar in 1 eller 2 för att lägga till ett ord eller för att bryta while loopen. om input inte är 1 eller 2 returneras "invalid input"
        val = int(input("Vill du lägga till ett ord eller gå bak? Välj menu 1 eller 2\n"))
        if val == 1:
            ord = input("ord\n")
            Hittat = False
            #skapar en variabel vilket till början är false. Om ordet vi vill mata in redan finns i ordlistan, gör vi om variabel Hittat = True och därmed lägger inte till ordet i ordlistan.
            for term, _ in ordlista:
                if term == ord:
                    print("Sluta genast")
                    Hittat = True
            if Hittat == False:
                beskrivning = input("beskrivning\n")
                ordlista.append((ord,beskrivning))
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
            ord = input("välj ett ord du vill söka upp\n")
            #om termen vi söker efter finns i ordlistan så printar vi ut relaterad beskrivning
            for term, beskrivning in ordlista:
                if term == ord:
                    print(beskrivning) 
                    return
            print("nehe")
        
        elif val == 2:
            break 

#huvudfuktion vilket kallar på addword() och searchword()
def main_lst(): 
    while(True):
        #samma sort av menusystem som i addword() och searchword()
        print("Hej. Välj 1 för lägga till ord, 2 för att söka upp ett ord, 3 för att avsluta") 
        var=None
        try:
            var = int(input())
        except:
            print("Not a valid choice")
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