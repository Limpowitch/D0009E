
class Person:
    def __init__(self,number):
        self.number = number
        self.alias = []
        
def main():
    numberlist = {} 
    while(True):
        choice = input("input stuff \n")
        menuchoice = choice.split(" ")
        try:
            match menuchoice[0]:
                case "add":
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
        except(KeyboardInterrupt):
            break
        except(TypeError):
            print("to few/many arguments")

            #match måste köras med python 3.10


def add(numberlist,name,number):
    if name not in numberlist.keys():
        numberlist[name]=Person(number)
    else:
        print("this name already exist")
        
def lookup(numberlist,name):
    if name in numberlist.keys():
        print(numberlist[name].number)
    else:
        print("this name does not exist")

def alias(numberlist,name,alias):
    if name in numberlist.keys():
        numberlist[alias] = numberlist[name]
    else:
         print("this name does not exist")

def change(numberlist,name,newnumber):
    if name in numberlist.keys():  
        numberlist[name].number = newnumber
    else:
        print("this name does not exist")
    
def save(numberlist,filename):
    with open(filename,"w+") as f:
        for x in numberlist.keys():
            saved_data= x + ";" + numberlist[x].number + ";"
            f.write(saved_data+"\n")
    f.close()
        
def load(numberlist,filename):
    numberlist.clear()
    with open(filename, "r") as f:
        for row in f:
           x = row.split(";")
           numberlist[x[0]]=Person(x[1])
def quit():
    print("quiting program")
    
    

main()