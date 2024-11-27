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

def impuestoElegido(formato, impuesto, valor):
    while True:
        valorIva = (valor / 100) * impuesto
        resultado = valor + valorIva

        # Guardamos los resultados en el diccionario 'formato' con 'valor' como clave
        formato[valor] = [{
            "valor ingresado": valor,
            "valor del impuesto": valorIva,
            "Total sumado": resultado,
            "Tipo de impuesto": impuesto,
        }]
        
        # Impresión de los resultados
        print(f"""
                ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
                ---------------------------------------------------
                Precio Base: ${valor}
                Impuesto(s): {impuesto}%
                Valor del impuesto: ${valorIva}
                Total con impuestos: ${resultado}
        """)
        opcion=int(input("Desea salir? S/1 O N/2"))
        if opcion==1:
            from main import principal
            principal()
            break
        if opcion==2:
            
            return formato, resultado
