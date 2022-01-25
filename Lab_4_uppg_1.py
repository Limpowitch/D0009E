class Board:
    def __init__(self,msg):
        self.sugmin = [msg] 
        
    
    def addmessage(self):
        message = input("add message")
        self.sugmin.append(message)
        


def main():
    Board_1 = Board("XOXO")
    Board_2 = Board("A spectre is haunting europe")
    kim = Board_1
    chris = Board_2
    while(True):
        print("=== Bulletin Board System ===")
        print("Kim reads message:", kim.sugmin)
        print("Chris reads message:", chris.sugmin)
        print("1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: exit")
        print("Enter choice:")
        var = None
        try:
            var = int(input())
        except:
            print("Not a valid choice")
        if var == 1:
            if kim == Board_1:
                kim = Board_2
            else:
                kim = Board_1
        if var == 2:
            if chris == Board_2:
                chris = Board_1
            else:
                chris = Board_2
        if var == 3:
            Board_1.addmessage()
                
        if var == 4:
            Board_2.addmessage()
                
        if var == 0:
            break

main()
