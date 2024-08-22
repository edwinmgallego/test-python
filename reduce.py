from functools import reduce

def suma(x,y):
    return x+y
numeros=[1,2,3,4,5,6,7,8,9,10]
print(reduce(suma,numeros))