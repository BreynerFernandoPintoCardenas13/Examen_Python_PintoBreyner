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

def impuestoLocal(formato, valor):
    while True:
        impuestoLocalNumero = 8  # Impuesto Local al 8%
        valorIva = (valor / 100) * impuestoLocalNumero  # Cálculo del impuesto
        resultado = valor + valorIva  # Precio total con el impuesto

        # Guardamos los resultados en el formato que has definido
        formato[valor] = [{
            "valor ingresado": valor,
            "Impuesto Local": impuestoLocalNumero,
            "Total sumado": resultado,
            "tipo de impuesto": impuestoLocalNumero,
        }]
        
        # Mostrar los resultados al usuario
        print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Precio Base: ${valor}
        Impuesto(s):
        - Impuesto Local (8%): ${valorIva}
        Total con impuestos: ${resultado}
        """)

        # Opciones para agregar otro impuesto o regresar al menú principal
        print("""
                    ¿Desea agregar otro impuesto?
        1. Sí
        2. No (Regresa al menú principal)
        ---------------------------------------------------
        """)

        # Validación de la opción de agregar otro impuesto
        opcionOne=int(input("Ingresa una opcion valida: "))
        if opcionOne==1:
                print()
        elif opcionOne==2:
                from main import principal
                break
        print("""
        INGRESE UN TIPO DE IMPUESTO
        1. Impuesto Especial (5%)
        2. Impuesto Local (8%)
        3. Otro (permite ingresar una tasa personalizada)                     
                            """)
        opcion = int(input("cual impuesto? (1 para sí, 2 para no): "))

        if opcion==1:
                        volverAplicarN=(resultado/100)*5
                        resultadoF=resultado+volverAplicarN
                        print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Precio Base: ${valor}
        Impuesto(s):
        - IVA (10%): ${valorIva}
        - Impuesto local: ${volverAplicarN} 
        Total con impuestos: ${resultadoF}
        """)
                        from main import principal
                        principal()
        elif opcion==2:
                        volverAplicarN=(resultado/100)*8
                        resultadoF=resultado+volverAplicarN
                        print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Precio Base: ${valor}
        Impuesto(s):
        - IVA (10%): ${valorIva}
        - Impuesto local: ${volverAplicarN} 
        Total con impuestos: ${resultadoF}
        """)
                        from main import principal
                        principal()
        elif opcion==3:
                        desicion=float(input("ingrese el porcentaje de impuesto: "))
                        volverAplicarN=(resultado/100)*desicion
                        resultadoF=resultado+volverAplicarN
                        print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Precio Base: ${valor}
        Impuesto(s):
        - IVA (10%): ${valorIva}
        - Impuesto local: ${volverAplicarN} 
        Total con impuestos: ${resultadoF}
        """)
                        from main import principal
                        principal()
        return formato