def impuestoEspecial(formato, valor):
    impuestoEspecialNumero=5
    valorIva=(valor/100)*impuestoEspecialNumero
    resultado=valor + valorIva
    formato[+1]=[{
        "valor ingresado": valor,
        "Iva": valorIva,
        "Total sumado": resultado,
        "Tipo de impuesto": impuestoEspecialNumero,
    }
    ]
    print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Precio Base: ${valor}
    Impuesto(s):
    -Impuesto Especial (5%): ${valorIva}
    Total con impuestos: ${resultado}
""")
    return formato, resultado