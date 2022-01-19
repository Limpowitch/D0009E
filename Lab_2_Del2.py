import math


def f(x):
    return(x**2-3*x)
def derivative(f,x,h):
    k1 = (f(x+h)-f(x-h))/(2*h)
    h=h/2
    k2 = (f(x+h)-f(x-h))/(2*h)
    while abs(k2-k1) > 0.1:
        h = h/2
        k1 = k2
        k2 = (f(x+h)-f(x-h))/(2*h)
    return(k2)


def solve(f,x0,h):
    while abs(f(x0)) > h:
        x0 = (x0-((f(x0)/derivative(f,x0,h))))    
    return(x0)


import d0009e_lab2_solveTest
