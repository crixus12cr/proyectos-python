import os
import platform
import time
import math

def monitor_clear():
    if os.name == 'nt' or os.name == 'ce' or os.name == 'dos':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')

def mostrar_coordenadas_frecuentes(matriz):
    for i in range(len(matriz)):
        print("coordenada [latitud,longitud] " + str(i+1)+ " :", matriz[i])

def distancia_zonas(zonas, punto):
    latitud1 = math.radians(punto[0])
    longitud1 = math.radians(punto[1])
    r = 6372.795477598
    for i in range(len(zonas)):
        latitud2 = math.radians(zonas[i][0])
        longitud2 = math.radians(zonas[i][1])
        delta_long = longitud2 - longitud1
        distancia = (math.acos(math.sin(latitud1)* math.sin(latitud2) + math.cos(latitud1)* math.cos(latitud2)* math.cos(delta_long))) *r
        distancia *=1000
        distancia = round(distancia,3)
        zonas[i].append(distancia)
    #ordenamiento
    for i in range(len(zonas)-1):
        for j in range(i+1,len(zonas)):
            if zonas[i][3] > zonas[j][3]:
                distancias_tem = zonas[i]
                zonas[i] = zonas[j]
                zonas[j] = distancias_tem
    return(zonas[:2])     

def ordenar_vectores(vector):
    for i in range(len(vector) - 1):
        for j in range(i+1, len(vector)):
            if vector[i][2] > vector[j][2]:
                usuarios_promedio = vector[i]
                vector[i] = vector[j]
                vector[j] = usuarios_promedio
    return(vector)

def definirzonas():
    #matriz de 4 filas y 3 columnas datos wifi
    zonaswifi=[[2.698,-76.680,63],[2.724,-76.693,20],[2.606,-76.742,680],[2.698,-76.690,15]]
    validazonas = 0
    for i in range(4):
        for j in range(2):
            if j == 0:
                if zonaswifi[i][j] > 2.766 or zonaswifi[i][j] < 2.548:
                    print("La latitud de la coordenada",i+1,"No esta dentro de los límites estipulados")
                    validazonas = 1
            else:
                if zonaswifi[i][j] > -76.493 or zonaswifi[i][j] < -76.879:
                    print("La longitud de la coordenada",i+1,"No esta dentro de los límites estipulados")
                    validazonas = 1
    if validazonas == 0:
        print("Las coordenadas cumplen con los límites estipulados")
        return(zonaswifi)

    
coordenadas =[]
ubicactual = []
user="51644"
pw="44615"

#velocidades definidas reto 4
velmoto = 19.44
velbici = 3.33

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
                        print("Usted ha elegido la opción "+str(opcion))
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
                        elif menu[opcion - 1] == "Ubicar zona wifi más cercana":
                            zonaswifi = definirzonas()
                            monitor_clear()
                            if len(coordenadas) == 0:
                                print("Error sin registro de coordenadas")
                                time.sleep(2)
                                exit()
                            mostrar_coordenadas_frecuentes(coordenadas)
                            try:
                                submenuzona = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión "))
                                if submenuzona >= 1 and submenuzona <= 3:
                                    cordistancia = distancia_zonas(zonaswifi,coordenadas[submenuzona - 1])
                                    ubicactual = coordenadas[submenuzona - 1].copy()
                                    cordistancia = ordenar_vectores(cordistancia)
                                    print("Zonas wifi cercanas con menos usuarios")
                                    for i in range(len(cordistancia)):
                                        print("La zona wifi",i+1, "ubicada en [",cordistancia[i][:2],"] a", cordistancia[i][3], "metros, tiene en promedio",cordistancia[i][2],"usuarios")
                                    try:
                                        guia = "Para llegar a la zona wifi dirigirse "
                                        indicaciones = int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
                                        if indicaciones >= 1 and indicaciones <= 2:
                                            if coordenadas[submenuzona - 1][1] < cordistancia[indicaciones -1 ][1]:
                                                guia = guia + "primero al oriente"
                                            elif coordenadas[submenuzona - 1][1] > cordistancia[indicaciones -1 ][1]:
                                                guia = guia + "occidente"
                                            if coordenadas[submenuzona - 1][0] < cordistancia[indicaciones -1 ][0]:
                                                guia = guia + "y luego hacia el norte"
                                            elif coordenadas[submenuzona - 1][0] > cordistancia[indicaciones -1 ][0]:
                                                guia = guia + "y luego hacia el sur"
                                            tiempomoto = cordistancia[indicaciones -1][3] / velmoto
                                            tiempobici = cordistancia[indicaciones -1][3] / velbici
                                            tiempomoto = round(tiempomoto / 60,2)
                                            tiempobici = round(tiempobici / 60,2)
                                            print("Tiempo estimado en moto",tiempomoto,"minutos")
                                            print("Tiempo estimado en bicicleta",tiempobici,"minutos")
                                            time.sleep(2)
                                            while True:
                                                saliropci = input("Presione 0 para salir")
                                                if saliropci == "0":
                                                    break
                                        else:
                                            print("Error zona wifi")
                                            time.sleep(2)
                                            exit()
                                    except ValueError:
                                        print("Error zona wifi")
                                        time.sleep(2)
                                        exit()
                                else:
                                    print("Error ubicación")
                                    time.sleep(2)
                                    exit()    
                            except ValueError:
                                print("Error ubicación")
                                time.sleep(2)
                                exit()
                        #fin reto 4
                        
                        #reto 5
                        elif menu[opcion - 1] == "Guardar archivo con ubicación cercana":
                            if len(coordenadas) == 0:
                                print("Error de alistamiento")
                                time.sleep(2)
                                exit()
                            if len(ubicactual) == 0:
                                print("Error de alistamiento")
                                time.sleep(2)
                                exit()
                            diccionario ={"actual":ubicactual,"zonawifi1":[cordistancia[0][0:3]],"recorrido":[cordistancia[0][3],'Moto',tiempomoto]}
                            print(diccionario)
                            while True:
                                opmenu = input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal")
                                if opmenu == "1":
                                    try:
                                        File = open(r'D:\DESCARGAS\Archivo_reto5\zonacercana.txt',"w")
                                        File.write(str(diccionario))
                                        print("Exportando archivo")
                                        time.sleep(2)
                                        exit()
                                    except IOError:
                                        print("Exportando archivo")
                                        time.sleep(2)
                                        exit()
                                elif opmenu == "0":
                                    break
                        elif menu[opcion - 1] == "Actualizar registros de zonas wifi desde archivo":
                            try:    
                                File = open(r'D:\DESCARGAS\Archivo_reto5\actualizarzonas.txt')
                                indi = 0
                                for i in File.readlines():
                                    zonaswifi[indi] = i.strip().split(',')
                                    zonaswifi[indi][0] = float(zonaswifi[indi][0])
                                    zonaswifi[indi][1] = float(zonaswifi[indi][1])
                                    zonaswifi[indi][2] = int(zonaswifi[indi][2])
                                    indi +=1
                                print("estas son las zonas wifi actualizadas")
                                print(zonaswifi)
                                while True:
                                    opsubmenu = input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ")
                                    if opsubmenu == "0":
                                        break
                            except IOError:
                                while True:
                                    opsubmenu = input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ")
                                    if opsubmenu == "0":
                                        break
                            #fin reto 5

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