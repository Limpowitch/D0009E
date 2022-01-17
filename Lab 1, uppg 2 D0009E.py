def recept(X):
    print("TILL FORMEN:")
    print("ca " , ((10/4)*X) , "g smör")
    print("ca " , ((0.75/4)*X) , "dl ströbröd")
    print("SOCKERKAKA")
    print(int((3/4)*X) , " st ägg")
    print((3/4)*X , " dl strösocker")
    print((2/4)*X , " dl bakpulver")
    print((3/4)*X , " dl vetemjöl")
    print((75/4)*X , " g smör")
    print((1/4)*X , " dl vatten")
def tidblanda(X):
    print("Det tar " , 10+X , " minuter att blanda smeten")
def tidgradda(X):
    print("Det tar " , (30+(3*X)) , " minuter att grädda kakan")
    recept(4)
    tidblanda(4)
    tidgradda(4)
    recept(7)
    tidblanda(7)
    tidgradda(7)



