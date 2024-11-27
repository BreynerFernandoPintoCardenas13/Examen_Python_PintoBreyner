import match 
def menuPrincipal():
    print("""
        ---------------------------------------------------
                CALCULADORA DE IMPUESTOS
        ---------------------------------------------------
        Seleccione una opción:
        ---------------------------------------------------
                CALCULADORA DE IMPUESTOS
        ---------------------------------------------------
        Seleccione una opción:
        1. Calcular impuesto sobre un producto o servicio
        2. Ver lista de tipos de impuestos
        3. Salir
        ---------------------------------------------------
""")
    desicion=int(input("ingresa una opcion valida: "))
    while True:    
        match desicion:
            case 1:
                from menu.calculoImpuestos import menuCalculoImpuestos
                menuCalculoImpuestos()
            case 2:
                from menu.lista import lista
                lista()
            case 3:
                from menu.bye import bye
                bye()
                break