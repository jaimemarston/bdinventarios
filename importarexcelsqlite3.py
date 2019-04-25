
import sqlite3
try:

    bd = sqlite3.connect("db.sqlite3")
    
    print("Base de datos abierta correctamente")

    cursor = bd.cursor()
    #res = cursor.execute("SELECT * FROM gestionapp_articulo ;")
    cursor.execute("SELECT npasajeros, descripcion, placa, color FROM gestionapp_unidad ;")
    res = cursor.fetchall()
    
    
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
    print("|{:^20}|{:^20}|{:^10}|{:^50}|".format("codigo", "descripcion", "placa", "color"))
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
 
    for npasajeros, descripcion, placa, color in res:
        print("|{:^20}|{:^20}|{:^10}|{:^50}|".format(npasajeros, descripcion, placa, color))
 
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))


except sqlite3.OperationalError as error:
    print("Error al abrir:", error)