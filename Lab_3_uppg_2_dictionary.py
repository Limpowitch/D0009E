def main_lst():
    ordlista = {}
    
    while(True):
        print("Hej. Välj 1 för lägga till ord, 2 för att söka upp ett ord, 3 för att avsluta")
        var = int(input())
        if var == 1:
            while(True):
                val = int(input("Vill du lägga till ett ord eller gå bak? Välj menu 1 eller 2\n"))
                if val == 1:
                    ord = input("ord\n")
                    beskrivning = input("beskrivning\n")
                    if ord not in ordlista.keys(): 
                        ordlista[ord]=beskrivning
                    else:
                        print("detta ord finns redan i listan")
                        
                elif val == 2:
                    break
    
    
    
        if var == 2:
            while(True):
                print("Vill du söka upp ett ord eller gå bak? Välj menu 1 eller 2")
                val = int(input())
                if val == 1:
                    ord = input("välj ett ord du vill söka upp\n")
                    if ord in ordlista.keys(): 
                        print(ordlista[ord])
                    else:
                        print("nehe")
                
                elif val == 2:
                    break
        if var == 3:
            break

main_lst()