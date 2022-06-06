import os
import time
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user=51644
pw=44615

userid=input("Ingrese su nombre de usuario: ")
if int(userid)==user:
    password=input("Ingrese su contraseña: ")
    if int(password)==pw:
        oneterm=644
        seterm=(5+1-6+4) and (4+5-6+1) and (-(5%4)-1+6)
        result=int(input(str(oneterm)+" + "+str(seterm)+" = "))
        if result == (oneterm+seterm):
            os.system("cls")          
            print("Sesión iniciada") 
            
            time.sleep(2)
            os.system("cls")
            menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
            intentos=0

            while True:
                if intentos >= 3:
                    
                    print("Error")
                    exit()

                for i in range(len(menu)):
                    print(str(i+1)+". ",menu[i])
            
                try:
                    opcion=int(input("Elija una opción "))
                    if opcion < 1 or opcion > 7:
                        print("Error")
                        intentos +=1
                        
                    elif opcion == 6:
                        try:
                            favorita=int(input("Seleccione opción favorita "))
                            intentos=0
                            if favorita >=1  and favorita <= 5:
                                
                                try:
                                    r1=4
                                    adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                    if adio == r1:
                                        r2=4
                                        adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                        if adis == 4:
                                            favorita -=1
                                            temporal = menu[favorita]
                                            menu.pop(favorita)
                                            menu.insert(0,temporal)
                                            
                                        else:
                                            print("Error")
                                    else:
                                        print("Error") 
                                except ValueError:
                                    print("Error")  
                                
                            else:
                                print("Error")
                                exit() 
                        
                        except ValueError:
                            
                            print("Error")
                            exit()

                    elif opcion >0 and opcion <6:
                        print("Usted ha elegido la opción "+str(opcion))
                        exit()
                    
                    elif opcion == 7:
                        print("Hasta pronto")
                        exit()

                except ValueError:
                    
                    print("Error")
                    exit()

        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")