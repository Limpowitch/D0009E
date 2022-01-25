
ordlista = []
ordbeskrivning = []
#funktion för att lägga till ett ord
def addword(): 
     while(True):
        #user matar in 1 eller 2 för att lägga till ett ord eller för att bryta while loopen. om input inte är 1 eller 2 returneras "invalid input"
        val = input("Vill du lägga till ett ord eller gå bak? Välj menu 1 eller 2\n") 
        if val == 1:
            ord = input("ord\n")
            #om ordet inte finns med i ordlistan, så lägger vi till det inmatade ordet samt ordbeskrivning i ordlista[]
            if ord not in ordlista: 
                beskrivning = input("beskrivning\n")
                ordlista.append(ord)
                ordbeskrivning.append(beskrivning)
            else:
                print("Sluta genast")
        elif val == 2:
            break
        else:
            print("invalid input")

#funktion för att söka upp ett ord
def searchword(): 
    while(True):
        #samma process som i addword()
        print("Vill du söka upp ett ord eller gå bak? Välj menu 1 eller 2") 
        val = int(input())
        if val == 1:
            ord = input("välj ett ord du vill söka upp\n")
            #lägger till ett index till inmatade ordet t.ex (0, Term[0]), (1, Term[1]) etc.
            for i, term in enumerate(ordlista): 
                #om term är detsamma som det inmatade ordet, så söker det upp vilket index term har och sedan get det index till ordbeskrivning[] och därmed printar ut ordbeskrivningen
                if term == ord: 
                    print(ordbeskrivning[i]) 
                    return
            print("nehe")
        elif val == 2:
            break
        else:
            print("invalid input")

#huvudfuktion vilket kallar på addword() och searchword()
def main_lst(): 
    while(True):
        print("Hej. Välj 1 för lägga till ord, 2 för att söka upp ett ord, 3 för att avsluta") #samma sort av menusystem som i addword() och searchword()
        var = None
        try:
            var = int(input())
        except:
            print("Not an valid choice")
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