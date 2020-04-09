def a_power_b(a,b):
    acum=1
    for i in range (0,b):
        acum = a*acum
    return acum

contp=0
contim=0
conte=0

while True:
    
    try:
        num1=float(input("Ingrese un número: "))
        num2=int(input("Ingrese un número: "))
        c = a_power_b(num1,num2)
        print("El resultado de elevar",num1,"a",num2,"es:",c)
    
        if num1==0:
            break
        
        if c % 2==0:
            contp += 1
        else:
            contim += 1
    
    except:
        print("Error al ingresar los valores númericos, por favor vuelva a ingresarlos.")
        conte += 1

print("Durante la ejecución del programa:\nSe calcularon",contim+contp,"potencias.") 
print(contp,"dieron como resultado un número par.")
print(contim,"dieron como resultado un número impar.")
print("Y se presentaron",conte,"errores de digitación durante la ejecución del programa.")


print("Fin del programa")





