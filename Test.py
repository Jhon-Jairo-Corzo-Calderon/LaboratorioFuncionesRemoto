#Sistemas para saber cuando un número es perfecto o no.

def perfect_number(n):
    suma=0
    for i in range(1,n):
        if (n % i == 0):
            suma+=i

    if n == suma:
        return True
    else:
        return False
    
n=int(input("Por favor digite un numero entero: "))

if perfect_number(n):
    print(n,"Es un número perfecto")
else:
    print(n,"No es un número perfecto")