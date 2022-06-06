while True:
    try:
        hora=int(input("¿Que hora es?="))
    except:
        print("Favor ingresar un número, intenta de nuevo")
        continue
    
    if hora<0 or hora >=23:
        print("Favor ingresar un número entre 0 y 23, intenta de nuevo")
        continue
    if hora>=0 and hora<13:
        print("buenos dias")
    if hora>12 and hora<19:
        print("buenas tardes")
    if hora>18 and hora<24:
        print("buenas noches")
    break
print("SALIÓ DEL WHILE TRUE")