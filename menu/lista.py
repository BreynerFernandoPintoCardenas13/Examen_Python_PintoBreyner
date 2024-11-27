def lista():
    print("""

    ---------------------------------------------------
               TIPOS DE IMPUESTOS
    ---------------------------------------------------
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (Personalizado)

    ¿Desea calcular un impuesto ahora?
    1. Sí (Regresa al cálculo)
    2. No (Regresa al menú principal)
    ---------------------------------------------------
""")   
    desicion=int(input("ingresa una opcion valida: "))
    if desicion==1:
        from menu.calculoImpuestos import menuCalculoImpuestos
        menuCalculoImpuestos()
    if desicion==2:
        from main import principal
        principal()
    else:
        print("error intente de nuevo con un caracter valido")