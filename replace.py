import sqlite3


#nombretabla='gestionapp_articulo'
#nombretabla='gestionapp_material'

con = sqlite3.connect("dbinventario.sqlite3")
cursor      = con.cursor()
#Statement = "UPDATE " + nombretabla + " SET descolor = color "
#Statement = "update gestionapp_dmateriales set codpro = (select gestionapp_material.codigo  from gestionapp_material where gestionapp_material.descripcion = gestionapp_dmateriales.descripcion)"
Statement = "update gestionapp_dcotizacion set codpro = (select gestionapp_articulo.codigo  from gestionapp_articulo where gestionapp_articulo.descripcion = gestionapp_dcotizacion.descripcion)"

cursor.execute(Statement)
con.commit()
con.close()
