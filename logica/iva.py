import json  # Para trabajar con archivos JSON
from tabulate import tabulate  

def read_file(path):
    try:
        with open(f"databses/{path}", "r") as file:
            data = file.read() 
            return json.loads(data)  
    except FileNotFoundError:
        return {}  
    
def write_file(data, path):
    with open(f"databses/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)  

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

def precioIva(formato, valor):
     while True:    
        iva = 10
        valorIva = (valor / 100) * iva
        resultado = valor + valorIva
        formato[valor] = [{
            "valor ingresado": valor,
            "Iva": valorIva,
            "Total sumado": resultado,
            "tipo de impuesto": iva,
        }]
        
        print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Precio Base: ${valor}
        Impuesto(s):
        - IVA (10%): ${valorIva}
        Total con impuestos: ${resultado}
        """)

        print("""
                    ¿Desea agregar otro impuesto?
        1. Sí
        2. No (Regresa al menú principal)
        ---------------------------------------------------
        """)
        opcionOne=int(input("Ingresa una opcion valida: "))
        if opcionOne==1:
              print()
        elif opcionOne==2:
              from main import principal
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
                    break
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