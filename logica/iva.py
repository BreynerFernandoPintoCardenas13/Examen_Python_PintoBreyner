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


def precioIva(formato, valor):
    iva=10
    valorIva=(valor/100)*iva
    resultado=valor + valorIva
    formato[valor]=[{
        "valor ingresado": valor,
        "Iva": valorIva,
        "Total sumado": resultado,
        "tipo de impuesto": iva,
    }
    ]
    print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Precio Base: ${valor}
    Impuesto(s):
    - IVA (10%): ${valorIva}
    Total con impuestos: ${resultado}

""")
    return formato, resultado