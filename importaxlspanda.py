import sqlite3
import pandas as pd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#nombretabla='gestionapp_articulo'
nombretabla='gestionapp_material'

filename="E:\proyectosdjango\Insumos_app_inventarios\PRUEBA3.xlsx"
#con=sqlite3.connect('dbinventario.sqlite3')

con = sqlite3.connect("dbinventario.sqlite3")
 # Get a cursor object
cursor      = con.cursor()
dropTableStatement = "DELETE FROM " + nombretabla


cursor.execute(dropTableStatement)
df = pd.read_excel(filename, sheet_name='Sheet1')
print("Column headings:")
print(df.columns)

df.to_sql(nombretabla,con,if_exists='append', index=False)
con.commit()
con.close()



#wb=pd.read_excel(filename,sheet_name='hoja1')
#for sheet in wb:
#    wb[sheet].to_sql(sheet,con, index=False)
