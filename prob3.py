from math import factorial
n=int(input('Dati n='))
m=int(input('Dati m='))
if n<m:
    print('N trebuie sa fie mai mare ca M')
    exit()
def f(x):
    s=0
    d=1
    for i in range(1, x+1):
        d*=1
    return d
num=factorial(m) * (factorial(n-m))
c=factorial(n)/num
print('n/m(n-m) =', c)