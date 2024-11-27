import match
import json
from logica.iva import read_file, write_file, precioIva
from logica.impuestoElegido import impuestoElegido
import keyboard  # Para la validación con la librería keyboard

def validar_numero_ingresado(mensaje):
    while True:
        try:
            valor = input(mensaje)
            # Comprobamos si la entrada no es un número válido
            if not valor.replace(".", "", 1).isdigit():  # Permite un solo punto decimal
                raise ValueError("Valor no válido. Por favor ingrese un número válido.")
            return float(valor)
        except ValueError as e:
            print(e)

def menuCalculoImpuestos():
    while True:    
        formato = read_file("base.json")
        print("""
    ---------------------------------------------------
    CÁLCULO DE IMPUESTOS
    ---------------------------------------------------
            """)
        # Validación del precio base
        valor = validar_numero_ingresado("    Ingrese el precio base del producto o servicio: ")
        
        print("""
    ---------------------------------------------------
    Seleccione el tipo de impuesto:
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (permite ingresar una tasa personalizada)
        """)
        
        # Validación de la opción de impuesto
        while True:
            try:
                desicion = int(input("        ingrese una opcion: "))
                if desicion not in [1, 2, 3, 4]:
                    raise ValueError("Opción no válida. Ingrese una opción entre 1 y 4.")
                break
            except ValueError as e:
                print(e)
        
        match desicion:
            case 4:
                from logica.impuestoElegido import impuestoElegido
                impuesto = validar_numero_ingresado("      Ingrese el valor del impuesto (en porcentaje) si seleccionó 'Otro':")
                impuestoElegido(formato, impuesto, valor)
                write_file(formato, "base.json")
                
                desicion = int(input("          ingrese una opcion valida"))
                if desicion == 1:
                    print()
                elif desicion == 2:
                    from main import principal
                    principal()
                    break
                
            case 1:
                from logica.iva import precioIva
                precioIva(formato, valor)
                write_file(formato, "base.json")
                
                desicion = int(input("          ingrese una opcion valida"))
                if desicion == 1:
                    print()
                elif desicion == 2:
                    from main import principal
                    principal()
                    break

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
                desicion = int(input("          ingrese una opcion valida"))
                if desicion == 1:
                    print()
                elif desicion == 2:
                    from main import principal
                    principal()
                    break

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
                desicion = int(input("          ingrese una opcion valida"))
                if desicion == 1:
                    print()
                elif desicion == 2:
                    from main import principal
                    principal()
                    break
