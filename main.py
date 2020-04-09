def a_power_b(a,b):
    acum=1
    for i in range (0,b):
        acum = a*acum
    return acum

num1=float(input("Ingrese un número: "))
num2=int(input("Ingrese un número: "))

print(a_power_b(num1,num2))


