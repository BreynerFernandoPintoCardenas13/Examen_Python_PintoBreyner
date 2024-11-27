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
    valorIva=(valor/100)*impuesto
    resultado=valor + valorIva
    formato[valor]=[{
        "valor ingresado": valor,
        "valor del impuesto": valorIva,
        "Total sumado": resultado,
        "Tipo de impuesto": impuesto,
    }
    ]
    print(f"""
            ---------------------------------------------------
                RESULTADO DEL CÁLCULO
            ---------------------------------------------------
            Precio Base: ${valor}
            Impuesto(s):{impuesto}
            valor del impuesto: {valorIva},
            Total con impuestos: ${resultado}
""")
    return formato, resultado