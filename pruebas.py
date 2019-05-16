data='{ "codigo": "TCV-072",\
        "descripcion": "TIRA AZUL MARINO COSTA VERDE 24 NIÑO PAQUETES T/24",\
        "unimed": "PAQUETES",\
        "talla": "T/24",\
        "inv.inicial": 105.0,\
        "ingresos": 0,\
        "salidas": 0,\
        "saldo.actual": 105.0,\
        "cotizaciones": [\
            {\
                "id": 7,\
                "codigo": 1,\
                "descripcion": "Inventario Inicial",\
                "cantidad": 105.0,\
                "precio": 2.8,\
                "imptotal": 294.0\
            }\
        ]\
    },\
    {\
        "codigo": "TCV-073",\
        "descripcion": "TIRA PLOMO COSTA VERDE 24 NIÑO PAQUETES T/24",\
        "unimed": "PAQUETES",\
        "talla": "T/24",\
        "inv.inicial": 57.0,\
        "ingresos": 65.0,\
        "salidas": 0,\
        "saldo.actual": 122.0,\
        "cotizaciones": [\
            {\
                "id": 7,\
                "codigo": 1,\
                "descripcion": "Inventario Inicial",\
                "cantidad": 57.0,\
                "precio": 2.8,\
                "imptotal": 159.6\
            },\
            {\
                "id": 7,\
                "codigo": 19,\
                "descripcion": "Ingreso Producto",\
                "cantidad": 65.0,\
                "precio": 2.8,\
                "imptotal": 182.0\
            }\
        ]\
    }'\

print (data)

for item in data:
    print (item[0])
    