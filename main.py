def a_power_b(a,b):
    acum=1
    for i in range (0,b):
        acum = a*acum
    return acum

while True:
    
    num1=float(input("Ingrese un número: "))
    num2=int(input("Ingrese un número: "))
    print("El resultado de elevar",num1,"a",num2,"es:",a_power_b(num1,num2))
    
    if num1==0:
        break


print("Fin del programa")





