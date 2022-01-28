
#class för en person med variablerna number och alias
class Person:
    #konstruktorn initierar klassen med parametern number
    def __init__(self,number):
        self.number = number
        
#main fungerar som ett menusystem vilket kallar i sin följd på funktion add... etc beroende på input        
def main():
    #dictionary för nummer och i sin följd namn som nycklar
    numberlist = {} 
    #oändrig while loop vilket först tar input x, vilket vi sedan matchar mot add... etc.
    while(True):
        choice = input("input stuff \n")
        #splittar våran input vid mellanslagen
        menuchoice = choice.split(" ")
        #match måste köras med python 3.10
        #simpel try-catch
        try:
            #matchchoice fungerar som en lista, där vi först läser av index 0 av våran input för att matcha mot vårat menuval.
            match menuchoice[0]:
                case "add":
                    #*menuchoice[1:] tar index 1 och framåt i våran input. Denna input skickas vidare till våran valda funktion 
                    add(numberlist, *menuchoice[1:])
                case "lookup":
                    lookup(numberlist, *menuchoice[1:])
                case "alias":
                    alias(numberlist, *menuchoice[1:])
                case "change":
                    change(numberlist, *menuchoice[1:])
                case "save":
                    save(numberlist, *menuchoice[1:])
                case "load":
                    load(numberlist, *menuchoice[1:])
                case "quit":
                    print("quiting program")
                    break
        #except för keyboardInterrupt 
        except(KeyboardInterrupt):
            break
        #fångar upp typeError vid fall att vi inputtar för många parametrar till våran valda funktion
        except(TypeError):
            print("to few/many arguments")

           

#funktion för att lägga till nummer samt namn
def add(numberlist,name,number):
    #checkar om namnet inte finns med i dictionary. Om namnet inte finns så lägger vi till både vårat inputtade namn samt nummer i dictionary där namnet fungerar som en nyckel.
    if name not in numberlist.keys():
        #när vi lägger till namn och nummer så kallar vi på class Person vilket skapar ett nytt personobjekt som håller koll på nummer.
        numberlist[name]=Person(number)
    else:
        print("this name already exist")

#funktion för att söka upp nummer        
def lookup(numberlist,name):
    #checkar om namnet finns med i dictionary. Om namnet finns så printar vi ut telefonnummer
    if name in numberlist.keys():
        print(numberlist[name].number)
    else:
        print("this name does not exist")

#funktion för att lägga till alias 
def alias(numberlist,name,alias):
    ##heckar om namnet finns med i dictionary. Om namnet finns med i dictionary så assignar vi att våran inputtade alias ska peka på samma personobjekt som vårat namn gör.
    if name in numberlist.keys():
        numberlist[alias] = numberlist[name]
    else:
         print("this name does not exist")

#funktion för att ändra telefonnummer
def change(numberlist,name,newnumber):
    #checkar om namnet finns med i dictionary. Om namnet finns så overridar vi värdet i numberlist[name].number till värdet av newnumber och därmed får ett nytt nummer
    if name in numberlist.keys():  
        numberlist[name].number = newnumber
    else:
        print("this name does not exist")
    
#funktion för att spara namn och nummer
def save(numberlist,filename):
    #öppnar en fil med vårat inputtade "filename" med read/write access samt access att skapa en ny fil om "filename" inte redan finns. Filen skapas sedan i f:
    with open(filename,"w+") as f:
        for x in numberlist.keys():
            #skapar en variabel saved data vilket sparar ner x som vårat namn och numberlist[x].number som vårat nummer
            saved_data= x + ";" + numberlist[x].number + ";"
            #sparar ner våran data
            f.write(saved_data+"\n")
    f.close()

#funktion för att ladda våran sparade data
def load(numberlist,filename):
    #clearar våran numberlist för att undvika duplicates 
    numberlist.clear()
    with open(filename, "r") as f:
        for row in f:
           #läser våran sparade data som ett index där x[0] = namn, och x[1] = telefonnummer
           x = row.split(";")
           numberlist[x[0]]=Person(x[1])

#fuktion för att avsluta programmet
def quit():
    print("quiting program")
    
    
#kallar på main
main()