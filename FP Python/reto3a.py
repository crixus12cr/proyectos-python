import os

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
            print("Sesión iniciada")
            
            def menu():
                print("1. Cambiar contraseña")
                print("2. Ingresar coordenadas actuales")
                print("3. Ubicar zona wifi más cercana")
                print("4. Guardar archivo con ubicación cercana")
                print("5. Actualizar registros de zonas wifi desde archivo")
                print("6. Elegir opción de menú favorita")
                print("7. Cerrar sesión.")
            
            def back_menu():
                while True:
                    menu()
                    inten=0
                    while inten <= 3:
                        cent=int(input("Elija una opción "))
                        if cent == 6:
                            favorita=int(input("Seleccione opción favorita "))

                            if favorita == 1:
                                
                                r1=4
                                adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                if adio == r1:
                                    r2=4
                                    adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                    if adis == 4:
                                        os.system('cls')
                                        print("1. Cambiar contraseña")
                                        print("2. Ingresar coordenadas actuales")
                                        print("3. Ubicar zona wifi más cercana")
                                        print("4. Guardar archivo con ubicación cercana")
                                        print("5. Actualizar registros de zonas wifi desde archivo")
                                        print("6. Elegir opción de menú favorita")
                                        print("7. Cerrar sesión.")
                                        inten=0
                                        while inten <= 3:                                    
                                            cent=int(input("Elija una opción "))
                                            if cent > 7:
                                                print("Error")
                                                inten=inten+1
                                                continue
                                            if cent >0 and cent <= 7:
                                                return cent
                                                break
                                            if inten >= 3:
                                                print("Error")
                                                exit()
                                    else:
                                        print("Error")
                                        cent=back_menu()
                                else:
                                    print("Error")
                                    cent=back_menu()

                                
                            elif favorita == 2:
                                
                                r1=4
                                adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                if adio == r1:
                                    r2=4
                                    adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                    if adis == 4:
                                        os.system('cls')
                                        print("1. Ingresar coordenadas actuales")
                                        print("2. Cambiar contraseña")
                                        print("3. Ubicar zona wifi más cercana")
                                        print("4. Guardar archivo con ubicación cercana")
                                        print("5. Actualizar registros de zonas wifi desde archivo")
                                        print("6. Elegir opción de menú favorita")
                                        print("7. Cerrar sesión.")
                                        inten=0
                                        while inten <= 3:                                    
                                            cent=int(input("Elija una opción "))

                                            if cent > 7:
                                                print("Error")
                                                inten=inten+1
                                                continue
                                            if cent >0 and cent <= 7:
                                                return cent
                                                break
                                            if inten >= 3:
                                                print("Error")
                                                exit()
                                    else:
                                        print("Error")
                                        cent=back_menu()
                                else:
                                    print("Error")
                                    cent=back_menu()

                            elif favorita == 3 :

                                r1=4
                                adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                if adio == r1:
                                    r2=4
                                    adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                    if adis == 4:
                                        os.system('cls')
                                        print("1. Ubicar zona wifi más cercana")
                                        print("2. Ingresar coordenadas actuales")
                                        print("3. Cambiar contraseña")
                                        print("4. Guardar archivo con ubicación cercana")
                                        print("5. Actualizar registros de zonas wifi desde archivo")
                                        print("6. Elegir opción de menú favorita")
                                        print("7. Cerrar sesión.")
                                        inten=0
                                        while inten <= 3:                                    
                                            cent=int(input("Elija una opción "))
                                            if cent > 7:
                                                print("Error")
                                                inten=inten+1
                                                continue
                                            if cent >0 and cent <= 7:
                                                return cent
                                                break
                                            if inten >= 3:
                                                print("Error")
                                                exit()
                                    else:
                                        print("Error")
                                        cent=back_menu()
                                else:
                                    print("Error")
                                    cent=back_menu()
                            elif favorita == 4:

                                r1=4
                                adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                if adio == r1:
                                    r2=4
                                    adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                    if adis == 4:
                                        os.system('cls')                                    
                                        print("1. Guardar archivo con ubicación cercana")
                                        print("2. Ingresar coordenadas actuales")
                                        print("3. Ubicar zona wifi más cercana")
                                        print("4. Cambiar contraseña")
                                        print("5. Actualizar registros de zonas wifi desde archivo")
                                        print("6. Elegir opción de menú favorita")
                                        print("7. Cerrar sesión.")
                                        inten=0
                                        while inten <= 3:                                    
                                            cent=int(input("Elija una opción "))
                                            if cent > 7:
                                                print("Error")
                                                inten=inten+1
                                                continue
                                            if cent >0 and cent <= 7:
                                                return cent
                                                break
                                            if inten >= 3:
                                                print("Error")
                                                exit()
                                    else:
                                        print("Error")
                                        cent=back_menu()
                                else:
                                    print("Error")
                                    cent=back_menu()

                            elif favorita == 5:

                                r1=4
                                adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                                if adio == r1:
                                    r2=4
                                    adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                                    if adis == 4:
                                        os.system('cls') 
                                        print("1. Actualizar registros de zonas wifi desde archivo")
                                        print("2. Ingresar coordenadas actuales")
                                        print("3. Ubicar zona wifi más cercana")
                                        print("4. Guardar archivo con ubicación cercana")
                                        print("5. Cambiar contraseña")
                                        print("6. Elegir opción de menú favorita")
                                        print("7. Cerrar sesión.")
                                        inten=0
                                        while inten <= 3:                                    
                                            cent=int(input("Elija una opción "))
                                            
                                            if cent > 7:
                                                print("Error")
                                                inten=inten+1
                                                continue
                                            if cent >0 and cent <= 7:
                                                return cent
                                                break
                                            if inten >= 3:
                                                print("Error")
                                                exit()
                                    else:
                                        print("Error")
                                        cent=back_menu()
                                else:
                                    print("Error")
                                    cent=back_menu()
                                    
                            else:
                                print("Error")
                                exit()
                        if cent > 7:
                            print("Error")
                            inten=inten+1
                            continue
                        if cent >0 and cent <= 7:
                            return cent
                            break
                        if inten >= 3:
                            print("Error")
                            exit()
                            
                    break
                    
                
            
            cent=back_menu()
            if cent == 1:
                print("Usted ha elegido la opción número 1")
                password=int(input("Ingrese la contraseña actual"))
                if password == pw:
                    newpass=int(input("Ingrese la nueva contraseña"))
                    if newpass == pw:
                        print("Error")
                        exit()
                    else:
                        pw=newpass
                        cent=back_menu()
                else:
                    print("Error")
                    exit()
            if cent == 2:
                print("Usted ha elegido la opción número 2")
            if cent == 3:
                print("Usted ha elegido la opción número 3")
            if cent == 4:
                print("Usted ha elegido la opción número 4")
            if cent == 5:
                    print("Usted ha elegido la opción número 5")
            if cent == 7:
                print("Hasta pronto")
                exit()   

        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")