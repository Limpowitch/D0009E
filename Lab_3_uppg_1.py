import Lab_2_Del1 as Del1
import Lab_2_Del2 as Del2

def f(x):
    return(x**2-1)

while(True):
    print("Hello here's your menu")   
    var = int(input())
    if var == 1:
        n = int(input("Ange n\n"))
        Del1.bounce(n)
        
    elif var == 2:
        n = int(input("Ange n\n"))
        print(Del1.tvarsumman(n))

    elif var == 3:
        x0 = int(input("Ange x0\n"))
        h = float(input("Ange h\n"))
        print(Del2.solve(f,x0,h))
    elif var == 4:
        break