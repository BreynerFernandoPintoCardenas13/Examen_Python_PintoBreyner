def impuestoLocal(formato, valor):
    impuestoLocalNumero=8
    valorIva=(valor/100)*impuestoLocalNumero
    resultado=valor + valorIva
    formato[valor]=[{
        "valor ingresado": valor,
        "Impuesto Local": impuestoLocalNumero,
        "Total sumado": resultado,
        "tipo de impuesto": impuestoLocalNumero,
    }
    ]
    print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Precio Base: ${valor}
    Impuesto(s):
    - Impuesto Especial (5%): $[valor del impuesto local] ${valorIva}
    Total con impuestos: ${resultado}

""")
    return formato, resultado