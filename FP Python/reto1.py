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
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")