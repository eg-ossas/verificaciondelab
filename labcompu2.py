curso = input("¿Estas cursando de segundo año o superior? (si/no)\n")

if curso.lower() == "si":
    arancel = input ("¿Tienes el arancel al día? (si/no)\n")
    if arancel.lower() == "si":
        susp = input("¿Estas suspendido? (si/no)\n")
        if susp.lower() == "no":
            print("Acceso Autorizado")
        else:
            print("Denegado")
            print("Actualmente usted se encuentra suspendido")
    else:
        print("Denegado")
        print("Usted no tiene el arancel al día")
else:
    print("Denegado")
    print("Usted no se encuentra en segundo año o superior")