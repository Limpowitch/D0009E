


def bounce(n):
    print(n)
    if n!=0:
        bounce(n-1)
        print(n)
    


def bounce2(n):
    for i in reversed(range(0,n+1)):
        print(i)
    for i in (range(1,n+1)):
        print(i)



import d0009e_lab2_bounceTest  

def tvarsumman(n):
    if n > 0:
        return (n % 10) + tvarsumman(n // 10)
    return 0
    # return (n % 10) + tvarsumman(n // 10) if n > 0 else 0




def tvarsumman2(n):
    sum=0
    while n!=0:
        sum += n % 10
        n = n // 10
    return sum



import d0009e_lab2_sumTest
