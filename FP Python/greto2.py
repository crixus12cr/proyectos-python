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
            #menu
            
            def opcion():
                intentos=0
                while intentos <= 3:
                    
                    cent=int(input("Elija una opción "))
                    if cent > 0 and cent <= 7:
                        break
                    else:
                        print("Error")
                        intentos=intentos+1
                        if intentos > 3:
                            print("Error")
                            quit()
                        continue
                return cent
            
            def menu():
                contra="Cambiar contraseña"
                coordenadas="Ingresar coordenadas actuales"
                ubicar="Ubicar zona wifi más cercana"
                guardar="Guardar archivo con ubicación cercana"
                actualizar="Actualizar registros de zonas wifi desde archivo"
                print("1.",contra)
                print("2.",coordenadas)
                print("3.",ubicar)
                print("4.",guardar)
                print("5.",actualizar)
                print("6. Elegir opción de menú favorita")
                print("7. Cerrar sesión.")
            
            def Actualizar_menu():
                cent = 6
                if cent == 6:
                    favorita=int(input("Seleccione opción favorita "))
                    if favorita == 1:
                        
                        r1=4
                        adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                        if adio == r1:
                            r2=4
                            adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                            if adis == r2:
                                os.system('cls')
                                contra="Cambiar contraseña"
                                coordenadas="Ingresar coordenadas actuales"
                                ubicar="Ubicar zona wifi más cercana"
                                guardar="Guardar archivo con ubicación cercana"
                                actualizar="Actualizar registros de zonas wifi desde archivo"
                                print("1.",contra)
                                print("2.",coordenadas)
                                print("3.",ubicar)
                                print("4.",guardar)
                                print("5.",actualizar)
                                print("6. Elegir opción de menú favorita")
                                print("7. Cerrar sesión.")
                                inten=0
                                while inten <= 3:                                    
                                    cent=int(input("Elija una opción "))
                                    if cent == 6:
                                        return Actualizar_menu()
                                    if cent > 7:
                                        print("Error")
                                        inten=inten+1
                                        continue
                                    if cent >0 and cent <= 7:
                                        return cent
                                    if inten >= 3:
                                        print("Error")
                                        quit()
                            else:
                                print("Error")
                                return
                        else:
                            print("Error")
                            return
                        return cent

                    if favorita == 2:
                    
                        r1=4
                        adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                        if adio == r1:
                            r2=4
                            adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                            if adis == r2:
                                os.system('cls')
                                contra="Cambiar contraseña"
                                coordenadas="Ingresar coordenadas actuales"
                                ubicar="Ubicar zona wifi más cercana"
                                guardar="Guardar archivo con ubicación cercana"
                                actualizar="Actualizar registros de zonas wifi desde archivo"
                                print("1.",coordenadas)
                                print("2.",contra)
                                print("3.",ubicar)
                                print("4.",guardar)
                                print("5.",actualizar)
                                print("6. Elegir opción de menú favorita")
                                print("7. Cerrar sesión.")
                                inten=0
                                while inten <= 3:                                    
                                    cent=int(input("Elija una opción "))
                                    if cent == 6:
                                        return Actualizar_menu()
                                    if cent > 7:
                                        print("Error")
                                        inten=inten+1
                                        continue
                                    if cent >0 and cent <= 7:
                                        return cent
                                    if inten >= 3:
                                        print("Error")
                                        quit()
                            else:
                                print("Error")
                                return
                        else:
                            print("Error")
                            return
                        return cent
                    if favorita == 3:
                    
                        r1=4
                        adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                        if adio == r1:
                            r2=4
                            adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                            if adis == r2:
                                os.system('cls')
                                contra="Cambiar contraseña"
                                coordenadas="Ingresar coordenadas actuales"
                                ubicar="Ubicar zona wifi más cercana"
                                guardar="Guardar archivo con ubicación cercana"
                                actualizar="Actualizar registros de zonas wifi desde archivo"
                                print("1.",ubicar)
                                print("2.",coordenadas)
                                print("3.",contra)
                                print("4.",guardar)
                                print("5.",actualizar)
                                print("6. Elegir opción de menú favorita")
                                print("7. Cerrar sesión.")
                                inten=0
                                while inten <= 3:                                    
                                    cent=int(input("Elija una opción "))
                                    if cent == 6:
                                        return Actualizar_menu()
                                    if cent > 7:
                                        print("Error")
                                        inten=inten+1
                                        continue
                                    if cent >0 and cent <= 7:
                                        return cent
                                    if inten >= 3:
                                        print("Error")
                                        quit()
                            else:
                                print("Error")
                                return
                        else:
                            print("Error")
                            return
                        return cent
                    if favorita == 4:
                    
                        r1=4
                        adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                        if adio == r1:
                            r2=4
                            adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                            if adis == r2:
                                os.system('cls')
                                contra="Cambiar contraseña"
                                coordenadas="Ingresar coordenadas actuales"
                                ubicar="Ubicar zona wifi más cercana"
                                guardar="Guardar archivo con ubicación cercana"
                                actualizar="Actualizar registros de zonas wifi desde archivo"
                                print("1.",guardar)
                                print("2.",coordenadas)
                                print("3.",ubicar)
                                print("4.",contra)
                                print("5.",actualizar)
                                print("6. Elegir opción de menú favorita")
                                print("7. Cerrar sesión.")
                                inten=0
                                while inten <= 3:                                    
                                    cent=int(input("Elija una opción "))
                                    if cent == 6:
                                        return Actualizar_menu()
                                    if cent > 7:
                                        print("Error")
                                        inten=inten+1
                                        continue
                                    if cent >0 and cent <= 7:
                                        return cent
                                    if inten >= 3:
                                        print("Error")
                                        quit()
                            else:
                                print("Error")
                                return
                        else:
                            print("Error")
                            return
                        return cent
                    if favorita == 5:
                    
                        r1=4
                        adio=int(input("Para confirmar por favor responda: Las estaciones del año y tambien los elementos y los puntos cardinales, este número represento, la respuesta es: "))
                        if adio == r1:
                            r2=4
                            adis=int(input("Para confirmar por favor responda: Soy un número y no miento al decir que tengo forma de asiento, la respuesta es: "))
                            if adis == r2:
                                os.system('cls')
                                contra="Cambiar contraseña"
                                coordenadas="Ingresar coordenadas actuales"
                                ubicar="Ubicar zona wifi más cercana"
                                guardar="Guardar archivo con ubicación cercana"
                                actualizar="Actualizar registros de zonas wifi desde archivo"
                                print("1.",actualizar)
                                print("2.",coordenadas)
                                print("3.",ubicar)
                                print("4.",guardar)
                                print("5.",contra)
                                print("6. Elegir opción de menú favorita")
                                print("7. Cerrar sesión.")
                                inten=0
                                while inten <= 3:                                    
                                    cent=int(input("Elija una opción "))
                                    if cent == 6:
                                        return Actualizar_menu()
                                    if cent > 7:
                                        print("Error")
                                        inten=inten+1
                                        continue
                                    if cent >0 and cent <= 7:
                                        return cent
                                    if inten >= 3:
                                        print("Error")
                                        quit()
                            else:
                                print("Error")
                                return
                        else:
                            print("Error")
                            return
                        return cent



            while True:
                cent=0
                menu()
                cent=opcion()

                if cent == 6:
                    cent=Actualizar_menu()

                cent=cent

                if cent == 1:
                    print("Usted ha elegido la opción número 1")
                    quit()

                if cent == 2:
                        print("Usted ha elegido la opción número 2")
                        quit()

                if cent == 3:
                        print("Usted ha elegido la opción número 3")
                        quit()

                if cent == 4:
                        print("Usted ha elegido la opción número 4")
                        quit()

                if cent == 5:
                        print("Usted ha elegido la opción número 5")
                        quit()

                

                if cent == 7:
                    print ("Hasta pronto")
                    quit()

        
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")