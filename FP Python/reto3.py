import os
import platform
import time

def monitor_clear():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')

coordenadas =[]
user="51644"
pw="44615"
#reto 1
while True:
    monitor_clear()
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

    userid = input("Ingrese su nombre de usuario: ")

    if userid!="":
        break

if userid == user:
        password = (input("Ingrese su contraseña: "))
        oneterm=644
        seterm=(5+1-6+4) and (4+5-6+1) and (-(5%4)-1+6)
        
        while True:
            if password == pw:
                result=int(input(str(oneterm)+" + "+str(seterm)+" = "))
                break
            else:
                monitor_clear()
                print("Error")
                exit()
        
        if result == oneterm+seterm:
            monitor_clear()
            print("Sesión iniciada")
            #reto 2

            time.sleep(2)
            monitor_clear()
            menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
            intentos=0

            while True:
                if intentos >= 3:
                    monitor_clear()
                    print("Error")
                    exit()

                for i in range(len(menu)):
                    print(str(i+1)+". ",menu[i])
            
                try:
                    opcion=int(input("Elija una opción "))
                    if opcion < 1 or opcion > 7:
                        print("Error")
                        intentos +=1
                        time.sleep(2)
                    elif opcion == 6:
                        try:
                            favorita=int(input("Seleccione opción favorita "))
                            intentos=0
                            if favorita < 1 or favorita > 5:
                                monitor_clear()
                                print("Error")
                                exit()
                            else:
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
                                            monitor_clear()
                                        else:
                                            print("Error")
                                    else:
                                        print("Error") 
                                except ValueError:
                                    print("Error")   
                        
                        except ValueError:
                            monitor_clear()
                            print("Error")
                            exit()

                    elif opcion >=1 and opcion <= 5:
                        print("Usted ha elegido la opción número "+str(opcion))
                        #reto 3

                        if menu[opcion - 1] == "Cambiar contraseña":
                            password2=(input("Ingrese la contraseña actual: "))
                            if password == password2:
                                password2 = (input("Ingrese la nueva contraseña: "))
                                if password != password2:
                                    password = password2
                                else:
                                    print("Error")
                                    exit()
                            else:
                                print("Error")
                                exit()
                        
                        elif menu[opcion - 1] == "Ingresar coordenadas actuales":
                            if len(coordenadas) == 0:
                                coordenadas=[[0] * 2 for i in range(3)]
                                for i in range(3):
                                    for j in range(2):
                                        try:
                                            if j == 0:
                                                coordenadas[i][j] = float(input("Digite la latitud para la coordenada "+str(i+1)+": "))
                                                coordenadas[i][j] = round(coordenadas[i][j],3)
                                                if coordenadas[i][j] > 2.766 or coordenadas[i][j] < 2.548:
                                                    print("Error coordenada")
                                                    exit()
                                            else:
                                                coordenadas[i][j] = float(input("Digite la longitud para la coordenada "+str(i+1)+": "))
                                                coordenadas[i][j] = round(coordenadas[i][j],3)
                                                if coordenadas[i][j] > -76.493 or coordenadas[i][j] < -76.879:
                                                    print("Error coordenada")
                                                    exit()
                                        except ValueError:
                                            print("Error")
                                            exit()

                            else:
                                for i in range(3):
                                    print("coordenada [latitud,longitud] "+str(i+1)+" :", coordenadas[i])
                                print("La coordenada "+str(coordenadas.index(max(coordenadas))+1) +" es la que está más al sur")
                                latitud_promedio = 0
                                longitud_promedio = 0
                                for i in range(3):
                                    for j in range(2):
                                        if j == 0:
                                            latitud_promedio = latitud_promedio + coordenadas[i][j]
                                        else:
                                            longitud_promedio = longitud_promedio + coordenadas[i][j]
                                latitud_promedio /=3
                                longitud_promedio /=3
                                latitud_promedio = round(latitud_promedio,3)
                                longitud_promedio = round(longitud_promedio,3)
                                print("La coordenada promedio de todos los puntos [latitud,longitud] : ["+str(latitud_promedio)+","+str(longitud_promedio)+"]")
                                time.sleep(2)
                                try:
                                    actualizar_coordenada = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú "))
                                    if actualizar_coordenada >= 1 and actualizar_coordenada <= 3:
                                        coordenadas[actualizar_coordenada - 1][0] = round(float(input("Digite la latitud para la coordenada "+ str(actualizar_coordenada)+" ")),3)
                                        if coordenadas[int(actualizar_coordenada) -1 ] [0] >2.766 or coordenadas[actualizar_coordenada -1 ][0] < 2.548:
                                            print("Error coordenada")
                                            exit()
                                        coordenadas[actualizar_coordenada - 1][1] = round(float(input("Digite la longitud para la coordenada "+ str(actualizar_coordenada)+" ")),3)
                                        if coordenadas[i][j] > -76.493 or coordenadas[i][j] < -76.879:
                                            print("Error coordenada")
                                            exit()
                                    elif actualizar_coordenada == 0:
                                        pass
                                    else:
                                        print("Error actualización")
                                        exit()
                                except ValueError:
                                    print("Error actualización")
                                    exit()
                            #fin reto 3
                        
                    elif opcion == 7:
                        print("Hasta pronto")
                        exit()

                except ValueError:
                    monitor_clear()
                    print("Error")
                    exit()


        else:
            print("Error")
else:
    print("Error")