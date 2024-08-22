def cuadrado(x):
    return x**2

lista= [1,2,3,4,5]
cuadrados= map(cuadrado,lista)
print(list(cuadrados))