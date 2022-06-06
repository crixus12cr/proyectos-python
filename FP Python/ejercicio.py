import os
import time

menu=["Sumar","Restar","Dividir","Multiplicar","Salir"]
os.system("cls") 
while True:
    resultado=0
    print("Que operacion deseas realizar\n")
    for i in range(len(menu)):
        print(str(i+1)+". ",menu[i])

    try:
        opcion=int(input("Elija una opción "))
        if opcion == 1:
            os.system("cls")
            time.sleep(1)
            print("SUMA\n")
            num1=int(input("Ingrese el primer numero "))
            num2=int(input("Ingrese el segundo numero "))
            resultado= num1+num2
            print("El resultado de la suma es: ",(resultado))
            continua=input("\nPresione ENTER para continuar ")
            time.sleep(1)
            os.system("cls")
        elif opcion == 2:
            os.system("cls")
            time.sleep(1)
            print("RESTA\n")
            num1=int(input("Ingrese el primer numero "))
            num2=int(input("Ingrese el segundo numero "))
            resultado= num1-num2
            print("El resultado de la resta es: ",(resultado))
            continua=input("\nPresione ENTER para continuar ")
            time.sleep(1)
            os.system("cls")
        elif opcion == 3:
            os.system("cls")
            time.sleep(1)
            print("DIVISION\n")
            num1=int(input("Ingrese el primer numero "))
            num2=int(input("Ingrese el segundo numero "))
            resultado= num1/num2
            print("El resultado de la division es: ",(resultado))
            continua=input("\nPresione ENTER para continuar ")
            time.sleep(1)
            os.system("cls")
        elif opcion == 4:
            os.system("cls")
            time.sleep(1)
            print("MULTIPLICACION\n")
            num1=int(input("Ingrese el primer numero "))
            num2=int(input("Ingrese el segundo numero "))
            resultado= num1*num2
            print("El resultado de la multiplicacion es: ",(resultado))
            continua=input("\nPresione ENTER para continuar ")
            time.sleep(1)
            os.system("cls")
        elif opcion == 5:
            os.system("cls")
            print("Hasta Luego")
            break
        else:
            os.system("cls")
            print("ERROR")
            break


    except ValueError:
        print("Error Valor incorrecto")
        exit()