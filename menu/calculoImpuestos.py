import match
import json
from logica.iva import read_file, write_file, precioIva
from logica.impuestoElegido import impuestoElegido
def menuCalculoImpuestos():
    while True:    
        formato=read_file("base.json")
        print("""
    ---------------------------------------------------
    CÁLCULO DE IMPUESTOS
    ---------------------------------------------------
            """)
        valor=float(input("    Ingrese el precio base del producto o servicio: "))
        print("""
    ---------------------------------------------------
    Seleccione el tipo de impuesto:
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (permite ingresar una tasa personalizada)
        """)
        desicion=int(input("        ingrese una opcion: "))
        match desicion:
            case 4:
                from logica.impuestoElegido import impuestoElegido
                impuesto=float(input("      Ingrese el valor del impuesto (en porcentaje) si seleccionó 'Otro':"))
                impuestoElegido(formato, impuesto, valor)
                write_file(formato, "base.json")
       
                desicion=int(input("          ingrese una opcion valida"))
                if desicion==1:
                    print()
                elif desicion==2:
                    from main import principal
                    principal()
        match desicion:
            case 1:
                from logica.iva import precioIva
                precioIva(formato, valor)
                write_file(formato, "base.json")
                print("""
                      ¿Desea agregar otro impuesto?
                1. Sí
            2. No (Regresa al menú principal)
            ---------------------------------------------------
        """)
                
                desicion=int(input("          ingrese una opcion valida"))
                if desicion==1:
                    print()
                elif desicion==2:
                    from main import principal
                    principal()
            case 2:
                from logica.impuestoEspecial import impuestoEspecial
                impuestoEspecial(formato, valor)
                write_file(formato, "base.json")
                print("""
                      ¿Desea agregar otro impuesto?
            1. Sí
            2. No (Regresa al menú principal)
            ---------------------------------------------------
        """)
                desicion=int(input("          ingrese una opcion valida"))
                if desicion==1:
                    print()
                elif desicion==2:
                    from main import principal
                    principal()
            case 3:
                from logica.impuestoLocal import impuestoLocal
                impuestoLocal(formato, valor)
                print("""
                      ¿Desea agregar otro impuesto?
            1. Sí
            2. No (Regresa al menú principal)
            ---------------------------------------------------
        """)
                write_file(formato, "base.json")
                desicion=int(input("          ingrese una opcion valida"))
                if desicion==1:
                    print()
                elif desicion==2:
                    from main import principal
                    principal()