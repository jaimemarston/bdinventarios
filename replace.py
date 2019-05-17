import sqlite3


#nombretabla='gestionapp_articulo'
#nombretabla='gestionapp_material'

con = sqlite3.connect("dbinventario.sqlite3")
cursor      = con.cursor()
#Statement = "UPDATE " + nombretabla + " SET descolor = color "
#Statement = "update gestionapp_dmateriales set codpro = (select gestionapp_material.codigo  from gestionapp_material where gestionapp_material.descripcion = gestionapp_dmateriales.descripcion)"
#Statement = "update gestionapp_dcotizacion set codpro = (select gestionapp_articulo.codigo  from gestionapp_articulo where gestionapp_articulo.descripcion = gestionapp_dcotizacion.descripcion)"

if 1==2:
    Statement = "update gestionapp_dmateriales set modelo  = (select gestionapp_material.modelo   from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "genero  = (select gestionapp_material.genero       from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "precio  = (select gestionapp_material.precioventa  from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "unimed  = (select gestionapp_material.unimed       from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "desunimed  = (select gestionapp_material.unimed       from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "talla   = (select gestionapp_material.talla        from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro),"
    Statement += "tipo    = (select gestionapp_material.tipo         from gestionapp_material where gestionapp_material.codigo = gestionapp_dmateriales.codpro)"

if 1==2:
    Statement = "update gestionapp_dcotizacion set modelo  = (select gestionapp_articulo.modelo   from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "genero  = (select gestionapp_articulo.genero       from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "precio  = (select gestionapp_articulo.precioventa  from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "unimed  = (select gestionapp_articulo.unimed       from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "desunimed  = (select gestionapp_articulo.unimed       from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "talla   = (select gestionapp_articulo.talla        from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro),"
    Statement += "tipo    = (select gestionapp_articulo.tipo         from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro)"

if 1==1:
    Statement = "update gestionapp_dcotizacion set genero  = (select gestionapp_articulo.genero   from gestionapp_articulo where gestionapp_articulo.codigo = gestionapp_dcotizacion.codpro)"
#print (Statement)

#Statement = "update gestionapp_dcotizacion set imptotal = precio * cantidad "
#Statement = "update gestionapp_dmateriales set imptotal = precio * cantidad "

cursor.execute(Statement)
con.commit()

con.close()
