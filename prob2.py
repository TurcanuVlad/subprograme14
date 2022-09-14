a=int(input('Dati numaratorul primei fractie:'))
b=int(input('Dati numitorul primei fractie:'))
c=int(input('Dati numaratorul 2 fractie:'))
d=int(input('Dati numitorul 2 fractie:'))
from fractions import Fraction
def afract():
    s=Fraction(a,b)+Fraction(c,d)
    return s
def pfract():
    p=Fraction(a,b) * Fraction(c,d)
    return p
print('Suma=', afract())
print('Produsul=', pfract())